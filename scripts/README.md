# Scripts Directory

Utility scripts for the AAVAIL Imputation project.

## Scripts

### `create_simple_html.py`
Converts the RISE presentation notebook to a standalone HTML file that can be viewed in any browser.

**Usage:**
```bash
python scripts/create_simple_html.py
```

**Output:** `reports/aavail_presentation.html`

### `export_to_html.py`
Alternative export script using nbconvert (requires nbconvert package).

**Usage:**
```bash
python scripts/export_to_html.py
```

### `export_presentation.sh`
Bash script to export RISE presentation to HTML using jupyter nbconvert.

**Usage:**
```bash
bash scripts/export_presentation.sh
```

**Requirements:** RISE and jupyter nbconvert must be installed.

### `verify_setup.py`
Verifies that all required Python packages are installed and the environment is properly configured.

**Usage:**
```bash
python scripts/verify_setup.py
```

**Checks:**
- Python version (3.9+)
- Required packages (pandas, numpy, matplotlib, seaborn, jupyter)
- Data files existence
- Directory structure

## Requirements

All scripts require Python 3.9+ and the packages listed in `requirements.txt`.

For HTML export scripts, additional packages may be needed:
- `nbconvert` (for `export_to_html.py`)
- `RISE` (for RISE presentation features)

Install with:
```bash
pip install -r requirements.txt
```

