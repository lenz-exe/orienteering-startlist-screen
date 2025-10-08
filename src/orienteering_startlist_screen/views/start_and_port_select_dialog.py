import logging
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMessageBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QDialogButtonBox,
)
from PySide6.QtGui import QIntValidator

from orienteering_startlist_screen.ui.start_port_select_dialog_ui import (
    Ui_StartPortSelectDialog,
)

logger = logging.getLogger(__name__)


class StartAndPortSelectDialog(QtWidgets.QDialog):
    def __init__(
        self, start_name_list: list, parent=None, max_servers: int | None = None
    ):
        super().__init__(parent)
        self.ui = Ui_StartPortSelectDialog()
        self.ui.setupUi(self)

        self.result_data: list[dict] = []
        self._rows: list[dict[str, QLineEdit | QComboBox]] = []

        if max_servers is None:
            cpu_count = os.cpu_count() or 4
            max_servers = max(1, cpu_count - 1 if cpu_count > 2 else 1)
        self.max_servers = max_servers

        self.ui.scrollArea.setWidgetResizable(True)
        content = self.ui.scrollAreaWidgetContents

        container_layout = content.layout()
        if container_layout is None:
            container_layout = QVBoxLayout(content)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setSpacing(6)

        # start_name_list.sort(key=lambda x: int(x.split()[1]))
        start_name_list = sorted(start_name_list, key=lambda x: int(x.split()[1]))

        choices = ["---"] + start_name_list

        port = 5000
        for _ in choices:
            row_layout = QHBoxLayout()

            host_le = QLineEdit("127.0.0.1")
            host_le.setReadOnly(True)

            port_le = QLineEdit(str(port))
            port_le.setValidator(QIntValidator(1, 65535, self))
            port += 1

            combo = QComboBox()
            combo.addItems(choices)
            combo.setCurrentIndex(0)
            fm = combo.fontMetrics()
            w = (
                max(
                    fm.horizontalAdvance(combo.itemText(i))
                    for i in range(combo.count())
                )
                + 32
            )
            combo.setMinimumWidth(max(150, w))

            row_layout.addWidget(combo)
            row_layout.addWidget(host_le)
            row_layout.addWidget(port_le)

            row_widget = QWidget()
            row_widget.setLayout(row_layout)
            container_layout.addWidget(row_widget)

            self._rows.append({"host_le": host_le, "port_le": port_le, "combo": combo})

            # set trigger for changes at the QComboBox
            combo.currentIndexChanged.connect(self.on_combo_changed)

        container_layout.addStretch(1)

        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply).setEnabled(
            False
        )
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(
            self.handle_apply
        )
        self.ui.label_max_servers.setText(f"Selected: 0 / {self.max_servers}")
        self.enforce_selection_cap()

    def on_combo_changed(self, _index: int):
        self.enforce_selection_cap()

    def enforce_selection_cap(self):
        # count active selected (≠ '---')
        selected_count = sum(1 for r in self._rows if r["combo"].currentIndex() > 0)

        # if limit reached: all combo boxes left set on deactivated
        limit_reached = selected_count >= self.max_servers
        for row in self._rows:
            combo = row["combo"]
            is_selected = combo.currentIndex() > 0
            if is_selected:
                combo.setEnabled(True)  # already selected stay always editable
            else:
                combo.setEnabled(not limit_reached)  # lock remaining, if limit reached

        any_selected = selected_count > 0
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(any_selected)

        self.ui.label_max_servers.setText(
            f"Selected: {selected_count} / {self.max_servers}"
        )

    def update_apply_enabled(self):
        any_selected = any(r["combo"].currentText() != "---" for r in self._rows)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(any_selected)

    def handle_apply(self):
        errors = []
        results = []
        for row in self._rows:
            combo_box = row["combo"].currentText()
            if combo_box == "---":
                continue

            host = row["host_le"].text().strip()
            port_text = row["port_le"].text().strip()

            # simple port validation
            # port range: 1 - 65535 (16-Bit)
            # reserved ports:
            #   - 0-1023: "well-known ports" (HTTP 80, HTTPS 443, SSH 22, ...)
            # recommended ports:
            #   - 1024-49151: "registered ports"
            #   - 1024–49151 = "registered ports" – may also be occupied, but are usually unproblematic.
            #   - 49152–65535 = "ephemeral/dynamic ports" – fewest conflicts, ideal for test and development servers
            if not port_text.isdigit():
                errors.append(f"Invalid port: {port_text}")
                continue
            if not (1 <= int(port_text) <= 65535):
                errors.append(f"Port is out of range (1-65535): {port_text}")
                continue
            results.append(
                {
                    "host": host,
                    "port": int(port_text),
                    "combo": combo_box,
                }
            )

        if errors:
            QMessageBox.warning(self, "Input Error", "\n".join(errors))
            return
        if not results:
            QMessageBox.information(self, "Note", "Please select at least one option.")
            return

        if len(results) > self.max_servers:
            QMessageBox.warning(
                self,
                "Limit Exceeded",
                f"Maximum number of servers reached: {self.max_servers}",
            )
            return
        self.result_data = results
        self.accept()
