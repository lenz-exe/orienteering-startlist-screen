import subprocess
import sys
import shutil
import os
import uuid
from typing import Optional

from src.orienteering_startlist_screen import config


class InnoSetupFileGenerator:
    def __init__(
            self,
            app_name: str,
            app_version: str,
            installer_output_dir: str,
            pyinstaller_exe_name: str,
            app_id_path: str,
            pyinstaller_output_dir: str,
            app_icon_path: Optional[str] = None,
            org_name: str = "Example Company",
            org_url: str = "https://www.example.com",
            license_path: Optional[str] = None,
            installer_name: Optional[str] = None,
            need_admin_install: bool = True,
    ):
        """
        Class to generate the .iss file for the Inno Setup Compiler.

        :param app_name: The name of the app/tool
        :param app_version: The version of the app/tool e.g: '1.0.0
        :param app_icon_path: The Path to the icon of the app/tool e.g: 'G:\\GIT\\toolname\\icons\\logo.ico'
        :param installer_output_dir: Path to the directory where the generated installer exe file get placed
        :param pyinstaller_exe_name: Name of the exe file which get created by the PyInstaller
        :param app_id_path: Path to the txt file which contains the app_id. If file not found a new gets created
        :param pyinstaller_output_dir: Path to the folder with the generated files/folders from PyInstaller
        :param org_name: The name of the organisation e.g.: 'Example Company'
        :param org_url: The url of the organisation e.g.: 'https://www.example.com'
        :param installer_name: Name of the installer e.g.: 'installer_toolname_1_0_0.exe'
        :param need_admin_install: Whether the installer should be installed as administrator or not
        """
        if app_icon_path and not os.path.isfile(app_icon_path):
            raise FileNotFoundError(app_icon_path)
        if not os.path.isdir(installer_output_dir):
            raise NotADirectoryError(installer_output_dir)
        if not os.path.isdir(pyinstaller_output_dir):
            raise NotADirectoryError(pyinstaller_output_dir)
        if license_path and not os.path.isfile(license_path):
            raise FileNotFoundError(license_path)

        self.app_name = app_name
        self.app_version = app_version
        self.pyinstaller_exe_name = pyinstaller_exe_name
        self.app_id = get_app_id(app_id_path=app_id_path, app_name=app_name)
        self.pyinstaller_output_dir = pyinstaller_output_dir
        self.installer_output_dir = installer_output_dir
        self.app_icon_path = app_icon_path
        self.org_name = org_name
        self.org_url = org_url
        self.license_path = license_path
        if not installer_name:
            self.installer_name = normalize_installer_name(app_name=app_name, app_version=app_version)
        else:
            self.installer_name = installer_name
        self.need_admin_install = need_admin_install

    def create_iss_file(self, iss_output_dir: str):
        """
        Create the .iss file for the Inno Setup Compiler.
        :param iss_output_dir: Path to the directory where the generated iss get placed
        """
        if not os.path.isdir(iss_output_dir):
            raise NotADirectoryError(iss_output_dir)

        files = get_folders_and_files(target_dir=self.pyinstaller_output_dir)
        files_str = "\n".join([f"{file}" for file in files])

        content = rf"""[Setup]
AppId={'{{' + self.app_id + '}'}
AppName={self.app_name}
AppVersion={self.app_version}
AppPublisher={self.org_name}
AppPublisherURL={self.org_url}
AppSupportURL={self.org_url}
AppUpdatesURL={self.org_url}
DefaultDirName={{autopf}}\{self.app_name}
UninstallDisplayIcon={{app}}\{self.pyinstaller_exe_name}
DisableProgramGroupPage=yes
{f'LicenseFile={self.license_path}' if self.license_path else ''}
{'' if self.need_admin_install else 'PrivilegesRequired=lowest'}
PrivilegesRequiredOverridesAllowed=dialog
OutputDir={self.installer_output_dir}
OutputBaseFilename={self.installer_name}
{f'SetupIconFile={self.app_icon_path}' if self.app_icon_path else ''}
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked

[Files]
{files_str}

[Icons]
Name: "{{autoprograms}}\{self.app_name}"; Filename: "{{app}}\{self.pyinstaller_exe_name}"
Name: "{{autodesktop}}\{self.app_name}"; Filename: "{{app}}\{self.pyinstaller_exe_name}"; Tasks: desktopicon

[Run]
; Start the app after the installation (optional)
Filename: "{{app}}\{self.pyinstaller_exe_name}"; Description: "{{cm:LaunchProgram,{self.app_name}}}"; Flags: nowait postinstall skipifsilent
"""
        with open(os.path.join(iss_output_dir, f"{self.app_name}.iss"), 'w') as file:
            file.write(content)


