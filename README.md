# SVG to PDF Converter

Converts all `.svg` files found under the `input/` directory into `.pdf` files in `output/`.

## Dependencies

- Python `>= 3.13` (as defined in `pyproject.toml`)
- `uv` (used by `run.sh` and `run.bat` to install project dependencies)
- Python package dependencies:
	- `svglib>=2.0.0`
	- `reportlab` (imported by `main.py`; installed as part of dependency resolution)

## Project Structure

- `main.py`: conversion logic
- `input/`: place SVG files here
- `output/`: generated PDF files are written here
- `run.sh`: macOS/Linux helper script
- `run.bat`: Windows helper script

## How to Run

### macOS / Linux

From the project root:

```bash
bash run.sh
```

What this script does:

1. Creates `venv/` if needed and activates it.
2. Checks whether dependencies are installed.
3. If installed, runs `python main.py`.
4. If not installed, runs `uv sync --active`.

Note: On first run (when dependencies are missing), the script installs dependencies but does not execute conversion in the same run. Run `bash run.sh` a second time to start conversion.

### Windows

From the project root:

```bat
run.bat
```

Behavior is the same as `run.sh`: first run may install dependencies only, then run it again to convert files.

### Manual Execution (Alternative)

If you prefer manual commands:

```bash
python3 -m venv venv
source venv/bin/activate
uv sync --active
python main.py
```

On Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
uv sync --active
python main.py
```

## Input and Output

1. Put one or more `.svg` files in `input/` (subdirectories are also scanned).
2. Run the program.
3. Converted `.pdf` files are written to `output/`.

File names are preserved, with extension changed from `.svg` to `.pdf`.

## Important Behavior

- If `output/` already exists, the program exits without processing files.
- If no SVG files are found in `input/`, the program exits without processing files.

To run again, delete or rename the existing `output/` directory first.
