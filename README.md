# scanner_app/README.md
# Scanner App

A simple Python-based scanner application supporting HP Deskjet 2130.

## Installation

This project uses `uv` package manager. To set up:

1. Install `uv` if not already: `pip install uv`
2. Create virtual environment: `uv venv`
3. Activate: `source .venv/bin/activate` (on Unix) or `.venv\Scripts\activate` (on Windows)
4. Install dependencies: `uv pip install -r requirements.txt`
5. Install the package: `uv pip install -e .`

## Usage

Run the application: `python -m scanner_app`

## Features

- Configure and check printer status
- Set export path and filename
- Scan documents
- View scanned images in session
- Reset session
- Export to PDF