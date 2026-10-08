$ErrorActionPreference = 'Stop'

# MCP stdio is UTF-8. Windows PowerShell otherwise uses the active console code
# page for redirected output, which can turn valid JSON containing non-ASCII
# text into an invalid byte stream that the client waits on until timeout.
$utf8NoBom = New-Object Text.UTF8Encoding($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom

$script:Version = '0.4.1'
$script:CardUri = 'ui://widget/cache-stats.html'
$script:RuntimeRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$script:CardPath = Join-Path $script:RuntimeRoot 'ui\cache-card.html'
$script:InvocationMaxAgeMs = 15 * 60 * 1000
$script:SessionTailBytes = 128 * 1024
$script:SessionHeadBytes = 64 * 1024
$script:UsageTailBytes = 8 * 1024 * 1024

function Read-SharedText {
    param([Parameter(Mandatory = $true)][string]$Path)

    $share = [IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete
    $stream = New-Object IO.FileStream($Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, $share)
    try {
        $reader = New-Object IO.StreamReader($stream, [Text.Encoding]::UTF8, $true)
        try { return $reader.ReadToEnd() } finally { $reader.Dispose() }
    } finally {
        $stream.Dispose()
    }
}

function Read-SharedTail {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [int]$MaximumBytes = $script:SessionTailBytes
    )

    $share = [IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete
    $stream = New-Object IO.FileStream($Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, $share)
    try {
        $length = [Math]::Min($stream.Length, $MaximumBytes)
        $start = [Math]::Max(0, $stream.Length - $length)
        [void]$stream.Seek($start, [IO.SeekOrigin]::Begin)
        $buffer = New-Object byte[] $length
        $read = $stream.Read($buffer, 0, $length)
        $text = [Text.Encoding]::UTF8.GetString($buffer, 0, $read)
        if ($start -gt 0) {
            $lineBreak = $text.IndexOf("`n")
            if ($lineBreak -ge 0) { $text = $text.Substring($lineBreak + 1) } else { $text = '' }
        }
        return $text
    } finally {
        $stream.Dispose()
    }
}

function Read-SharedHead {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [int]$MaximumBytes = $script:SessionHeadBytes
    )

    $share = [IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete
    $stream = New-Object IO.FileStream($Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, $share)
    try {
        $length = [Math]::Min($stream.Length, $MaximumBytes)
        $buffer = New-Object byte[] $length
        $read = $stream.Read($buffer, 0, $length)
        return [Text.Encoding]::UTF8.GetString($buffer, 0, $read)
    } finally {
        $stream.Dispose()
    }
}

function Convert-LineToRecord {
    param([string]$Line)
    if ([string]::IsNullOrWhiteSpace($Line)) { return $null }
    try { return $Line | ConvertFrom-Json } catch { return $null }
}

function Get-ResponseMessageText {
    param([object]$Message)
    if ($null -eq $Message) { return '' }

    $parts = @()
    foreach ($item in @($Message.content)) {
        if ($null -eq $item) { continue }
        foreach ($propertyName in @('text', 'input_text')) {
            $property = $item.PSObject.Properties[$propertyName]
            if ($null -ne $property -and -not [string]::IsNullOrWhiteSpace([string]$property.Value)) {
                $parts += [string]$property.Value
                break
            }
        }
    }
    return $parts -join "`n"
}

function Test-CacheStatsInvocation {
    param([object]$Message)
    $text = [string]$Message
    return (
        $text -match 'plugin://cache-stats(?:@[a-z0-9._-]+)?' -or
        $text -match '\[\$cache-stats:cache-stats\]\(' -or
        $text -match '\[@cache-stats\]' -or
        $text -match '(?:^|\s)@cache-stats(?:\s|$)'
    )
}

function Get-ActiveInvocation {
    param(
        [Parameter(Mandatory = $true)][string]$SessionText,
        [DateTimeOffset]$Now = [DateTimeOffset]::UtcNow
    )

    $activeTurnId = $null
    $invocationMessage = $null
    $latestTimestamp = $null

    foreach ($line in ($SessionText -split "`r?`n")) {
        $record = Convert-LineToRecord $line
        if ($null -eq $record) { continue }

        if ($record.timestamp) {
            try {
                $timestamp = [DateTimeOffset]::Parse([string]$record.timestamp)
                if ($null -eq $latestTimestamp -or $timestamp -gt $latestTimestamp) {
                    $latestTimestamp = $timestamp
                }
            } catch { }
        }

        $payload = $record.payload
        if ($record.type -eq 'event_msg' -and $payload.type -eq 'task_started') {
            $activeTurnId = [string]$payload.turn_id
            $invocationMessage = $null
            continue
        }

        if (-not $activeTurnId) { continue }

        if ($record.type -eq 'response_item' -and $payload.type -eq 'message' -and $payload.role -eq 'user') {
            $messageTurnId = [string]$payload.internal_chat_message_metadata_passthrough.turn_id
            if ($messageTurnId -and $messageTurnId -ne $activeTurnId) { continue }
            $messageText = Get-ResponseMessageText $payload
            if (Test-CacheStatsInvocation $messageText) {
                $invocationMessage = $messageText
            }
            continue
        }

        if ($record.type -eq 'event_msg' -and $payload.type -eq 'user_message' -and (Test-CacheStatsInvocation $payload.message)) {
            $invocationMessage = [string]$payload.message
            continue
        }

        if (($payload.type -eq 'task_complete' -or $payload.type -eq 'turn_aborted') -and
            (-not $payload.turn_id -or [string]$payload.turn_id -eq $activeTurnId)) {
            $activeTurnId = $null
            $invocationMessage = $null
        }
    }

    if (-not $activeTurnId -or -not $invocationMessage -or $null -eq $latestTimestamp) { return $null }
    $ageMs = ($Now - $latestTimestamp).TotalMilliseconds
    if ($ageMs -lt -60000 -or $ageMs -gt $script:InvocationMaxAgeMs) { return $null }

    return [pscustomobject]@{
        turnId = $activeTurnId
        invocationMessage = $invocationMessage
        latestTimestamp = $latestTimestamp.ToString('o')
    }
}

function Get-SessionFiles {
    $codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
    $sessionsRoot = Join-Path $codexHome 'sessions'
    if (-not (Test-Path -LiteralPath $sessionsRoot -PathType Container)) {
        throw "No ChatGPT/Codex session transcripts were found under $sessionsRoot."
    }

    $files = @([IO.Directory]::EnumerateFiles($sessionsRoot, '*.jsonl', [IO.SearchOption]::AllDirectories))
    if ($files.Count -eq 0) {
        throw "No ChatGPT/Codex session transcripts were found under $sessionsRoot."
    }
    return $files
}

function Find-CurrentSessionPath {
    $files = @(Get-SessionFiles)
    $threadId = [string]$env:CODEX_THREAD_ID
    if (-not [string]::IsNullOrWhiteSpace($threadId)) {
        $matches = @($files | Where-Object { [IO.Path]::GetFileName($_).EndsWith("$threadId.jsonl") })
        if ($matches.Count -eq 0) { throw "No session transcript matched the current task $threadId." }
        if ($matches.Count -gt 1) { throw "Multiple session transcripts matched the current task $threadId; refusing to guess." }
        return $matches[0]
    }

    $active = @()
    foreach ($file in $files) {
        $tail = Read-SharedTail -Path $file
        if ($null -ne (Get-ActiveInvocation -SessionText $tail)) { $active += $file }
    }

    if ($active.Count -eq 0) {
        throw "No active @cache-stats invocation could be identified. Refusing to use another task's usage."
    }
    if ($active.Count -gt 1) {
        throw 'Multiple active @cache-stats invocations were found. Refusing to guess which task requested usage.'
    }
    return $active[0]
}

function Get-TokenValue {
    param([object]$Usage, [string[]]$Names)
    foreach ($name in $Names) {
        $property = $Usage.PSObject.Properties[$name]
        if ($null -ne $property -and $null -ne $property.Value) {
            $number = 0L
            if ([long]::TryParse([string]$property.Value, [ref]$number) -and $number -gt 0) { return $number }
        }
    }
    return 0L
}

function Get-SessionId {
    param([string]$SessionText)
    foreach ($line in ($SessionText -split "`r?`n")) {
        $record = Convert-LineToRecord $line
        if ($null -ne $record -and $record.type -eq 'session_meta' -and $record.payload.id) {
            return [string]$record.payload.id
        }
    }
    return $null
}

function Get-CompletedTurns {
    param([string]$SessionText)
    $completed = New-Object System.Collections.ArrayList
    $active = $null

    foreach ($line in ($SessionText -split "`r?`n")) {
        $record = Convert-LineToRecord $line
        if ($null -eq $record) { continue }
        $payload = $record.payload

        if ($record.type -eq 'event_msg' -and $payload.type -eq 'task_started') {
            $active = [pscustomobject]@{
                turnId = [string]$payload.turn_id
                model = $null
                reasoningEffort = $null
                inputTokens = 0L
                cachedInputTokens = 0L
                cacheWriteInputTokens = 0L
                outputTokens = 0L
                reasoningOutputTokens = 0L
                modelCalls = 0
                completedAt = $null
            }
            continue
        }

        if ($null -eq $active) { continue }

        if ($record.type -eq 'turn_context' -and [string]$payload.turn_id -eq $active.turnId -and $payload.model) {
            $active.model = [string]$payload.model
            if ($payload.effort) {
                $active.reasoningEffort = [string]$payload.effort
            } elseif ($payload.collaboration_mode -and $payload.collaboration_mode.settings -and
                      $payload.collaboration_mode.settings.reasoning_effort) {
                $active.reasoningEffort = [string]$payload.collaboration_mode.settings.reasoning_effort
            }
            continue
        }

        if ($record.type -eq 'event_msg' -and $payload.type -eq 'token_count') {
            $usage = $payload.info.last_token_usage
            if ($null -eq $usage) { continue }
            $inputTokens = Get-TokenValue $usage @('input_tokens')
            $cachedTokens = Get-TokenValue $usage @('cached_input_tokens', 'cache_read_input_tokens')
            $cacheWriteTokens = Get-TokenValue $usage @('cache_write_input_tokens', 'cache_write_tokens')
            $outputTokens = Get-TokenValue $usage @('output_tokens')
            $reasoningTokens = Get-TokenValue $usage @('reasoning_output_tokens')
            if ($inputTokens -gt 0 -or $outputTokens -gt 0) {
                $active.inputTokens += $inputTokens
                $active.cachedInputTokens += $cachedTokens
                $active.cacheWriteInputTokens += $cacheWriteTokens
                $active.outputTokens += $outputTokens
                $active.reasoningOutputTokens += $reasoningTokens
                $active.modelCalls += 1
            }
            continue
        }

        if ($record.type -eq 'event_msg' -and $payload.type -eq 'task_complete' -and
            [string]$payload.turn_id -eq $active.turnId) {
            $active.completedAt = if ($record.timestamp) { [string]$record.timestamp } else { $null }
            [void]$completed.Add($active)
            $active = $null
        }
    }
    return @($completed)
}

function Get-PreviousCacheStats {
    $sessionPath = Find-CurrentSessionPath
    $sessionHead = Read-SharedHead -Path $sessionPath
    $sessionText = Read-SharedTail -Path $sessionPath -MaximumBytes $script:UsageTailBytes
    $sessionId = Get-SessionId -SessionText $sessionHead
    if (-not $sessionId) { throw 'The selected transcript has no session identity; refusing to report usage.' }

    $threadId = [string]$env:CODEX_THREAD_ID
    if (-not [string]::IsNullOrWhiteSpace($threadId) -and $sessionId -ne $threadId) {
        throw "Session identity mismatch: expected $threadId, found $sessionId. Refusing to report another task's usage."
    }
    if ([string]::IsNullOrWhiteSpace($threadId) -and $null -eq (Get-ActiveInvocation -SessionText $sessionText)) {
        throw 'The selected transcript no longer contains the active @cache-stats invocation; refusing to report usage.'
    }

    $turns = @(Get-CompletedTurns -SessionText $sessionText | Where-Object { $_.modelCalls -gt 0 -and $_.inputTokens -gt 0 })
    if ($turns.Count -eq 0) { throw 'No previous completed response with token usage was found in this task.' }
    $turn = $turns[$turns.Count - 1]
    $cached = [Math]::Min($turn.cachedInputTokens, $turn.inputTokens)
    $fresh = [Math]::Max(0, $turn.inputTokens - $cached)
    $percent = [Math]::Round(($cached * 100.0) / $turn.inputTokens, 1)

    return [ordered]@{
        cacheHit = $cached -gt 0
        cachePercent = $percent
        inputTokens = [long]$turn.inputTokens
        cachedInputTokens = [long]$cached
        cacheWriteInputTokens = [long]$turn.cacheWriteInputTokens
        freshInputTokens = [long]$fresh
        outputTokens = [long]$turn.outputTokens
        reasoningOutputTokens = [long]$turn.reasoningOutputTokens
        modelCalls = [int]$turn.modelCalls
        model = if ($turn.model) { [string]$turn.model } else { 'Unknown model' }
        reasoningEffort = if ($turn.reasoningEffort) { [string]$turn.reasoningEffort } else { $null }
        taskId = $sessionId
        turnId = [string]$turn.turnId
        completedAt = $turn.completedAt
        error = $null
    }
}

function Format-Fallback {
    param([System.Collections.IDictionary]$Stats)
    $heading = if ($Stats.cacheHit) { '### Prompt cache hit' } else { '### No cached input' }
    $reasoning = if ($Stats.reasoningEffort) { " | $($Stats.reasoningEffort) reasoning" } else { '' }
    return @(
        $heading,
        '',
        "**$($Stats.cachePercent.ToString('0.0'))%** of input tokens were reused.",
        '',
        '| Token type | Count |',
        '| --- | ---: |',
        "| Cached input | **$($Stats.cachedInputTokens.ToString('N0'))** |",
        "| Cache-write input | **$($Stats.cacheWriteInputTokens.ToString('N0'))** |",
        "| Non-cached input (includes cache writes) | **$($Stats.freshInputTokens.ToString('N0'))** |",
        "| Newly generated output | **$($Stats.outputTokens.ToString('N0'))** |",
        '',
        "``$($Stats.model)``$reasoning | $($Stats.modelCalls) model call(s) | verified current task",
        '',
        '> Cache-write input is included in non-cached input; do not add it again. Reuse percentage measures tokens, not cost savings. Output tokens are always newly generated.'
    ) -join "`n"
}

function Get-ToolDefinition {
    return [ordered]@{
        name = 'show_cache_stats'
        title = 'Show cache stats'
        description = "Show exact prompt-cache usage for the immediately preceding completed response in the current local ChatGPT/Codex task. Task identity is verified and the tool refuses to read another task."
        inputSchema = [ordered]@{ type = 'object'; properties = [ordered]@{}; additionalProperties = $false }
        outputSchema = [ordered]@{
            type = 'object'
            properties = [ordered]@{
                cacheHit = @{ type = 'boolean' }
                cachePercent = @{ type = 'number'; minimum = 0; maximum = 100; description = 'Percentage of input tokens reused, not percentage cost savings.' }
                inputTokens = @{ type = 'integer'; minimum = 0 }
                cachedInputTokens = @{ type = 'integer'; minimum = 0 }
                cacheWriteInputTokens = @{ type = 'integer'; minimum = 0; description = 'Input written to cache when reported by the host. Included in freshInputTokens.' }
                freshInputTokens = @{ type = 'integer'; minimum = 0; description = 'All non-cached input, including cache writes. Equal to inputTokens minus cachedInputTokens.' }
                outputTokens = @{ type = 'integer'; minimum = 0 }
                reasoningOutputTokens = @{ type = 'integer'; minimum = 0 }
                modelCalls = @{ type = 'integer'; minimum = 0 }
                model = @{ type = 'string' }
                reasoningEffort = @{ type = @('string', 'null') }
                taskId = @{ type = 'string' }
                turnId = @{ type = 'string' }
                completedAt = @{ type = @('string', 'null') }
                error = @{ type = @('string', 'null') }
            }
            required = @('cacheHit', 'cachePercent', 'inputTokens', 'cachedInputTokens', 'cacheWriteInputTokens', 'freshInputTokens', 'outputTokens', 'reasoningOutputTokens', 'modelCalls', 'model', 'taskId', 'turnId')
            additionalProperties = $false
        }
        annotations = [ordered]@{ readOnlyHint = $true; openWorldHint = $false; destructiveHint = $false }
        _meta = [ordered]@{
            'ui/resourceUri' = $script:CardUri
            'openai/outputTemplate' = $script:CardUri
            'openai/toolInvocation/invoking' = 'Reading cache usage...'
            'openai/toolInvocation/invoked' = 'Cache usage ready'
        }
    }
}

function Get-ResourceDefinition {
    return [ordered]@{
        uri = $script:CardUri
        name = 'cache-stats-card'
        title = 'Cache Stats prompt-cache card'
        description = 'Visual cache usage for the previous verified response.'
        mimeType = 'text/html;profile=mcp-app'
    }
}

function New-RpcError {
    param($Id, [int]$Code, [string]$Message)
    return [ordered]@{ jsonrpc = '2.0'; id = $Id; error = [ordered]@{ code = $Code; message = $Message } }
}

function Invoke-RpcRequest {
    param([object]$Request)
    $id = $Request.id
    $method = [string]$Request.method

    switch ($method) {
        'initialize' {
            return [ordered]@{
                jsonrpc = '2.0'
                id = $id
                result = [ordered]@{
                    protocolVersion = '2025-06-18'
                    capabilities = [ordered]@{
                        tools = [ordered]@{ listChanged = $false }
                        resources = [ordered]@{ subscribe = $false; listChanged = $false }
                    }
                    serverInfo = [ordered]@{ name = 'cache-stats'; version = $script:Version }
                    instructions = 'Use show_cache_stats when the user asks whether the previous response used cached input tokens.'
                }
            }
        }
        'ping' { return [ordered]@{ jsonrpc = '2.0'; id = $id; result = [ordered]@{} } }
        'tools/list' {
            return [ordered]@{ jsonrpc = '2.0'; id = $id; result = [ordered]@{ tools = @((Get-ToolDefinition)) } }
        }
        'resources/list' {
            return [ordered]@{ jsonrpc = '2.0'; id = $id; result = [ordered]@{ resources = @((Get-ResourceDefinition)) } }
        }
        'resources/templates/list' {
            return [ordered]@{ jsonrpc = '2.0'; id = $id; result = [ordered]@{ resourceTemplates = @() } }
        }
        'resources/read' {
            if ([string]$Request.params.uri -ne $script:CardUri) { return New-RpcError $id -32002 'Resource not found.' }
            $html = Read-SharedText -Path $script:CardPath
            $content = [ordered]@{
                uri = $script:CardUri
                mimeType = 'text/html;profile=mcp-app'
                text = $html
                _meta = [ordered]@{
                    ui = [ordered]@{ prefersBorder = $true }
                    'openai/widgetDescription' = 'An inline card showing verified current-task cache usage, model, and reasoning effort.'
                }
            }
            return [ordered]@{ jsonrpc = '2.0'; id = $id; result = [ordered]@{ contents = @($content) } }
        }
        'tools/call' {
            if ([string]$Request.params.name -ne 'show_cache_stats') { return New-RpcError $id -32602 'Unknown tool.' }
            try {
                $stats = Get-PreviousCacheStats
                $result = [ordered]@{
                    structuredContent = $stats
                    content = @([ordered]@{ type = 'text'; text = (Format-Fallback $stats) })
                    isError = $false
                }
            } catch {
                $message = $_.Exception.Message
                $empty = [ordered]@{
                    cacheHit = $false; cachePercent = 0; inputTokens = 0; cachedInputTokens = 0; cacheWriteInputTokens = 0
                    freshInputTokens = 0; outputTokens = 0; reasoningOutputTokens = 0; modelCalls = 0
                    model = 'Unavailable'; reasoningEffort = $null; taskId = ''; turnId = ''
                    completedAt = $null; error = $message
                }
                $result = [ordered]@{
                    structuredContent = $empty
                    content = @([ordered]@{ type = 'text'; text = "Cache Stats could not read usage: $message" })
                    isError = $true
                }
            }
            return [ordered]@{ jsonrpc = '2.0'; id = $id; result = $result }
        }
        default {
            if ($method.StartsWith('notifications/')) { return $null }
            return New-RpcError $id -32601 "Method not found: $method"
        }
    }
}

while ($null -ne ($line = [Console]::In.ReadLine())) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    if ($line.Length -gt 0 -and $line[0] -eq [char]0xFEFF) { $line = $line.Substring(1) }
    try {
        $request = $line | ConvertFrom-Json
        $response = Invoke-RpcRequest $request
        if ($null -ne $response) {
            [Console]::Out.WriteLine(($response | ConvertTo-Json -Depth 30 -Compress))
            [Console]::Out.Flush()
        }
    } catch {
        $response = New-RpcError $null -32700 $_.Exception.Message
        [Console]::Out.WriteLine(($response | ConvertTo-Json -Depth 10 -Compress))
        [Console]::Out.Flush()
    }
}
