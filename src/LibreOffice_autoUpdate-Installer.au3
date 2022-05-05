#RequireAdmin
#include <File.au3>
#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
$spath = "http://downloads:downloads@dimitric.de/downloads/LibreOffice_autoUpdate/LibreOffice_autoUpdate.exe"
$prname = "LibreOffice_autoUpdate"
$ProgramPath = @ProgramFilesDir & "\" & $prname & ""
$Verknuepfung = True
$gui1 = GUICreate($prname, 358, 87, 582, 347)
$Text1 = GUICtrlCreateLabel("Möchtest du " & $prname & " installieren?", 8, 8, 237, 17)
$Verknuepfung_box = GUICtrlCreateCheckbox("Desktopverknüpfung erstellen", 16, 48, 193, 17)
GUICtrlSetState(-1, $GUI_UNCHECKED)
$Ja = GUICtrlCreateButton("Ja", 272, 8, 75, 25)
$Nein = GUICtrlCreateButton("Nein", 272, 48, 75, 25)
GUISetState(@SW_SHOW)
While 1
   $nMsg = GUIGetMsg()
   Switch $nMsg
	  Case $GUI_EVENT_CLOSE
		 Exit

	  Case $Nein
		 Exit

	  Case $Ja
		 GUIDelete($gui1)
		 ExitLoop

	  Case $Verknuepfung_box
		 If _IsChecked($Verknuepfung_box) Then
			$Verknuepfung = True
		 Else
			$Verknuepfung = False
		 EndIf

   EndSwitch
WEnd

$gui2 = GUICreate($prname, 250, 87, 582, 347)
$Text2 = GUICtrlCreateLabel("" & $prname & " wird installiert...", 8, 8, 193, 17)
GUISetState(@SW_SHOW)
$nMsg = GUIGetMsg()
Switch $nMsg
   Case $GUI_EVENT_CLOSE
EndSwitch

DirCreate($ProgramPath)
;~ FileCopy($spath, $ProgramPath & "\" & $prname & ".exe", 1)
InetGet($spath, $ProgramPath & "\" & $prname & ".exe")

FileCreateShortcut($ProgramPath & "\" & $prname & ".exe", @ProgramsDir & "\" & $prname & ".lnk")

If $Verknuepfung Then
   FileCreateShortcut($ProgramPath & "\" & $prname & ".exe", @DesktopDir & "\" & $prname & ".lnk")
EndIf

GUIDelete($gui2)
$gui3 = GUICreate($prname, 277, 87, 582, 347)
$Text3 = GUICtrlCreateLabel("" & $prname & " wurde erfolgreich installiert.", 8, 8, 249, 17)
$Beenden = GUICtrlCreateButton("Beenden", 16, 40, 75, 25)
GUISetState(@SW_SHOW)
While 1
   $nMsg = GUIGetMsg()
   Switch $nMsg
	  Case $GUI_EVENT_CLOSE
		 Exit
	  Case $Beenden
		 Exit
	EndSwitch
WEnd

Func _IsChecked($idControlID)
    Return BitAND(GUICtrlRead($idControlID), $GUI_CHECKED) = $GUI_CHECKED
 EndFunc
