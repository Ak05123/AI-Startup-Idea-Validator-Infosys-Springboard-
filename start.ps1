# ============================================================
# AI Startup Validator — One-Click Startup (Streamlit only)
# ============================================================
# The validation pipeline runs directly inside Streamlit
# (no FastAPI / uvicorn / port 8000 required).
# ============================================================

$ErrorActionPreference = "Stop"

$ProjectRoot = $PSScriptRoot
$FrontendUrl = "http://localhost:8501"

# Local dependency cache used when the default pip location is unavailable.
# Optional — ignored if it does not exist.
$LocalPackages = "D:\Downloads\AiStartupValidator\site-packages"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   AI STARTUP VALIDATOR" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting Streamlit frontend..." -ForegroundColor Yellow

if (Test-Path $LocalPackages) {
    $env:PYTHONPATH = "$LocalPackages;$env:PYTHONPATH"
}

$frontendProcess = Start-Process -FilePath "python" `
    -ArgumentList "-m", "streamlit", "run", "frontend/streamlit_app.py", "--server.port", "8501", "--server.headless", "true" `
    -WorkingDirectory $ProjectRoot `
    -PassThru `
    -WindowStyle Hidden

# Wait for the frontend to be ready
$frontendReady = $false
for ($i = 0; $i -lt 60; $i++) {
    Start-Sleep -Seconds 1
    try {
        $health = Invoke-WebRequest -Uri "$FrontendUrl/_stcore/health" -TimeoutSec 2 -UseBasicParsing
        if ($health.Content -match "ok") {
            $frontendReady = $true
            break
        }
    } catch {
        # Not ready yet — keep waiting
    }
}

if (-not $frontendReady) {
    Write-Host "ERROR: Streamlit frontend did not become ready on $FrontendUrl" -ForegroundColor Red
    if (-not $frontendProcess.HasExited) {
        Stop-Process -Id $frontendProcess.Id -Force
    }
    exit 1
}

Write-Host "Streamlit frontend is ready at $FrontendUrl" -ForegroundColor Green

# Open the app in the browser
Start-Process $FrontendUrl

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host "   AI STARTUP VALIDATOR IS RUNNING" -ForegroundColor Cyan
Write-Host "   Frontend: $FrontendUrl" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C in this terminal to stop the app." -ForegroundColor DarkGray
Write-Host ""

# Keep the script alive so the user can stop the app with Ctrl+C
try {
    while ($true) {
        Start-Sleep -Seconds 1
        if ($frontendProcess.HasExited) {
            break
        }
    }
} finally {
    if (-not $frontendProcess.HasExited) {
        Stop-Process -Id $frontendProcess.Id -Force
    }
}
