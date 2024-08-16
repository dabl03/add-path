@ECHO OFF

set "DIR_BASE=%~dp0"
set "OUT=%DIR_BASE%out.tmp.bat"

addPath.py %* --OUT "%OUT%"

if EXIST "%OUT%" (
  call "%OUT%"
  DEL "%OUT%" /Q
)
set DIR_BASE=
set OUT=

:: Para test:
:END 
@ECHO ON