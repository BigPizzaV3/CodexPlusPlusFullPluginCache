[CmdletBinding()]
param(
    [switch]$ConfirmInstall,
    [string]$InstallRoot = (Join-Path $env:LOCALAPPDATA 'OpenAI\CacheStats'),
    [string]$ConfigPath = (Join-Path $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }) 'config.toml')
)

$ErrorActionPreference = 'Stop'
$productId = 'openai-cache-stats-local'
$version = '0.4.1'
$serverName = 'cache-stats-local'
$beginMarker = '# BEGIN CACHE STATS LOCAL - managed by openai-cache-stats-local'
$endMarker = '# END CACHE STATS LOCAL - managed by openai-cache-stats-local'

if (-not $ConfirmInstall) {
    throw 'Installation requires explicit confirmation. Re-run with -ConfirmInstall only after the user approves the disclosed local changes.'
}
if ($env:OS -ne 'Windows_NT') { throw 'Cache Stats 0.4.1 supports ChatGPT for Windows only.' }

$skillRoot = Split-Path -Parent $PSScriptRoot
$payloadRoot = Join-Path $skillRoot 'assets\runtime'
$hashFile = Join-Path $payloadRoot 'payload.sha256'
$required = @('server.ps1', 'ui\cache-card.html', 'LICENSE', 'payload.sha256')
foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $payloadRoot $relative) -PathType Leaf)) {
        throw "The reviewed runtime payload is incomplete: $relative is missing."
    }
}

foreach ($entry in (Get-Content -LiteralPath $hashFile | Where-Object { $_.Trim() })) {
    if ($entry -notmatch '^([A-Fa-f0-9]{64})\s+\*(.+)$') { throw "Invalid payload hash entry: $entry" }
    $expected = $matches[1].ToUpperInvariant()
    $relative = $matches[2].Replace('/', [IO.Path]::DirectorySeparatorChar)
    $candidate = Join-Path $payloadRoot $relative
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) { throw "A hashed payload file is missing: $relative" }
    if ((Get-FileHash -LiteralPath $candidate -Algorithm SHA256).Hash -ne $expected) {
        throw "Payload integrity check failed for $relative."
    }
}

$installRootFull = [IO.Path]::GetFullPath($InstallRoot)
$configPathFull = [IO.Path]::GetFullPath($ConfigPath)
$destination = Join-Path $installRootFull $version
$receiptPath = Join-Path $installRootFull 'install.json'
$existingReceipt = $null
if (Test-Path -LiteralPath $receiptPath -PathType Leaf) {
    $existingReceipt = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
    if ($existingReceipt.productId -ne $productId -or $existingReceipt.serverName -ne $serverName) {
        throw 'The existing install receipt is not owned by this Cache Stats package. Refusing to replace it.'
    }
}

$configText = if (Test-Path -LiteralPath $configPathFull -PathType Leaf) {
    [IO.File]::ReadAllText($configPathFull)
} else { '' }
$managedPattern = '(?ms)^' + [regex]::Escape($beginMarker) + '.*?^' + [regex]::Escape($endMarker) + '(?:\r?\n)?'
$hasManagedBlock = [regex]::IsMatch($configText, $managedPattern)
$hasNamedSection = $configText -match '(?m)^\s*\[mcp_servers\.cache-stats-local\]\s*$'
if ($hasNamedSection -and -not $hasManagedBlock) {
    throw "An MCP registration named $serverName already exists and is not owned by this installer. Refusing to replace it."
}
if ($hasManagedBlock -and -not $existingReceipt) {
    throw 'A managed Cache Stats configuration block exists without its install receipt. Refusing to guess ownership.'
}
if ($existingReceipt -and [IO.Path]::GetFullPath([string]$existingReceipt.configPath) -ne $configPathFull) {
    throw 'The existing install receipt belongs to a different ChatGPT/Codex configuration file.'
}

New-Item -ItemType Directory -Path (Join-Path $destination 'ui') -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $payloadRoot 'server.ps1') -Destination (Join-Path $destination 'server.ps1') -Force
Copy-Item -LiteralPath (Join-Path $payloadRoot 'ui\cache-card.html') -Destination (Join-Path $destination 'ui\cache-card.html') -Force
Copy-Item -LiteralPath (Join-Path $payloadRoot 'LICENSE') -Destination (Join-Path $destination 'LICENSE') -Force
Copy-Item -LiteralPath $hashFile -Destination (Join-Path $destination 'payload.sha256') -Force

$serverPath = Join-Path $destination 'server.ps1'
$serverPathJson = $serverPath | ConvertTo-Json -Compress
$block = @(
    $beginMarker,
    '[mcp_servers.cache-stats-local]',
    'command = "powershell.exe"',
    "args = [`"-NoLogo`", `"-NoProfile`", `"-ExecutionPolicy`", `"Bypass`", `"-File`", $serverPathJson]",
    'env_vars = ["CODEX_HOME", "CODEX_THREAD_ID", "USERPROFILE"]',
    'tool_timeout_sec = 30',
    'enabled = true',
    'default_tools_approval_mode = "auto"',
    $endMarker
) -join "`r`n"

$configWithoutManagedBlock = [regex]::Replace($configText, $managedPattern, '').TrimEnd("`r", "`n")
$newConfig = if ($configWithoutManagedBlock) { $configWithoutManagedBlock + "`r`n`r`n" + $block + "`r`n" } else { $block + "`r`n" }
$configDirectory = Split-Path -Parent $configPathFull
New-Item -ItemType Directory -Path $configDirectory -Force | Out-Null
$backupPath = $null
if (Test-Path -LiteralPath $configPathFull -PathType Leaf) {
    $backupPath = $configPathFull + '.cache-stats-backup-' + [DateTimeOffset]::UtcNow.ToString('yyyyMMddHHmmssfff')
    Copy-Item -LiteralPath $configPathFull -Destination $backupPath
}

$temporaryConfig = Join-Path $configDirectory ('.cache-stats-config-' + [Guid]::NewGuid().ToString('N') + '.tmp')
try {
    [IO.File]::WriteAllText($temporaryConfig, $newConfig, [Text.UTF8Encoding]::new($false))
    Move-Item -LiteralPath $temporaryConfig -Destination $configPathFull -Force
} finally {
    if (Test-Path -LiteralPath $temporaryConfig) { Remove-Item -LiteralPath $temporaryConfig -Force }
}

$receipt = [ordered]@{
    productId = $productId
    version = $version
    serverName = $serverName
    installRoot = $installRootFull
    serverPath = $serverPath
    configPath = $configPathFull
    configBackupPath = $backupPath
    installedAt = [DateTimeOffset]::UtcNow.ToString('o')
}
$receipt | ConvertTo-Json | Set-Content -LiteralPath $receiptPath -Encoding UTF8

Write-Output "Cache Stats $version was installed locally and registered as $serverName."
Write-Output 'Restart ChatGPT for Windows and open a new task before invoking Cache Stats.'
