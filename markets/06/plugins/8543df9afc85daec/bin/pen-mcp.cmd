@echo off
rem Starts the server binary built for this CPU.
if /i "%PROCESSOR_ARCHITECTURE%"=="ARM64" (
  "%~dp0pen-mcp-windows-arm64.exe" %*
) else (
  "%~dp0pen-mcp-windows-x64.exe" %*
)
exit /b %errorlevel%
