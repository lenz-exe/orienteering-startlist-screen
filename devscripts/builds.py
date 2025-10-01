import subprocess
import sys
import shutil
import os
import uuid
from typing import Optional

from src.orienteering_startlist_screen import config


class InnoSetupScriptGenerator:
    def __init__(
        self,
        app_name: str,
        app_version: str,
        app_icon_path: str,
        installer_exe_output_dir: str,
        exe_name: str,
        app_id_txt_path: str,
        pyinstaller_gen_output_dir: str,
        org_name: str = "Example Company",
        org_url: str = "https://www.example.com",
        installer_name: Optional[str] = None,
        need_admin_install: bool = False,
    ):
        """
        Class to generate the .iss file for the Inno Setup Compiler.

        :param app_name: The name of the app/tool
        :param app_version: The version of the app/tool e.g: '1.0.0
        :param app_icon_path: The Path to the icon of the app/tool e.g: 'G:\\GIT\\toolname\\icons\\kft_logo.ico'
        :param installer_exe_output_dir: Path to the directory where the generated installer exe file get placed
        :param exe_name: Name of the exe file which get created by the PyInstaller
        :param app_id_txt_path: Path to the txt file which containes the app_id. If file not found a new gets created
        :param pyinstaller_gen_output_dir: Path to the folder with the generated files/folders from PyInstaller
        :param org_name: The name of the organisation e.g.: 'Example Company'
        :param org_url: The url of the organisation e.g.: 'https://www.example.com'
        :param installer_name: Name of the installer e.g.: 'installer_toolname_1_0_0.exe'
        :param need_admin_install: Whether the installer should be installed as administrator or not
        """
        try:
            if not os.path.isfile(app_icon_path):
                raise FileNotFoundError(app_icon_path)
            if not os.path.isdir(installer_exe_output_dir):
                raise NotADirectoryError(installer_exe_output_dir)

            self.app_name = app_name
            self.app_version = app_version
            self.app_icon_path = app_icon_path
            self.installer_exe_output_dir = installer_exe_output_dir
            self.exe_name = exe_name
            self.app_id_txt_path = app_id_txt_path
            self.pyinstaller_gen_output_dir = pyinstaller_gen_output_dir
            self.org_name = org_name
            self.org_url = org_url
            if not installer_name:
                self.installer_name = self.normalize_installer_name()
            else:
                self.installer_name = installer_name
            self.need_admin_install = need_admin_install

            self.app_id = self.load_or_generate_app_id()
        except Exception as e:
            raise Exception(e)

    def load_or_generate_app_id(self) -> str:
        try:
            if os.path.exists(self.app_id_txt_path):
                with open(self.app_id_txt_path, "r") as file:
                    app_id = file.read().strip()
                    return app_id
            else:
                app_id = str(uuid.uuid4())
                with open(self.app_id_txt_path, "w") as file:
                    file.write(app_id)
                return app_id
        except Exception as e:
            raise Exception(e)

    def normalize_installer_name(self) -> str:
        """
        When no installer name is provided, the installer name gets generated out of the app_name and the app_version.
        """
        temp_name = self.app_name.lower().replace("-", "_")
        version = self.normalize_version()
        installer_name = f"installer_{temp_name}_{version}"
        return installer_name

    def normalize_version(self) -> str:
        """
        Removes the dots out of the version string and replace it with underscores.
        """
        version = self.app_version.replace(".", "_")
        return version

    def generate_iss_file(self, iss_file_output_dir: str):
        """
        :param iss_file_output_dir: Path to the directory where the generated iss file get placed
        """
        try:
            if not os.path.isdir(iss_file_output_dir):
                raise NotADirectoryError(iss_file_output_dir)

            app_id_str = "{{" + self.app_id + "}"

            if self.need_admin_install:
                admin_install_str = ""
            else:
                admin_install_str = "PrivilegesRequired=lowest"

            tasks_description = "{cm:CreateDesktopIcon}"
            tasks_group_description = "{cm:AdditionalIcons}"
            icon_autoporgrams_name = "{autoprograms}\\" + self.app_name
            icon_autoporgrams_filename = "{app}\\" + self.exe_name
            icon_autodesktop_name = "{autodesktop}\\" + self.app_name
            icon_autodesktop_filename = "{app}\\" + self.exe_name

            files = get_files_and_folders(target_dir=self.pyinstaller_gen_output_dir)
            files_str = "\n".join([f"{file}" for file in files])

            script_content = rf"""[Setup]
AppId={app_id_str}
AppName={self.app_name}
AppVersion={self.app_version}
AppPublisher={self.org_name}
AppPublisherURL={self.org_url}
AppSupportURL={self.org_url}
AppUpdatesURL={self.org_url}
DefaultDirName=C:\\ExampleCompany\\{self.app_name}
DisableProgramGroupPage=yes
PrivilegesRequiredOverridesAllowed=dialog
OutputDir={self.installer_exe_output_dir}
OutputBaseFilename={self.installer_name}
SetupIconFile={self.app_icon_path}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
{admin_install_str}

[Languages]
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{tasks_description}"; GroupDescription: "{tasks_group_description}"; Flags: unchecked

[Files]
{files_str}

[Icons]
Name: "{icon_autoporgrams_name}"; Filename: "{icon_autoporgrams_filename}"
Name: "{icon_autodesktop_name}"; Filename: "{icon_autodesktop_filename}"; Tasks: desktopicon
            """

            with open(
                os.path.join(iss_file_output_dir, f"{self.app_name}.iss"), "w"
            ) as f:
                f.write(script_content)
        except Exception as e:
            raise Exception(e)


