[Setup]
AppId={{394bbb78-2714-58f6-a36f-3f7a5893e91f}
AppName=Orienteering-Startlist-Screen
AppVersion=0.1.0
AppPublisher=lenz-exe
AppPublisherURL=https://www.example.com
AppSupportURL=https://www.example.com
AppUpdatesURL=https://www.example.com
DefaultDirName={autopf}\Orienteering-Startlist-Screen
UninstallDisplayIcon={app}\Orienteering-Startlist-Screen.exe
DisableProgramGroupPage=yes
LicenseFile=C:\Users\XYZ-User\Documents\Projects\orienteering-startlist-screen\LICENSE

PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\XYZ-User\Documents\Projects\orienteering-startlist-screen
OutputBaseFilename=installer_orienteering-startlist-screen_0_1_0
SetupIconFile=src\orienteering_startlist_screen\resources\images\logo.ico
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\libcrypto-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\libffi-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\libssl-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\Orienteering-Startlist-Screen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\pyproject.toml"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\python313.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\VCRUNTIME140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_uuid.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_wmi.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\_zoneinfo.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Orienteering-Startlist-Screen\click-8.3.0.dist-info\*"; DestDir: "{app}\click-8.3.0.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\faker\*"; DestDir: "{app}\faker"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\flask-3.1.2.dist-info\*"; DestDir: "{app}\flask-3.1.2.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\itsdangerous-2.2.0.dist-info\*"; DestDir: "{app}\itsdangerous-2.2.0.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\lxml\*"; DestDir: "{app}\lxml"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\PIL\*"; DestDir: "{app}\PIL"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\pycountry\*"; DestDir: "{app}\pycountry"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\pycountry-24.6.1.dist-info\*"; DestDir: "{app}\pycountry-24.6.1.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\PySide6\*"; DestDir: "{app}\PySide6"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\qt_material\*"; DestDir: "{app}\qt_material"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\setuptools\*"; DestDir: "{app}\setuptools"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\shiboken6\*"; DestDir: "{app}\shiboken6"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\tzdata\*"; DestDir: "{app}\tzdata"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\werkzeug-3.1.3.dist-info\*"; DestDir: "{app}\werkzeug-3.1.3.dist-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "dist\Orienteering-Startlist-Screen\xmlschema\*"; DestDir: "{app}\xmlschema"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Orienteering-Startlist-Screen"; Filename: "{app}\Orienteering-Startlist-Screen.exe"
Name: "{autodesktop}\Orienteering-Startlist-Screen"; Filename: "{app}\Orienteering-Startlist-Screen.exe"; Tasks: desktopicon

[Run]
; Start the app after the installation (optional)
Filename: "{app}\Orienteering-Startlist-Screen.exe"; Description: "{cm:LaunchProgram,Orienteering-Startlist-Screen}"; Flags: nowait postinstall skipifsilent
