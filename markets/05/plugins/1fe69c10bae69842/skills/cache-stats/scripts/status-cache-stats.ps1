[CmdletBinding()]
param(
    [string]$InstallRoot = (Join-Path $env:LOCALAPPDATA 'OpenAI\CacheStats'),
    [string]$ConfigPath = (Join-Path $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }) 'config.toml')
)

$ErrorActionPreference = 'Stop'
$receiptPath = Join-Path ([IO.Path]::GetFullPath($InstallRoot)) 'install.json'
$configPathFull = [IO.Path]::GetFullPath($ConfigPath)
$beginMarker = '# BEGIN CACHE STATS LOCAL - managed by openai-cache-stats-local'
$endMarker = '# END CACHE STATS LOCAL - managed by openai-cache-stats-local'
$configText = if (Test-Path -LiteralPath $configPathFull -PathType Leaf) { [IO.File]::ReadAllText($configPathFull) } else { '' }

$result = [ordered]@{
    platform = if ($env:OS -eq 'Windows_NT') { 'Windows' } else { 'Unsupported' }
    receiptPresent = Test-Path -LiteralPath $receiptPath -PathType Leaf
    runtimePresent = $false
    registrationPresent = ($configText.Contains($beginMarker) -and $configText.Contains($endMarker))
    version = $null
    serverName = 'cache-stats-local'
    configPath = $configPathFull
}
if ($result.receiptPresent) {
    $receipt = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
    $result.version = $receipt.version
    $result.serverName = $receipt.serverName
    $result.runtimePresent = Test-Path -LiteralPath $receipt.serverPath -PathType Leaf
}
$result | ConvertTo-Json
