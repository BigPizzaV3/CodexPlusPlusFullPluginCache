param([Parameter(ValueFromRemainingArguments=$true)][string[]]$CliArgs)
$ErrorActionPreference = 'Stop'
$TaskRoot = Split-Path -Parent $PSScriptRoot
$TaskNode = $null
$TaskCandidate = Get-Command node -ErrorAction SilentlyContinue
if ($env:WANDEO_FORCE_PORTABLE_NODE -ne '1' -and $TaskCandidate) {
  # Windows PowerShell 5.1 strips embedded quotes from native command
  # arguments. Avoid a quoted JavaScript string so a valid system Node is not
  # mistaken for an old runtime and sent through the portable bootstrap.
  & $TaskCandidate.Source -e 'process.exit(parseInt(process.versions.node,10) >= 22 ? 0 : 1)'
  if ($LASTEXITCODE -eq 0) { $TaskNode = $TaskCandidate.Source }
}
if (-not $TaskNode) {
  if ($env:PROCESSOR_ARCHITECTURE -ne 'AMD64') { throw 'Wandeo supports Windows x64.' }
  $TaskCache = if ($env:WANDEO_CACHE_DIR) { $env:WANDEO_CACHE_DIR } else { Join-Path $env:LOCALAPPDATA 'Wandeo\Cache' }
  $TaskDirectory = Join-Path $TaskCache 'node\node-v24.21.0-win-x64'
  $TaskNode = Join-Path $TaskDirectory 'node.exe'
  if (-not (Test-Path $TaskNode)) {
    $TaskTemp = Join-Path $TaskCache ('node\bootstrap-' + [guid]::NewGuid().ToString())
    New-Item -ItemType Directory -Force $TaskTemp | Out-Null
    try {
      [Console]::Error.WriteLine('[wandeo] Preparing pinned portable Node.js')
      $TaskArchive = Join-Path $TaskTemp 'node.zip'
      Invoke-WebRequest -UseBasicParsing -Uri 'https://nodejs.org/dist/v24.21.0/node-v24.21.0-win-x64.zip' -OutFile $TaskArchive
      $TaskSha256 = [BitConverter]::ToString(([Security.Cryptography.SHA256]::Create()).ComputeHash([IO.File]::ReadAllBytes($TaskArchive))).Replace('-', '').ToLowerInvariant()
      if ($TaskSha256 -ne '158f7685b44de51f6c0df1d153526cbcd3e1bc739a8dfc607721cef75de9e541') { throw 'Portable Node checksum mismatch.' }
      Expand-Archive -LiteralPath $TaskArchive -DestinationPath $TaskTemp
      if (-not (Test-Path $TaskDirectory)) { Move-Item (Join-Path $TaskTemp 'node-v24.21.0-win-x64') $TaskDirectory }
    } finally { Remove-Item -Recurse -Force $TaskTemp -ErrorAction SilentlyContinue }
  }
}
& $TaskNode (Join-Path $TaskRoot 'dist\cli.mjs') @CliArgs
exit $LASTEXITCODE