def compile_installer_exe(
    iss_file_path: str, compiler_path: Optional[str] = None
) -> bool:
    try:
        if compiler_path and not os.path.isfile(compiler_path):
            raise FileNotFoundError(
                f"The given compiler path {compiler_path} not found"
            )
        compiler_path = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

        if not os.path.exists(compiler_path):
            compiler_path = search_for_inno_setup_folder()

            if not compiler_path:
                compiler_path = input(
                    "Der Inno Setup Compiler konnte nicht automatisch gefunden werden. "
                    "Bitte den Pfad zur ISCC.exe angeben: "
                )
                if not os.path.exists(compiler_path):
                    print("Der angegebene Pfad ist ungültig. Das Skript wird beendet.")
                    return False

        command = [compiler_path, iss_file_path]

        try:
            subprocess.run(command, check=True)
            print("Kompilierung erfolgreich!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Kompilierung: {e}")
            return False
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return False


def search_for_inno_setup_folder() -> Optional[str]:
    try:
        program_files_path = r"C:\Program Files (x86)"
        possible_folder_names = ["inno_setup", "innosetup", "inno_setup6", "innosetup6"]

        if not os.path.isdir(program_files_path):
            raise NotADirectoryError(f"{program_files_path} ist kein Verzeichnis.")

        for root, dirs, files in os.walk(program_files_path):
            # We only care about the files in the root directory (the program_files_path)
            if root == program_files_path:
                for dir_name in dirs:
                    if dir_name.lower().replace(" ", "") in possible_folder_names:
                        compiler_path = os.path.join(root, dir_name, "ISCC.exe")
                        if os.path.exists(compiler_path):
                            return compiler_path

            # Prevent os.walk from going deeper into subdirectories
            dirs[
                :
            ] = []  # Clear the dirs list so that os.walk doesn't descend into subfolders

        return None
    except NotADirectoryError as e:
        print(f"Fehler: {e}")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None


def get_files_and_folders(
    target_dir: str, ignore_extensions_list: Optional[str | tuple[str, ...]] = None
) -> list:
    """
    Function to get a list of files and folders in the needed format for the Inno Setup Compiler.

    :param target_dir: Target directory
    :param ignore_extensions_list: List of file extensions to ignore e.g. ('.exe', '.dll') or just '.exe'
    """
    try:
        if not os.path.isdir(target_dir):
            raise NotADirectoryError(target_dir)
        formated_files = []
        formated_folders = []
        dest_dir = "{app}"
        for root, dirs, files in os.walk(target_dir):
            # We only care about the files in the root directory (the target_dir)
            if root == target_dir:
                for file in files:
                    if ignore_extensions_list and file.endswith(ignore_extensions_list):
                        continue
                    file_path = os.path.join(root, file)
                    file_string = f'Source: "{file_path}"; DestDir: "{dest_dir}"; Flags: ignoreversion'
                    formated_files.append(file_string)

                for folder in dirs:
                    folder_path = os.path.join(root, folder)
                    folder_string = f'Source: "{folder_path}\\*"; DestDir: "{dest_dir}\\{folder}"; Flags: ignoreversion recursesubdirs createallsubdirs'
                    formated_folders.append(folder_string)

            # Prevent os.walk from going deeper into subdirectories
            dirs[
                :
            ] = []  # Clear the dirs list so that os.walk doesn't descend into subfolders
        return formated_files + formated_folders
    except Exception as e:
        raise Exception(e)


