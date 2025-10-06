[Setup]
AppId={{394bbb78-2714-58f6-a36f-3f7a5893e91f}}
AppName=Orienteering-Startlist-Screen
AppVersion=0.1.0
AppPublisher=lenz-exe
AppPublisherURL=https://www.example.com
AppSupportURL=https://www.example.com
AppUpdatesURL=https://www.example.com
DefaultDirName={autopf}\Orienteering-Startlist-Screen
UninstallDisplayIcon={app}\Orienteering-Startlist-Screen.exe
DisableProgramGroupPage=yes
LicenseFile=.\LICENSE

PrivilegesRequiredOverridesAllowed=dialog
OutputDir=.
OutputBaseFilename=installer_orienteering-startlist-screen_0_1_0
SetupIconFile=src\orienteering_startlist_screen\resources\images\logo.ico
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\Orienteering-Startlist-Screen\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{autoprograms}\Orienteering-Startlist-Screen"; Filename: "{app}\Orienteering-Startlist-Screen.exe"
Name: "{autodesktop}\Orienteering-Startlist-Screen"; Filename: "{app}\Orienteering-Startlist-Screen.exe"; Tasks: desktopicon

[Run]
; Start the app after the installation (optional)
Filename: "{app}\Orienteering-Startlist-Screen.exe"; Description: "{cm:LaunchProgram,Orienteering-Startlist-Screen}"; Flags: nowait postinstall skipifsilent
