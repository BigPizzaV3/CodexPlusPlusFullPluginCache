@echo off
setlocal EnableExtensions DisableDelayedExpansion
set /p "version=" < "%~dp0cirro-release.txt"
for /f "usebackq skip=1 delims=" %%H in ("%~dp0cirro-release.txt") do set "manifest_hash=%%H"
set "arch=%PROCESSOR_ARCHITECTURE%"
if defined PROCESSOR_ARCHITEW6432 set "arch=%PROCESSOR_ARCHITEW6432%"
if /i "%arch%"=="AMD64" set "arch=x64"
if /i "%arch%"=="ARM64" set "arch=arm64"
if not "%arch%"=="x64" if not "%arch%"=="arm64" (
  echo Unsupported Cirro architecture: %arch% 1>&2
  exit /b 1
)
set "name=cirro-windows-%arch%"
if not defined DEMO_VIDEOS_CACHE set "DEMO_VIDEOS_CACHE=%CD%\.demo-videos-cache"
set "cache=%DEMO_VIDEOS_CACHE%\%version%"
if not exist "%cache%\" mkdir "%cache%" || exit /b 1
set "work=%cache%\run-%RANDOM%-%RANDOM%"
mkdir "%work%" || exit /b 1
set "url=https://persistent.oaistatic.com/cirro/%version%"
call :verify SHA256SUMS "%manifest_hash%" || goto :fail
set "expected="
set "matches=0"
for /f "tokens=1,2" %%A in ('^""%SystemRoot%\System32\findstr.exe" /l /c:"  %name%.zip" "%cache%\SHA256SUMS"^"') do if "%%B"=="%name%.zip" (
  set "expected=%%A"
  set /a matches+=1 >nul
)
if not "%matches%"=="1" (
  echo Missing or duplicate Cirro checksum: %name%.zip 1>&2
  goto :fail
)
call :verify "%name%.zip" "%expected%" || goto :fail
"%SystemRoot%\System32\tar.exe" -xf "%cache%\%name%.zip" -C "%work%"
if errorlevel 1 goto :fail
"%work%\%name%\cirro.exe" %*
set "code=%errorlevel%"
rmdir /s /q "%work%"
exit /b %code%

:fail
rmdir /s /q "%work%"
exit /b 1

:verify
set "file=%~1"
if exist "%cache%\%file%" goto :hash
"%SystemRoot%\System32\curl.exe" --fail --silent --show-error --location --connect-timeout 15 --max-time 300 --speed-limit 1024 --speed-time 30 --proto "=https" --proto-redir "=https" "%url%/%file%" -o "%work%\%file%"
if errorlevel 1 exit /b 1
move /y "%work%\%file%" "%cache%\%file%" >nul || exit /b 1
:hash
set "CIRRO_CHECK_FILE=%cache%\%file%"
set "actual="
rem Use .NET directly: a pwsh caller can pass incompatible PowerShell 7 modules.
for /f "delims=" %%H in ('^""%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -Command "$ErrorActionPreference='Stop'; $s=[IO.File]::OpenRead($env:CIRRO_CHECK_FILE); try { $h=[Security.Cryptography.SHA256]::Create(); try { [BitConverter]::ToString($h.ComputeHash($s)).Replace('-','') } finally { $h.Dispose() } } finally { $s.Dispose() }"^"') do set "actual=%%H"
if not defined actual (
  echo Cirro could not compute SHA-256: %cache%\%file%. Check the error above. 1>&2
  exit /b 1
)
if /i not "%actual%"=="%~2" (
  echo Cirro checksum mismatch: %cache%\%file%. Remove that file and retry. 1>&2
  exit /b 1
)
exit /b 0
