@echo off
setlocal DisableDelayedExpansion
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUTF8=1
where py >nul 2>nul
if not errorlevel 1 goto use_py
where python >nul 2>nul
if not errorlevel 1 goto use_python
echo Python 3.10 or newer is needed for this OPTIONAL offline check.
echo This BAT does not install a ChatGPT plugin. Upload the original ZIP in ChatGPT.
pause
exit /b 1
:use_py
py -3 check_package.py --self-test
set RESULT=%ERRORLEVEL%
goto finish
:use_python
python check_package.py --self-test
set RESULT=%ERRORLEVEL%
:finish
echo.
echo This checked local files only. It did not install anything in ChatGPT.
echo After testing, please send back LogReport.zip.
pause
exit /b %RESULT%
