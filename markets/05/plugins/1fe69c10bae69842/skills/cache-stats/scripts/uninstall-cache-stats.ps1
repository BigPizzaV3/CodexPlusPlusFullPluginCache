[CmdletBinding()]
param(
    [switch]$ConfirmUninstall,
    [string]$InstallRoot = (Join-Path $env:LOCALAPPDATA 'OpenAI\CacheStats'),
    [string]$ConfigPath = (Join-Path $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }) 'config.toml')
)

$ErrorActionPreference = 'Stop'
$productId = 'openai-cache-stats-local'
$expectedServerName = 'cache-stats-local'
$beginMarker = '# BEGIN CACHE STATS LOCAL - managed by openai-cache-stats-local'
$endMarker = '# END CACHE STATS LOCAL - managed by openai-cache-stats-local'

if (-not $ConfirmUninstall) {
    throw 'Uninstallation requires explicit confirmation. Re-run with -ConfirmUninstall only after the user approves removal.'
}

$installRootFull = [IO.Path]::GetFullPath($InstallRoot).TrimEnd('\')
$configPathFull = [IO.Path]::GetFullPath($ConfigPath)
$receiptPath = Join-Path $installRootFull 'install.json'
if (-not (Test-Path -LiteralPath $receiptPath -PathType Leaf)) {
    throw 'No Cache Stats install receipt was found. Refusing to remove an unverified directory or MCP registration.'
}

$receipt = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
if ($receipt.productId -ne $productId -or $receipt.serverName -ne $expectedServerName) {
    throw 'The install receipt is not owned by this Cache Stats package. Refusing to continue.'
}
if ([IO.Path]::GetFullPath([string]$receipt.installRoot).TrimEnd('\') -ne $installRootFull -or
    [IO.Path]::GetFullPath([string]$receipt.configPath) -ne $configPathFull) {
    throw 'The install receipt does not match the requested runtime or configuration path. Refusing to continue.'
}

$forbidden = @(
    [IO.Path]::GetPathRoot($installRootFull).TrimEnd('\'),
    [IO.Path]::GetFullPath($env:USERPROFILE).TrimEnd('\'),
    [IO.Path]::GetFullPath($env:LOCALAPPDATA).TrimEnd('\'),
    [IO.Path]::GetFullPath((Join-Path $env:USERPROFILE '.codex')).TrimEnd('\')
)
if ($forbidden -contains $installRootFull) { throw 'The resolved uninstall target is too broad. Refusing to remove it.' }

if (Test-Path -LiteralPath $configPathFull -PathType Leaf) {
    $configText = [IO.File]::ReadAllText($configPathFull)
    $managedPattern = '(?ms)^' + [regex]::Escape($beginMarker) + '.*?^' + [regex]::Escape($endMarker) + '(?:\r?\n)?'
    $hasManagedBlock = [regex]::IsMatch($configText, $managedPattern)
    $hasNamedSection = $configText -match '(?m)^\s*\[mcp_servers\.cache-stats-local\]\s*$'
    if ($hasNamedSection -and -not $hasManagedBlock) {
        throw 'The Cache Stats MCP section is no longer installer-managed. Refusing to remove it or the runtime.'
    }
    if ($hasManagedBlock) {
        $newConfig = [regex]::Replace($configText, $managedPattern, '').TrimEnd("`r", "`n")
        if ($newConfig) { $newConfig += "`r`n" }
        $backupPath = $configPathFull + '.cache-stats-uninstall-backup-' + [DateTimeOffset]::UtcNow.ToString('yyyyMMddHHmmssfff')
        Copy-Item -LiteralPath $configPathFull -Destination $backupPath
        $temporaryConfig = Join-Path (Split-Path -Parent $configPathFull) ('.cache-stats-config-' + [Guid]::NewGuid().ToString('N') + '.tmp')
        try {
            [IO.File]::WriteAllText($temporaryConfig, $newConfig, [Text.UTF8Encoding]::new($false))
            Move-Item -LiteralPath $temporaryConfig -Destination $configPathFull -Force
        } finally {
            if (Test-Path -LiteralPath $temporaryConfig) { Remove-Item -LiteralPath $temporaryConfig -Force }
        }
    }
}

Remove-Item -LiteralPath $installRootFull -Recurse -Force
Write-Output "Removed the local Cache Stats runtime and MCP registration $expectedServerName."
Write-Output 'The Cache Stats directory skill can now be removed separately from ChatGPT if desired.'
