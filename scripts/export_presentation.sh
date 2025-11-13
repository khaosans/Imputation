#!/bin/bash
# Script to export RISE presentation to HTML

echo "Exporting RISE presentation to HTML..."

# Check if RISE is installed
python3 -c "import rise" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "RISE is not installed. Installing..."
    python3 -m pip install RISE
fi

# Navigate to notebooks directory
cd notebooks

# Export using jupyter nbconvert with RISE
jupyter nbconvert --to slides --reveal-prefix=reveal.js aavail_presentation.ipynb

# Also create HTML version
jupyter nbconvert --to html aavail_presentation.ipynb --output-dir=../reports

echo "Presentation exported successfully!"
echo "HTML file: reports/aavail_presentation.html"
echo "Slides file: notebooks/aavail_presentation.slides.html"

