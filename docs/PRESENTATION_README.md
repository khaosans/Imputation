# RISE Presentation Guide

## Overview

This directory contains a RISE-enabled Jupyter notebook presentation for the AAVAIL Market Analysis deliverable.

## Files

- `notebooks/aavail_presentation.ipynb`: Main RISE presentation notebook
- `docs/PRESENTATION_APPENDIX.md`: Technical appendix with detailed methodology
- `export_presentation.sh`: Script to export presentation to HTML

## Installation

### Prerequisites
- Python 3.9+
- Jupyter Notebook or JupyterLab
- Required packages (see `requirements.txt`)

### Install RISE

```bash
# Using pip
pip install RISE

# Or using conda
conda install -c conda-forge rise
```

### Install Jupyter Extension

After installing RISE, enable the extension:

```bash
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

## Running the Presentation

### Method 1: Interactive Slideshow (Recommended)

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `notebooks/aavail_presentation.ipynb`

3. Click the "Enter/Exit RISE Slideshow" button in the toolbar (or press `Alt+R`)

4. Navigate slides:
   - **Arrow keys**: Navigate between slides
   - **Space**: Next slide/fragment
   - **Shift+Space**: Previous slide/fragment
   - **Esc**: Exit slideshow mode

### Method 2: Export to HTML

Run the export script:

```bash
./export_presentation.sh
```

Or manually:

```bash
cd notebooks
jupyter nbconvert --to slides --reveal-prefix=reveal.js aavail_presentation.ipynb
```

The HTML file will be created as `aavail_presentation.slides.html` in the notebooks directory.

## Presentation Structure

### Section 1: Data Ingestion & Missing Values
- Data loading process
- Missing value identification
- Imputation strategy
- Before/after comparisons

### Section 2: Data Summary & Visualizations
- Dataset overview
- Key metrics
- Distribution visualizations

### Section 3: Singapore Market Investigation
- Market size comparison
- Five key factors explaining Singapore situation
- Comparative analysis with US market

### Section 4: Results & Recommendations
- Key findings
- Discussion of results
- Actionable recommendations
- Next steps

### Appendix
- Technical methodology
- Data dictionary
- Additional resources

## Slide Types

- **Slide**: Main slide (new section)
- **Subslide**: Subsection within a section
- **Fragment**: Appears incrementally on same slide
- **Skip**: Code cells that don't appear in presentation

## Tips

1. **Run all cells first**: Execute all code cells before starting the presentation to ensure visualizations are generated
2. **Check visualizations**: Ensure all images in `reports/assets/` exist
3. **Test navigation**: Practice navigating through slides before presenting
4. **Speaker notes**: Add notes in markdown cells with `notes` slide type for speaker guidance

## Troubleshooting

### RISE button not appearing
- Ensure RISE is properly installed and extension is enabled
- Restart Jupyter Notebook after installation
- Check browser console for errors

### Visualizations not showing
- Run all code cells in the notebook
- Verify image files exist in `reports/assets/`
- Check file paths are correct relative to notebook location

### Export issues
- Ensure `reveal.js` is available (RISE includes it)
- Check that all dependencies are installed
- Verify notebook is saved before exporting

## Additional Resources

- [RISE Documentation](https://rise.readthedocs.io/)
- [Reveal.js Documentation](https://revealjs.com/)
- Technical details: See `docs/PRESENTATION_APPENDIX.md`

