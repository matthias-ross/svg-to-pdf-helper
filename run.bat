@echo off
setlocal

cd /d "%~dp0" || exit /b 1

if exist "venv\Scripts\activate.bat" (
	call "venv\Scripts\activate.bat" || exit /b 1
) else (
	echo Creating virtual environment...
	python -m venv venv || exit /b 1
	call "venv\Scripts\activate.bat" || exit /b 1
)

python -c "import svglib, reportlab" >nul 2>&1
if %errorlevel%==0 (
    python main.py
) else (
	echo Installing dependencies...
	uv sync --active || exit /b 1
)


