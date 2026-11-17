# Рендер макетов приложений (make_apps.py) в PNG 1080x1920.
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$outDir = "apps"

python "$root\make_apps.py"
if (-not $?) { exit 1 }

New-Item -ItemType Directory -Force "$root\$outDir" | Out-Null
foreach ($f in Get-ChildItem "$root\html_apps\*.html") {
    $out = Join-Path "$root\$outDir" ($f.BaseName + ".png")
    $url = "file:///" + ($f.FullName -replace '\\', '/')
    & $edge --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 `
        --window-size=1080,1920 --screenshot="$out" --user-data-dir="$env:TEMP\edgeshot" `
        --no-first-run --no-default-browser-check $url | Out-Null
}

New-Item -ItemType Directory -Force "$root\_preview" | Out-Null
$imgs = (Get-ChildItem "$root\$outDir\*.png" | ForEach-Object {
    '<img src="../' + $outDir + '/' + $_.Name + '">' }) -join ""
$html = '<!doctype html><meta charset="utf-8"><style>body{margin:0;background:#15151c;display:grid;' +
        'grid-template-columns:repeat(3,330px);gap:8px;padding:8px}img{width:330px;height:587px;display:block}' +
        '</style>' + $imgs
Set-Content -Encoding utf8 "$root\_preview\sheet_apps.html" $html
& $edge --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=6000 `
    --window-size=1030,1800 --screenshot="$root\_preview\sheet_apps.png" --user-data-dir="$env:TEMP\edgeshot2" `
    --no-first-run ("file:///" + ($root -replace '\\', '/') + "/_preview/sheet_apps.html") | Out-Null

Get-ChildItem "$root\$outDir\*.png" | Select-Object Name, Length
