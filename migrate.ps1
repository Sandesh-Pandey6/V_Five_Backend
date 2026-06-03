# One-click database setup for V Five
# Run in PowerShell:  .\migrate.ps1

Set-Location $PSScriptRoot

Write-Host "Installing dependencies..." -ForegroundColor Cyan
.\.venv\Scripts\pip install -r requirements.txt -q

Write-Host "Running migrations..." -ForegroundColor Cyan
.\.venv\Scripts\alembic upgrade head
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Seeding default content..." -ForegroundColor Cyan
.\.venv\Scripts\python scripts\seed_cms.py

Write-Host "Seeding admin users..." -ForegroundColor Cyan
.\.venv\Scripts\python scripts\seed_admin_users.py

Write-Host "Verifying connection..." -ForegroundColor Cyan
.\.venv\Scripts\python scripts\test_db.py

Write-Host "`nDone! Start the API with:" -ForegroundColor Green
Write-Host "  .\.venv\Scripts\uvicorn app.main:app --reload --port 8000" -ForegroundColor Yellow
