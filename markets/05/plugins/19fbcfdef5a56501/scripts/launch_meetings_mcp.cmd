@echo off
setlocal DisableDelayedExpansion

if "%~1"=="" (
  echo ChatGPT Meetings could not start: missing MCP server path. 1>&2
  exit /b 64
)

set "CHATGPT_MEETINGS_MCP_SCRIPT=%~f1"
set "CHATGPT_MEETINGS_MCP_DUPLICATE_SCRIPT=1"

rem This batch process waits for Node and must not keep the plugin cache locked.
rem Capture the absolute MCP script first so its relative .mcp.json path survives.
if "%~d0"=="" (
  cd /d "%SystemRoot%"
) else (
  cd /d "%~d0\"
)
if errorlevel 1 (
  echo ChatGPT Meetings could not start: no safe Windows working directory. 1>&2
  exit /b 1
)

rem Parse the Node launch and dedicated-shell exit before an update moves this file.
rem Exiting the shell preserves the real Node status without delayed expansion.
if defined CHATGPT_MEETINGS_NODE_PATH if not exist "%CHATGPT_MEETINGS_NODE_PATH%" (
  echo ChatGPT Meetings could not start: CHATGPT_MEETINGS_NODE_PATH is not executable: %CHATGPT_MEETINGS_NODE_PATH% 1>&2
  exit /b 126
)
if defined CHATGPT_MEETINGS_NODE_PATH ("%CHATGPT_MEETINGS_NODE_PATH%" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)

rem WindowsApps can expose a Node path that exists but cannot be executed.
rem Prefer the relocated user-writable runtimes before probing packaged paths.
if defined LOCALAPPDATA for /d %%D in ("%LOCALAPPDATA%\OpenAI\Codex\runtimes\cua_node\*") do if exist "%%~fD\bin\node.exe" ("%%~fD\bin\node.exe" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)
if defined USERPROFILE if exist "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe" ("%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)

if defined CODEX_MCP_NODE_PATH if exist "%CODEX_MCP_NODE_PATH%" ("%CODEX_MCP_NODE_PATH%" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)
if defined CODEX_BROWSER_USE_NODE_PATH if exist "%CODEX_BROWSER_USE_NODE_PATH%" ("%CODEX_BROWSER_USE_NODE_PATH%" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)
if defined CODEX_ELECTRON_RESOURCES_PATH if exist "%CODEX_ELECTRON_RESOURCES_PATH%\cua_node\bin\node.exe" ("%CODEX_ELECTRON_RESOURCES_PATH%\cua_node\bin\node.exe" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)
if defined CODEX_CLI_PATH for %%I in ("%CODEX_CLI_PATH%") do if exist "%%~dpIcua_node\bin\node.exe" ("%%~dpIcua_node\bin\node.exe" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)
for /f "delims=" %%I in ('where codex 2^>nul') do if exist "%%~dpIcua_node\bin\node.exe" ("%%~dpIcua_node\bin\node.exe" "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)

where node >nul 2>&1
if not errorlevel 1 (node "%CHATGPT_MEETINGS_MCP_SCRIPT%" %* & exit)

echo ChatGPT Meetings could not find a Node runtime. Reinstall or update the ChatGPT app, or set CHATGPT_MEETINGS_NODE_PATH to an executable Node runtime. 1>&2
exit /b 127
