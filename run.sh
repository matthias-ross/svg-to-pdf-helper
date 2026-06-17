#!/bin/bash
set -e

cd "$(dirname "$0")"

if [ -f "venv/bin/activate" ]; then
	source venv/bin/activate
else
	echo "Creating virtual environment..."
	python3 -m venv venv
	source venv/bin/activate
fi

if python -c "import svglib, reportlab" >/dev/null 2>&1; then
    python main.py
else
	echo "Installing dependencies..."
	uv sync --active
fi



