@echo off
title Email Variations Generator - Build Script
echo ==========================================
echo Email Variations Generator - Build Script
echo ==========================================
echo.

REM Check if uv is installed
echo Checking for uv package manager...
uv --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] uv is not installed or not in PATH
    echo Please install uv first: https://docs.astral.sh/uv/getting-started/installation/
    echo.
    pause
    exit /b 1
)
echo [OK] uv found

REM Check if main.py exists
if not exist "main.py" (
    echo [ERROR] main.py not found
    echo Please run this script from the project root directory
    echo.
    pause
    exit /b 1
)
echo [OK] main.py found

REM Clean previous builds
echo.
echo Cleaning previous build artifacts...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
del /q *.spec 2>nul

REM Sync dependencies with uv
echo.
echo Syncing dependencies with uv...
uv sync
if %errorlevel% neq 0 (
    echo [ERROR] Failed to sync dependencies
    echo.
    pause
    exit /b 1
)
echo [OK] Dependencies synced

REM Create build directories
mkdir dist 2>nul
mkdir build 2>nul

REM Run PyInstaller to create executable using uv dependency management
echo.
echo Creating standalone executable with uv dependency management...
uv run pyinstaller ^
    --onefile ^
    --windowed ^
    --name "EmailVariationsGenerator" ^
    --distpath "dist" ^
    --workpath "build" ^
    --specpath "build" ^
    --hidden-import "PyQt6.QtCore" ^
    --hidden-import "PyQt6.QtWidgets" ^
    --hidden-import "PyQt6.QtGui" ^
    main.py

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Build completed successfully!
    if exist "dist\EmailVariationsGenerator.exe" (
        for %%I in ("dist\EmailVariationsGenerator.exe") do (
            echo [INFO] Executable: dist\EmailVariationsGenerator.exe
            echo [INFO] File size: %%~zI bytes
        )
        echo.
        echo The executable is ready for distribution.
        echo Built with uv's fast dependency management.
        echo No Python installation required on target machines.
    ) else (
        echo [WARNING] Executable not found in expected location
    )
) else (
    echo.
    echo [ERROR] Build failed! Check the error messages above.
)

echo.
pause
