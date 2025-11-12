#!/usr/bin/env python3
"""
Setup Verification Script
Verifies that all required files and dependencies are present for the AAVAIL Imputation project.
"""

import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and report status."""
    path = Path(filepath)
    if path.exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} MISSING: {filepath}")
        return False

def check_directory_exists(dirpath, description):
    """Check if a directory exists and report status."""
    path = Path(dirpath)
    if path.exists() and path.is_dir():
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description} MISSING: {dirpath}")
        return False

def check_python_package(package_name):
    """Check if a Python package is installed."""
    try:
        __import__(package_name)
        print(f"✅ Python package installed: {package_name}")
        return True
    except ImportError:
        print(f"❌ Python package MISSING: {package_name}")
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("AAVAIL Imputation Project - Setup Verification")
    print("=" * 60)
    print()
    
    all_checks_passed = True
    
    # Check Python version
    print("Python Version:")
    print(f"  Python {sys.version}")
    if sys.version_info < (3, 9):
        print("  ⚠️  Warning: Python 3.9+ recommended")
    else:
        print("  ✅ Python version is 3.9+")
    print()
    
    # Check required files
    print("Required Files:")
    files_to_check = [
        ("data/raw/aavail_customer_activity.csv", "Raw data file"),
        ("requirements.txt", "Dependencies file"),
        ("README.md", "README file"),
        ("SETUP.md", "Setup guide"),
        ("docs/PROJECT_PLAN.md", "Project plan"),
        ("docs/DATA_DICTIONARY.md", "Data dictionary"),
        ("docs/REFERENCES.md", "References"),
        (".gitignore", "Git ignore file"),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    print()
    
    # Check required directories
    print("Required Directories:")
    dirs_to_check = [
        ("data/raw", "Raw data directory"),
        ("data/processed", "Processed data directory"),
        ("notebooks", "Notebooks directory"),
        ("docs", "Documentation directory"),
        ("reports/assets", "Reports assets directory"),
    ]
    
    for dirpath, description in dirs_to_check:
        if not check_directory_exists(dirpath, description):
            all_checks_passed = False
    print()
    
    # Check notebooks
    print("Notebooks:")
    notebooks_to_check = [
        ("notebooks/aavail_eda_assignment.ipynb", "EDA assignment notebook"),
        ("notebooks/aavail_imputation_workflow.ipynb", "Imputation workflow notebook"),
    ]
    
    for filepath, description in notebooks_to_check:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    print()
    
    # Check Python packages
    print("Python Packages:")
    packages_to_check = [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "jupyter",
        "IPython",
    ]
    
    for package in packages_to_check:
        if not check_python_package(package):
            all_checks_passed = False
    print()
    
    # Summary
    print("=" * 60)
    if all_checks_passed:
        print("✅ All checks passed! Your setup looks good.")
        print()
        print("Next steps:")
        print("  1. Activate your virtual environment (if using one)")
        print("  2. Launch Jupyter: jupyter lab")
        print("  3. Open notebooks/aavail_eda_assignment.ipynb")
    else:
        print("❌ Some checks failed. Please review the errors above.")
        print()
        print("Common fixes:")
        print("  - Install missing packages: pip install -r requirements.txt")
        print("  - Ensure you're in the repository root directory")
        print("  - Check that data files are present in data/raw/")
    print("=" * 60)
    
    return 0 if all_checks_passed else 1

if __name__ == "__main__":
    sys.exit(main())

