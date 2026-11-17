param(
    [string]$Only = "*",   # маска для контрольного листа, напр. -Only "0[7-9]*"
    [switch]$NoBar         # рендер без строки состояния телефона -> screens_nobar
)

# Собирает HTML-макеты и рендерит их в PNG 1080x1920 через headless Edge.
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if ($NoBar) { $env:NO_STATUSBAR = "1"; $outDir = "screens_nobar" }
else        { $env:NO_STATUSBAR = "0"; $outDir = "screens" }

python "$root\make_screens.py"
if (-not $?) { exit 1 }
python "$root\make_screens2.py"
if (-not $?) { exit 1 }

New-Item -ItemType Directory -Force "$root\$outDir" | Out-Null
foreach ($f in Get-ChildItem "$root\html\*.html") {
    $out = Join-Path "$root\$outDir" ($f.BaseName + ".png")
    $url = "file:///" + ($f.FullName -replace '\\', '/')
    & $edge --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 `
        --window-size=1080,1920 --screenshot="$out" --user-data-dir="$env:TEMP\edgeshot" `
        --no-first-run --no-default-browser-check $url | Out-Null
}

# контрольный лист для быстрого просмотра
New-Item -ItemType Directory -Force "$root\_preview" | Out-Null
$imgs = (Get-ChildItem "$root\$outDir\$Only.png" | ForEach-Object {
    '<img src="../' + $outDir + '/' + $_.Name + '">' }) -join ""
$html = '<!doctype html><meta charset="utf-8"><style>body{margin:0;background:#15151c;display:grid;' +
        'grid-template-columns:repeat(3,330px);gap:8px;padding:8px}img{width:330px;height:587px;display:block}' +
        '</style>' + $imgs
Set-Content -Encoding utf8 "$root\_preview\sheet.html" $html
& $edge --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=6000 `
    --window-size=1030,2410 --screenshot="$root\_preview\sheet.png" --user-data-dir="$env:TEMP\edgeshot2" `
    --no-first-run ("file:///" + ($root -replace '\\', '/') + "/_preview/sheet.html") | Out-Null

Get-ChildItem "$root\$outDir\$Only.png" | Select-Object Name, Length
