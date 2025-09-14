#!/bin/bash

echo "=========================================="
echo "Email Variations Generator - Build Script"
echo "=========================================="
echo

# Check if uv is installed
echo "Checking for uv package manager..."
if ! command -v uv &>/dev/null; then
    echo "[ERROR] uv is not installed or not in PATH"
    echo "Please install uv first: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi
echo "[OK] uv found"

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "[ERROR] main.py not found"
    echo "Please run this script from the project root directory"
    exit 1
fi
echo "[OK] main.py found"

# Clean previous builds
echo
echo "Cleaning previous build artifacts..."
rm -rf dist build *.spec
echo "Previous builds cleaned"

# Create build directories
mkdir -p dist
mkdir -p build

# Run PyInstaller to create executable
echo
echo "Creating standalone executable..."
uv run pyinstaller \
    --onefile \
    --windowed \
    --name "EmailVariationsGenerator" \
    --distpath "dist" \
    --workpath "build" \
    --specpath "build" \
    main.py

if [ $? -eq 0 ]; then
    echo
    echo "[SUCCESS] Build completed successfully!"

    if [ -f "dist/EmailVariationsGenerator" ]; then
        # Make executable
        chmod +x dist/EmailVariationsGenerator

        # Get file size
        size=$(stat -f%z "dist/EmailVariationsGenerator" 2>/dev/null || stat -c%s "dist/EmailVariationsGenerator" 2>/dev/null)
        size_mb=$((size / 1024 / 1024))

        echo "[INFO] Executable: dist/EmailVariationsGenerator"
        echo "[INFO] File size: ${size_mb}MB"
        echo
        echo "The executable is ready for distribution."
        echo "No Python installation required on target machines."
    else
        echo "[WARNING] Executable not found in expected location"
    fi
else
    echo
    echo "[ERROR] Build failed! Check the error messages above."
    exit 1
fi
