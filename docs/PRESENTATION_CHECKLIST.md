# Presentation Checklist

## Pre-Presentation Setup

- [ ] Install RISE: `pip install RISE`
- [ ] Enable RISE extension: `jupyter-nbextension enable rise --py --sys-prefix`
- [ ] Restart Jupyter Notebook

## Before Presenting

- [ ] **Run all cells** (Cell > Run All or Kernel > Restart & Run All)
- [ ] Verify all visualizations appear correctly
- [ ] Check that all images load from `reports/assets/`
- [ ] Test RISE slideshow (click RISE button or press `Alt+R`)
- [ ] Practice navigation (arrow keys, space bar)

## During Presentation

### Navigation Controls
- **Arrow Keys**: Navigate between slides
- **Space**: Next slide/fragment
- **Shift+Space**: Previous slide/fragment
- **Esc**: Exit slideshow mode
- **F**: Fullscreen
- **S**: Speaker notes (if added)

### Slide Structure
- **9 main slides** (sections)
- **23 subslices** (detailed content)
- **17 fragments** (incremental reveals)
- **1 skip cell** (setup code)

## Content Verification

### Section 1: Data Ingestion & Missing Values
- [ ] Data loading works
- [ ] Missing value heatmap displays
- [ ] Missing data summary shows correct counts
- [ ] Imputation executes successfully
- [ ] Imputation comparison image loads

### Section 2: Data Summary & Visualizations
- [ ] Market distribution statistics display
- [ ] Subscriber type comparison image loads
- [ ] Streaming activity image loads
- [ ] Age distribution image loads

### Section 3: Singapore Market Investigation
- [ ] Market separation works (df_us, df_sg)
- [ ] Plan distribution comparison displays
- [ ] Streaming statistics by plan show
- [ ] Conversion rates calculate correctly
- [ ] Age statistics display
- [ ] Churn analysis image loads
- [ ] Churn rates calculate correctly

### Section 4: Results & Recommendations
- [ ] All findings display correctly
- [ ] Recommendations are clear

### Appendix
- [ ] Technical details are accessible

## Troubleshooting

### If images don't load:
1. Check that `reports/assets/` directory exists
2. Verify all image files are present
3. Re-run cells that generate visualizations
4. Check file paths in code cells

### If RISE button doesn't appear:
1. Verify RISE is installed: `pip list | grep -i rise`
2. Check extension is enabled: `jupyter-nbextension list`
3. Restart Jupyter Notebook
4. Try browser refresh (Ctrl+R or Cmd+R)

### If cells fail to execute:
1. Check that data files exist in `data/raw/` and `data/processed/`
2. Verify all imports work (run cell 3 first)
3. Run cells in order from top to bottom
4. Check for error messages in cell outputs

## Quick Test

Run this in a new cell to verify everything:
```python
# Quick verification
print("✓ Data loaded:", 'df' in locals() or 'df' in globals())
print("✓ Data imputed:", 'df_imputed' in locals() or 'df_imputed' in globals())
print("✓ Markets separated:", 'df_us' in locals() or 'df_us' in globals())
print("✓ Assets directory:", ASSETS_DIR.exists())
print("✓ Images exist:", len(list(ASSETS_DIR.glob("*.png"))) > 0)
```

## Presentation Tips

1. **Start with overview**: Give audience roadmap
2. **Explain missing values**: Important for data quality understanding
3. **Highlight Singapore factors**: This is the key investigation
4. **Emphasize recommendations**: Actionable insights are critical
5. **Use speaker notes**: Add notes in markdown cells if needed

## Time Allocation (20 minutes)

- Introduction & Overview: 2 min
- Data Ingestion & Missing Values: 4 min
- Data Summary: 3 min
- Singapore Investigation: 7 min
- Results & Recommendations: 3 min
- Q&A: 1 min