def build_spec():
    if os.path.exists(f"{config.application_name}.spec"):
        print(f"Removing: {f'{config.application_name}.spec'}")
        os.remove(f"{config.application_name}.spec")

    hidden_imports = [
        "pyttsx4.drivers",
        "pyttsx4.drivers.dummy",
        "pyttsx4.drivers.espeak",
        "pyttsx4.drivers.nsss",
        "pyttsx4.drivers.sapi5",
        "orienteering_startlist_screen.resources_rc",
    ]
    excludes = [
        "PyQt",
        "notebook",
        "torch",
        "tensorflow",
        "bokeh",
        "llvmlite",
        "babel",
        "pyarrow",
        "scipy",
        "pandas",
        "sphinx",
        "sklearn",
        "netCDF4",
        "jedi",
        "h5py",
        "ttk",
        "docutils",
        "tcl8",
        "sqlalchemy",
        "simplejson",
        "bcolz",
        "numcodecs",
        "numba",
        "zmq",
        "IPython",
        "cytoolz",
        "psutil",
        "fastparquet",
        "thrift",
        "bson",
        "snappy",
        "markupsafe",
        "tornado",
        "pygame",
        "tkinter",
        "tcl",
        "osgeo",
        "matplotlib",
    ]
    datas = [
        ("pyproject.toml", "."),
    ]

    icon_path = "src/orienteering_startlist_screen/resources/images/logo.png"

    command = [
        "pyi-makespec",
        # '--windowed',             # no terminal console
        "--contents-directory",
        ".",  # Use “.” to re-enable old one dir layout without contents directory
        f'--name "{config.application_name}"',
        f'--icon "{icon_path}"',
        "--paths=./src/orienteering_startlist_screen",
    ]
    # Trennzeichen je nach Betriebssystem für --add-data
    sep = ";" if os.name == "nt" else ":"

    for data in datas:
        command.append(f'--add-data "{data[0]}{sep}{data[1]}"')
    for hidden_import in hidden_imports:
        command.append(f"--hidden-import={hidden_import}")
    for exclude in excludes:
        command.append(f"--exclude={exclude}")

    command.append('"./src/orienteering_startlist_screen/main.py"')

    full_command = " ".join(command)
    print(full_command)

    result = subprocess.run(full_command, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def build_exe():
    spec_path = f"{config.application_name}.spec"
    if not os.path.exists(spec_path):
        print(f"{spec_path} wurde nicht gefunden!")
        print(f"Erstelle neue {spec_path} mit build_spec() ...")
        build_spec()

    for path in ["dist", "build"]:
        if os.path.exists(path):
            print(f"Removing: {path}")
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    command = [
        "pyinstaller",
        "--noconfirm",  # no confirmation when
        "--distpath ./dist",
        "--workpath ./build",
        "--clean",
        spec_path,
    ]

    full_command = " ".join(command)
    print(full_command)

    result = subprocess.run(full_command, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def build_installer():
    build_exe()

    installer_generator = InnoSetupScriptGenerator(
        app_name=config.application_name,
        app_version=config.application_version,
        app_icon_path=os.path.join(
            "src", "orienteering_startlist_screen", "resources", "images", "logo.ico"
        ),
        installer_exe_output_dir=os.path.dirname(os.path.abspath(__name__)),
        exe_name="Hello-World-Tool.exe",
        app_id_txt_path=os.path.join(
            os.path.dirname(os.path.abspath(__name__)), "app_id.txt"
        ),
        pyinstaller_gen_output_dir=os.path.join("dist", config.application_name),
        org_name=config.organization_name,
        org_url=config.organization_domain,
        need_admin_install=False,
    )
    installer_generator.generate_iss_file(os.path.dirname(os.path.abspath(__name__)))
    iss_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__name__)),
        f"{installer_generator.app_name}.iss",
    )
    result = compile_installer_exe(iss_file_path=iss_file_path)
    print(f"Compile result: {result}")
