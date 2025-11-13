#!/usr/bin/env python3
"""
Export RISE presentation to HTML for browser viewing.
This script converts the Jupyter notebook to an HTML slideshow.
"""

import subprocess
import sys
from pathlib import Path

def export_presentation():
    """Export the RISE presentation to HTML."""
    
    notebook_path = Path("notebooks/aavail_presentation.ipynb")
    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)
    
    if not notebook_path.exists():
        print(f"Error: Notebook not found at {notebook_path}")
        return False
    
    print("Exporting RISE presentation to HTML...")
    print(f"Notebook: {notebook_path}")
    print(f"Output directory: {output_dir}")
    
    # Try using jupyter nbconvert with RISE/reveal.js
    try:
        # Method 1: Export as reveal.js slides
        cmd = [
            "jupyter", "nbconvert",
            "--to", "slides",
            "--reveal-prefix", "https://cdn.jsdelivr.net/npm/reveal.js@4.3.1",
            str(notebook_path),
            "--output-dir", str(output_dir),
            "--output", "aavail_presentation"
        ]
        
        print(f"\nRunning: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            output_file = output_dir / "aavail_presentation.slides.html"
            if output_file.exists():
                print(f"\n✓ Success! Presentation exported to:")
                print(f"  {output_file.absolute()}")
                print(f"\nOpen in browser: file://{output_file.absolute()}")
                return True
            else:
                print("Warning: Command succeeded but output file not found")
        else:
            print(f"Error: {result.stderr}")
            
    except FileNotFoundError:
        print("Error: jupyter command not found")
        print("Please install Jupyter: pip install jupyter nbconvert")
        return False
    
    # Try alternative: Export as regular HTML
    try:
        print("\nTrying alternative: Export as HTML...")
        cmd = [
            "jupyter", "nbconvert",
            "--to", "html",
            str(notebook_path),
            "--output-dir", str(output_dir),
            "--output", "aavail_presentation"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            output_file = output_dir / "aavail_presentation.html"
            if output_file.exists():
                print(f"\n✓ HTML exported to:")
                print(f"  {output_file.absolute()}")
                print("\nNote: This is a regular HTML export, not RISE slides.")
                print("For RISE slideshow, use the notebook directly with RISE extension.")
                return True
    except Exception as e:
        print(f"Error: {e}")
    
    return False

if __name__ == "__main__":
    success = export_presentation()
    sys.exit(0 if success else 1)

