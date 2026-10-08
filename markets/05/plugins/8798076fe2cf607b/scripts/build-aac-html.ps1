[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$InputJson,

    [Parameter(Mandatory = $true)]
    [string]$OutputHtml
)

$ErrorActionPreference = 'Stop'

function Require-Text($Value, [string]$FieldName) {
    if ($null -eq $Value -or [string]::IsNullOrWhiteSpace([string]$Value)) {
        throw "Required field is empty: $FieldName"
    }
    return [string]$Value
}

function Get-ImageMimeType([string]$Path) {
    switch ([System.IO.Path]::GetExtension($Path).ToLowerInvariant()) {
        '.png'  { return 'image/png' }
        '.jpg'  { return 'image/jpeg' }
        '.jpeg' { return 'image/jpeg' }
        '.gif'  { return 'image/gif' }
        '.webp' { return 'image/webp' }
        '.svg'  { return 'image/svg+xml' }
        default { throw "Unsupported image extension: $Path" }
    }
}

try {
    $inputPath = (Resolve-Path -LiteralPath $InputJson).Path
    $outputPath = if ([System.IO.Path]::IsPathRooted($OutputHtml)) {
        [System.IO.Path]::GetFullPath($OutputHtml)
    }
    else {
        [System.IO.Path]::GetFullPath((Join-Path (Get-Location).Path $OutputHtml))
    }

    if (Test-Path -LiteralPath $outputPath) {
        throw "Output already exists: $outputPath"
    }

    $outputDirectory = [System.IO.Path]::GetDirectoryName($outputPath)
    if (-not (Test-Path -LiteralPath $outputDirectory -PathType Container)) {
        throw "Output directory does not exist: $outputDirectory"
    }

    $templatePath = Join-Path $PSScriptRoot '..\assets\aac-editor-template.html'
    if (-not (Test-Path -LiteralPath $templatePath -PathType Leaf)) {
        throw "HTML template does not exist: $templatePath"
    }

    $input = Get-Content -Raw -Encoding UTF8 -LiteralPath $inputPath | ConvertFrom-Json
    $title = Require-Text $input.title 'title'
    $profileAlias = Require-Text $input.profile_alias 'profile_alias'
    $cardsPerPage = [int]$input.cards_per_page
    if ($cardsPerPage -notin @(1, 2, 4, 8)) {
        throw 'cards_per_page must be one of: 1, 2, 4, 8'
    }
    if ($null -eq $input.cards -or @($input.cards).Count -eq 0) {
        throw 'cards must contain at least one card'
    }

    $inputDirectory = [System.IO.Path]::GetDirectoryName($inputPath)
    $seenIds = @{}
    $embeddedCards = foreach ($card in @($input.cards)) {
        $id = Require-Text $card.id 'cards[].id'
        $label = Require-Text $card.label 'cards[].label'
        $relativeImagePath = Require-Text $card.image_path 'cards[].image_path'
        if ($seenIds.ContainsKey($id)) {
            throw "Duplicate card id: $id"
        }
        $seenIds[$id] = $true

        $imagePath = if ([System.IO.Path]::IsPathRooted($relativeImagePath)) {
            [System.IO.Path]::GetFullPath($relativeImagePath)
        }
        else {
            [System.IO.Path]::GetFullPath((Join-Path $inputDirectory $relativeImagePath))
        }
        if (-not (Test-Path -LiteralPath $imagePath -PathType Leaf)) {
            throw "Image file does not exist for card '$id': $imagePath"
        }

        $mime = Get-ImageMimeType $imagePath
        $base64 = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($imagePath))
        [ordered]@{
            id = $id
            label = $label
            image_data = "data:$mime;base64,$base64"
            imageTransform = [ordered]@{ scale = 1; x = 0; y = 0 }
        }
    }

    $state = [ordered]@{
        title = $title
        profile_alias = $profileAlias
        cards_per_page = $cardsPerPage
        fontSize = 32
        fontFamily = 'Noto Sans KR, Arial, sans-serif'
        cards = @($embeddedCards)
    }
    $json = $state | ConvertTo-Json -Depth 8 -Compress
    $json = $json.Replace('&', '\u0026').Replace('<', '\u003c').Replace('>', '\u003e')

    $template = Get-Content -Raw -Encoding UTF8 -LiteralPath $templatePath
    $token = '__AAC_DATA__'
    if (($template.Split(@($token), [System.StringSplitOptions]::None).Count - 1) -ne 1) {
        throw "HTML template must contain exactly one $token token"
    }
    $html = $template.Replace($token, $json)
    [System.IO.File]::WriteAllText($outputPath, $html, [System.Text.UTF8Encoding]::new($false))
    Write-Output $outputPath
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
