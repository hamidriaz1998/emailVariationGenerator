#!/usr/bin/env python3
"""
Simplified build script for Email Variations Generator
Creates standalone executables using PyInstaller and uv

Usage:
    python build.py

Requirements:
    - uv package manager installed
    - Dependencies installed (uv add pyqt6 pyinstaller)

Output:
    - dist/EmailVariationsGenerator (Linux/Mac)
    - dist/EmailVariationsGenerator.exe (Windows)
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def run_command(cmd):
    """Run a command and return success status"""
    try:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return False


def clean_build():
    """Clean previous build artifacts"""
    print("Cleaning previous build artifacts...")

    for dir_name in ["build", "dist"]:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Removed {dir_name}/")

    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"Removed {spec_file}")


def build_executable():
    """Build the executable using PyInstaller"""
    print("Creating standalone executable...")

    system = platform.system().lower()

    # Create directories
    os.makedirs("dist", exist_ok=True)
    os.makedirs("build", exist_ok=True)

    # Build command
    cmd = [
        "uv",
        "run",
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name",
        "EmailVariationsGenerator",
        "--distpath",
        "dist",
        "--workpath",
        "build",
        "--specpath",
        "build",
        "main.py",
    ]

    if run_command(cmd):
        executable_name = (
            "EmailVariationsGenerator.exe"
            if system == "windows"
            else "EmailVariationsGenerator"
        )
        executable_path = os.path.join("dist", executable_name)

        if os.path.exists(executable_path):
            if system != "windows":
                os.chmod(executable_path, 0o755)

            size_mb = os.path.getsize(executable_path) / (1024 * 1024)
            print("\n✅ Build successful!")
            print(f"📦 Executable: {executable_path}")
            print(f"📏 Size: {size_mb:.1f} MB")
            return True

    return False


def main():
    """Main build process"""
    print("🚀 Email Variations Generator - Build Script")
    print("=" * 50)
    print(f"🖥️  Platform: {platform.system()}")
    print(f"🐍 Python: {sys.version.split()[0]}")

    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found")
        return 1

    try:
        clean_build()

        if build_executable():
            print("\n🎉 Build completed successfully!")
            print("\n📋 The executable is ready for distribution")
            return 0
        else:
            print("\n❌ Build failed!")
            return 1

    except KeyboardInterrupt:
        print("\n⚠️  Build interrupted")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
