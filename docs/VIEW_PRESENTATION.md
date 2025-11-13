# Viewing the AAVAIL Presentation

## Quick Start - Browser View

The presentation has been exported to HTML and can be viewed in any web browser:

### Option 1: Open HTML File Directly

```bash
# On macOS
open reports/aavail_presentation.html

# On Linux
xdg-open reports/aavail_presentation.html

# On Windows
start reports/aavail_presentation.html

# Or simply double-click the file in your file manager
```

**File Location:** `reports/aavail_presentation.html`

### Option 2: View via Web Server (Recommended)

For best compatibility, serve via a local web server:

```bash
# Python 3
cd reports
python3 -m http.server 8000

# Then open in browser:
# http://localhost:8000/aavail_presentation.html
```

## Navigation

Once the HTML file is open in your browser:

- **Arrow Keys**: Navigate between slides (← →)
- **Space Bar**: Next slide
- **Navigation Buttons**: Use Previous/Next buttons in bottom-right corner
- **Slide Counter**: Shows current slide number (e.g., "3 / 9")

## Features

- ✅ **9 main slides** with all content
- ✅ **Dark theme** for easy viewing
- ✅ **Keyboard navigation** (arrow keys, space)
- ✅ **Print-friendly** (can be printed or saved as PDF)
- ✅ **Self-contained** (no internet connection needed)

## Alternative: Interactive RISE Slideshow

For the full interactive RISE experience with transitions:

1. **Install RISE** (if not already installed):
   ```bash
   pip install RISE
   jupyter-nbextension install rise --py --sys-prefix
   jupyter-nbextension enable rise --py --sys-prefix
   ```

2. **Open in Jupyter**:
   ```bash
   jupyter notebook notebooks/aavail_presentation.ipynb
   ```

3. **Run all cells**: `Cell > Run All`

4. **Enter RISE mode**: Click the RISE button or press `Alt+R`

5. **Navigate**: Use arrow keys or space bar

## File Locations

- **HTML Presentation**: `reports/aavail_presentation.html` ← **Open this in browser**
- **Notebook**: `notebooks/aavail_presentation.ipynb`
- **Visualizations**: `reports/assets/`
- **Viewer Instructions**: `view_presentation.html`

## Troubleshooting

### Images Not Showing
- Ensure all cells in the notebook have been executed
- Check that `reports/assets/` contains all PNG files
- Re-run the notebook: `Cell > Run All`

### HTML File Not Opening
- Try opening with a different browser
- Check file permissions
- Use the web server method (Option 2 above)

### Want to Regenerate HTML
```bash
python3 create_simple_html.py
```

## Presentation Structure

1. **Title Slide** - AAVAIL Market Analysis
2. **Agenda** - Overview of presentation
3. **Overview** - What to expect
4. **Section 1** - Data Ingestion & Missing Values
5. **Section 2** - Data Summary & Visualizations
6. **Section 3** - Singapore Market Investigation
7. **Section 4** - Results & Recommendations
8. **Appendix** - Technical Details
9. **Thank You** - Closing slide

---

**Ready to present!** Open `reports/aavail_presentation.html` in your browser to get started.

