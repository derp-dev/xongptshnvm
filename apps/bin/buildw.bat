@echo off

REM Check number of arguments
if "%1"=="" goto usage
if "%2" neq "" goto usage

REM Check argument is single lowercase letter
for /f "delims=a-z" %%i in ("%1") do goto invalid

REM Set paths
set MSYS_DIR=/D:/
set MSYS_EXE=%MSYS_DIR%\msys2.exe

REM Check file exists
if exist "%1func.c" (
  REM Compile file using msys2.exe
  "%MSYS_EXE%" gcc -Wall -Wextra -o "%1func.out" "%1func.c" -v 2>nul
) else (
  REM Create file
  echo.>"%1func.c" 
  REM Open in editor
  start "" "%1func.c"
)

goto end

:usage
echo Usage: script.bat ^<letter^>
goto end

:invalid 
echo Invalid argument, must be a single lowercase letter

:end
