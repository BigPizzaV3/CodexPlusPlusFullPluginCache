[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][ValidateSet('install','start','stop','status','uninstall')][string]$Action,
    [Parameter(Mandatory=$true)][ValidateSet('public','private')][string]$Edition,
    [Parameter(Mandatory=$true)][string]$InstallRoot
)
$ErrorActionPreference = 'Stop'
$editionLabel = if ($Edition -eq 'private') { 'Private' } else { 'Public' }
$serviceName = "BetterContext $editionLabel Wake"
$expectedRoot = [IO.Path]::GetFullPath((Join-Path $env:USERPROFILE ".bettercontext\$Edition\wake"))
if ([IO.Path]::GetFullPath($InstallRoot) -ne $expectedRoot) { throw 'Unexpected service installation directory.' }
$existing = Get-ScheduledTask -TaskName $serviceName -ErrorAction SilentlyContinue
if ($Action -eq 'stop' -or $Action -eq 'uninstall' -or $Action -eq 'install') {
    if ($existing -and $existing.State -eq 'Running') {
        Stop-ScheduledTask -TaskName $serviceName
        $deadline = [DateTime]::UtcNow.AddSeconds(10)
        while ((Get-ScheduledTask -TaskName $serviceName).State -eq 'Running') {
            if ([DateTime]::UtcNow -ge $deadline) { throw 'Wake helper did not stop within ten seconds.' }
            Start-Sleep -Milliseconds 200
        }
    }
}
if ($Action -eq 'uninstall' -and $existing) {
    Unregister-ScheduledTask -TaskName $serviceName -Confirm:$false
}
if ($Action -eq 'install') {
    $config = Get-Content -LiteralPath (Join-Path $InstallRoot 'service.json') -Raw | ConvertFrom-Json
    $pythonWindowless = Join-Path (Split-Path -Parent $config.python) 'pythonw.exe'
    if (-not (Test-Path -LiteralPath $pythonWindowless -PathType Leaf)) { throw 'pythonw.exe is required for a hidden Windows wake helper.' }
    $dispatcher = Join-Path $InstallRoot 'wake_dispatcher.py'
    $hostConfig = Join-Path $InstallRoot 'wake-dispatcher.json'
    $taskAction = New-ScheduledTaskAction -Execute $pythonWindowless -Argument "`"$dispatcher`" --config `"$hostConfig`"" -WorkingDirectory $InstallRoot
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent().Name
    $trigger = New-ScheduledTaskTrigger -AtLogOn -User $identity
    $trigger.Delay = 'PT20S'
    $principal = New-ScheduledTaskPrincipal -UserId $identity -LogonType Interactive -RunLevel Limited
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
    Register-ScheduledTask -TaskName $serviceName -Action $taskAction -Trigger $trigger -Principal $principal -Settings $settings -Description 'Deliver BetterContext relays to configured local tasks.' -Force | Out-Null
}
if ($Action -eq 'install' -or $Action -eq 'start') {
    Start-ScheduledTask -TaskName $serviceName
    Start-Sleep -Seconds 2
    if ((Get-ScheduledTask -TaskName $serviceName).State -ne 'Running') { throw 'Wake helper exited. Check the edition WakeDispatcher/wake.log.' }
}
$current = Get-ScheduledTask -TaskName $serviceName -ErrorAction SilentlyContinue
@{ installed = [bool]$current; running = [bool]($current -and $current.State -eq 'Running'); service = $serviceName } | ConvertTo-Json -Compress
