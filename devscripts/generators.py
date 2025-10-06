import subprocess
import sys
import glob
import os


def generate_ui():
    ui_path = "src/orienteering_startlist_screen\\ui\\"
    commands = []

    ui_files = glob.glob(os.path.join(ui_path, "*.ui"))
    for ui_file in ui_files:
        filename = os.path.splitext(os.path.basename(ui_file))[0]
        output_file = os.path.join(ui_path, f"{filename}_ui.py")
        command = f"poetry run pyside6-uic {ui_file} -o {output_file} --python-paths .\\src --absolute-imports"
        # --python-paths .\src\orienteering_startlist_screen\ Python paths for –absolute-imports.
        # --star-imports                        Python: Use * imports
        # --from-imports	                    Python: generate imports relative to '.'
        # --absolute-imports                    Python: generate absolute imports
        commands.append(command)

    for cmd in commands:
        print(cmd)
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            sys.exit(result.returncode)


def generate_rcc():
    resources_path = "src/orienteering_startlist_screen\\resources\\"
    resources_out_path = "src/orienteering_startlist_screen\\resources\\"
    commands = []

    rcc_files = glob.glob(os.path.join(resources_path, "*.qrc"))
    for rcc_file in rcc_files:
        filename = os.path.splitext(os.path.basename(rcc_file))[0]
        output_file = os.path.join(resources_out_path, f"{filename}_rc.py")
        command = f"poetry run pyside6-rcc {rcc_file} -o {output_file}"
        print(command)
        commands.append(command)

    for cmd in commands:
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            sys.exit(result.returncode)
