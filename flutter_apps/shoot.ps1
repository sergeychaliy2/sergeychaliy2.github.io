param(
    [string]$Out = "..\apps_flutter",   # куда класть PNG
    [int]$Port = 8077
)

# Собирает веб-версию макетов и снимает все экраны в PNG 1080x1920.
$proj = Split-Path -Parent $MyInvocation.MyCommand.Path
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$outDir = Join-Path $proj $Out

Push-Location $proj
flutter build web --release --no-tree-shake-icons --no-wasm-dry-run
$code = $LASTEXITCODE
Pop-Location
if ($code -ne 0) {
    Write-Host "Сборка не удалась. Если путь к проекту длиннее 260 символов — соберите из короткого пути."
    exit 1
}

New-Item -ItemType Directory -Force $outDir | Out-Null
$srv = Start-Process -FilePath "python" `
    -ArgumentList "-m", "http.server", "$Port", "--directory", "$proj\build\web" `
    -WindowStyle Hidden -PassThru
Start-Sleep -Milliseconds 1500

$map = [ordered]@{
    flowers = "Flower_Shop"; gas = "Gas_Utility"; taxi = "Taxi_Ride"; bank = "Mobile_Bank";
    weather = "Weather_Today"; fitness = "Fitness_Tracker"; food = "Food_Delivery"; home = "Smart_Home"
}
foreach ($k in $map.Keys) {
    & $edge --headless=new --hide-scrollbars --force-device-scale-factor=1 `
        --window-size=1080,1920 --virtual-time-budget=20000 `
        --screenshot="$outDir\$($map[$k]).png" --user-data-dir="$env:TEMP\edgefl" `
        --no-first-run "http://localhost:$Port/#/$k" 2>$null | Out-Null
}

Stop-Process -Id $srv.Id -Force
Get-ChildItem "$outDir\*.png" | Select-Object Name, Length
