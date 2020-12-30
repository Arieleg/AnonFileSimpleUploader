!include MUI2.nsh
!include FileFunc.nsh

;--------------------------------
;Perform Machine-level install, if possible

!define MULTIUSER_EXECUTIONLEVEL Highest
;Add support for command-line args that let uninstaller know whether to
;uninstall machine- or user installation:
!define MULTIUSER_INSTALLMODE_COMMANDLINE
!include MultiUser.nsh
!include LogicLib.nsh

Function .onInit
  !insertmacro MULTIUSER_INIT
  ;Do not use InstallDir at all so we can detect empty $InstDir!
  ${If} $InstDir == "" ; /D not used
      ${If} $MultiUser.InstallMode == "AllUsers"
          StrCpy $InstDir "$PROGRAMFILES\AnonFileSimpleUploader"
      ${Else}
          StrCpy $InstDir "$LOCALAPPDATA\AnonFileSimpleUploader"
      ${EndIf}
  ${EndIf}
FunctionEnd

Function un.onInit
  !insertmacro MULTIUSER_UNINIT
FunctionEnd

;--------------------------------
;General

  Name "AnonFileSimpleUploader"
  OutFile "..\AnonFileSimpleUploader-Setup.exe"
  !define MUI_ICON "..\..\src\main\icons\base\AnonFileSimpleUploader_installer.ico"
  !define MUI_UNICON "..\..\src\main\icons\base\AnonFileSimpleUploader_uninstaller.ico"
  BrandingText "https://github.com/arieleg"

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !define MUI_WELCOMEPAGE_TEXT "This wizard will guide you through the installation of AnonFileSimpleUploader.$\r$\n$\r$\n$\r$\nClick Next to continue."
  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
    !define MUI_FINISHPAGE_NOAUTOCLOSE
    !define MUI_FINISHPAGE_RUN
      !define MUI_FINISHPAGE_RUN_CHECKED
      !define MUI_FINISHPAGE_RUN_TEXT "Run AnonFileSimpleUploader"
      !define MUI_FINISHPAGE_RUN_FUNCTION "LaunchLink"
    !define MUI_FINISHPAGE_SHOWREADME
      !define MUI_FINISHPAGE_SHOWREADME_TEXT "Create Desktop Shortcut"
      !define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED
      !define MUI_FINISHPAGE_SHOWREADME_FUNCTION "CreateDesktopShortcut"
  !insertmacro MUI_PAGE_FINISH

  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages

  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

!define UNINST_KEY \
  "Software\Microsoft\Windows\CurrentVersion\Uninstall\AnonFileSimpleUploader"
Section
  SetOutPath "$InstDir"
  File /r "..\AnonFileSimpleUploader\*"
  WriteRegStr SHCTX "Software\AnonFileSimpleUploader" "" $InstDir
  WriteUninstaller "$InstDir\uninstall.exe"
  CreateShortCut "$SMPROGRAMS\AnonFileSimpleUploader.lnk" "$InstDir\AnonFileSimpleUploader.exe"
  WriteRegStr SHCTX "${UNINST_KEY}" "DisplayName" "AnonFileSimpleUploader"
  WriteRegStr SHCTX "${UNINST_KEY}" "UninstallString" \
    "$\"$InstDir\uninstall.exe$\" /$MultiUser.InstallMode"
  WriteRegStr SHCTX "${UNINST_KEY}" "QuietUninstallString" \
    "$\"$InstDir\uninstall.exe$\" /$MultiUser.InstallMode /S"
  WriteRegStr SHCTX "${UNINST_KEY}" "Publisher" "Arieleg"
  ${GetSize} "$InstDir" "/S=0K" $0 $1 $2
  IntFmt $0 "0x%08X" $0
  WriteRegDWORD SHCTX "${UNINST_KEY}" "EstimatedSize" "$0"

SectionEnd

;--------------------------------
;Uninstaller Section

Section "Uninstall"

  RMDir /r "$InstDir"
  RMDir /r "$PROFILE\AppData\Roaming\AnonFileSimpleUploader"
  Delete "$desktop\AnonFileSimpleUploader.lnk"
  Delete "$SMPROGRAMS\AnonFileSimpleUploader.lnk"
  DeleteRegKey /ifempty SHCTX "Software\AnonFileSimpleUploader"
  DeleteRegKey SHCTX "${UNINST_KEY}"

SectionEnd

Function LaunchLink
  !addplugindir "."
  ShellExecAsUser::ShellExecAsUser "open" "$SMPROGRAMS\AnonFileSimpleUploader.lnk"
FunctionEnd

Function CreateDesktopShortcut
  CreateShortcut "$desktop\AnonFileSimpleUploader.lnk" "$instdir\AnonFileSimpleUploader.exe"
FunctionEnd