def get_app_id(app_id_path: str, app_name: str) -> str:
    """
    Get app id from app_id path if exists, else generate an app id with the app name as namespace dns and uuid version5
    :param app_id_path: string of the path to app id txt file or where it should be saved
    :param app_name: string of the app name
    """
    if not os.path.isfile(app_id_path):
        app_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, app_name))
        with open(app_id_path, "w") as file:
            file.write(app_id)
    with open(app_id_path, "r") as file:
        app_id = file.read()
    return app_id


def normalize_installer_name(app_name: str, app_version: str) -> str:
    """
    When no installer name is provided, the installer name gets generated out of the app_name and the app_version.
    :param app_name: string of the app name
    :param app_version: string of the app version
    """
    tmp_name = app_name.lower().replace(" ", "_")
    tmp_version = app_version.replace(".", "_")
    installer_name = f"installer_{tmp_name}_{tmp_version}"
    return installer_name


def get_folders_and_files(target_dir: str, ignore_extensions_list: Optional[str | tuple[str, ...]] = None) -> list:
    """
    Function to get a list of files and folders in the needed format for the Inno Setup Compiler.

    :param target_dir: Target directory
    :param ignore_extensions_list: List of file extensions to ignore e.g. ('.exe', '.dll') or just '.exe'
    """
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
                    "The Inno Setup Compiler could not be found. "
                    "Please provide the path to the ISCC.exe: "
                )
                if not os.path.exists(compiler_path):
                    print("The given path is does not exists. Exit script.")
                    return False

        command = [compiler_path, iss_file_path]

        try:
            subprocess.run(command, check=True)
            print("Compiling successful!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error while compiling: {e}")
            return False
    except Exception as e:
        print(f"An unexpected error: {e}")
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

    icon_path = "src/orienteering_startlist_screen/resources/images/logo.ico"

    command = [
        "pyi-makespec",
        '--windowed',             # no terminal console
        "--contents-directory",
        ".",  # Use “.” to re-enable old one dir layout without contents directory
        f'--name "{config.application_name}"',
        f'--icon "{icon_path}"',
        "--paths=./src/orienteering_startlist_screen",
    ]
    # separate mark depending on os for --add-data
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
        print(f"{spec_path} could not be found!")
        print(f"Create new {spec_path} with build_spec() ...")
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

    installer_generator = InnoSetupFileGenerator(
        app_name=config.application_name,
        app_version=config.application_version,
        app_icon_path=os.path.join(
            "src", "orienteering_startlist_screen", "resources", "images", "logo.ico"
        ),
        installer_output_dir=os.path.dirname(os.path.abspath(__name__)),
        pyinstaller_exe_name="Orienteering-Startlist-Screen.exe",
        app_id_path=os.path.join(
            os.path.dirname(os.path.abspath(__name__)), "app_id.txt"
        ),
        pyinstaller_output_dir=os.path.join("dist", config.application_name),
        org_name=config.organization_name,
        org_url=config.organization_domain,
        license_path=os.path.join(os.path.dirname(os.path.abspath(__name__)), "LICENSE"),
        need_admin_install=True,
    )
    installer_generator.create_iss_file(os.path.dirname(os.path.abspath(__name__)))
    iss_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__name__)),
        f"{installer_generator.app_name}.iss",
    )
    result = compile_installer_exe(iss_file_path=iss_file_path)
    print(f"Compile result: {result}")
