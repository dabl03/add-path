@ECHO OFF
set DIR_BASE=%~dp0
set OUT="%DIR_BASE%out.tmp"

addPath.py %* --OUT %OUT%

if EXIST "%OUT%" (
  set out_path=
  set /p out_path=<%OUT%
  echo "%out_path%"
  IF "%out_path%"=="" (goto del)
  set PATH=%PATH%;%out_path%
  :del
  DEL %OUT% /Q
)
@ECHO ON