# Local Setup Guide

This guide will help you set up the AAVAIL Imputation project on your local machine.

## Quick Start

```bash
# 1. Clone the repository
git clone <repository-url>
cd Imputation

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter lab
```

## Detailed Setup Instructions

### 1. System Requirements

- **Operating System**: macOS, Linux, or Windows
- **Python**: Version 3.9 or higher
- **Memory**: At least 4GB RAM recommended
- **Disk Space**: ~100MB for project files and dependencies

### 2. Python Installation

If Python is not installed:

- **macOS**: Install via Homebrew: `brew install python3`
- **Linux**: Use package manager: `sudo apt-get install python3 python3-pip` (Ubuntu/Debian)
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

Verify installation:
```bash
python3 --version  # Should show 3.9 or higher
pip3 --version
```

### 3. Virtual Environment Setup

Using a virtual environment isolates project dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

### 4. Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation using the verification script
python verify_setup.py

# Or verify key packages manually
python -c "import pandas; print(f'pandas {pandas.__version__}')"
python -c "import numpy; print(f'numpy {numpy.__version__}')"
python -c "import matplotlib; print(f'matplotlib {matplotlib.__version__}')"
python -c "import seaborn; print(f'seaborn {seaborn.__version__}')"
```

### 5. Verify Data Files

Ensure data files are present:

```bash
# Check raw data
ls -lh data/raw/aavail_customer_activity.csv

# Check processed data (may not exist until you run the imputation workflow)
ls -lh data/processed/aavail_data_imputed.csv
```

### 6. Launch Jupyter

```bash
# Start Jupyter Lab (recommended)
jupyter lab

# Or start Jupyter Notebook (classic interface)
jupyter notebook
```

Your browser should open automatically. If not, navigate to the URL shown in the terminal (typically `http://localhost:8888`).

### 7. Run the Notebooks

1. **Open the EDA Assignment**:
   - Navigate to `notebooks/aavail_eda_assignment.ipynb`
   - Click on the notebook to open it
   - Execute cells using Shift+Enter or click "Run All"

2. **Open the Imputation Workflow**:
   - Navigate to `notebooks/aavail_imputation_workflow.ipynb`
   - Execute cells in order

## Project Structure

```
Imputation/
├── data/
│   ├── raw/                              # Source data (immutable)
│   │   └── aavail_customer_activity.csv
│   └── processed/                        # Generated data
│       └── aavail_data_imputed.csv
├── docs/                                 # Documentation
│   ├── DATA_DICTIONARY.md
│   ├── PROJECT_PLAN.md
│   └── REFERENCES.md
├── notebooks/                            # Jupyter notebooks
│   ├── aavail_eda_assignment.ipynb      # EDA assignment
│   └── aavail_imputation_workflow.ipynb # Imputation workflow
├── reports/                              # Outputs
│   ├── aavail_market_insights.html
│   └── assets/                           # Visualization images
├── .gitignore
├── .gitattributes
├── requirements.txt                      # Python dependencies
├── README.md                             # Project overview
├── SETUP.md                              # This file
└── LICENSE
```

## Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'X'"

**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # Reactivate if needed
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: data/raw/aavail_customer_activity.csv"

**Solution**: Verify you're running the notebook from the correct directory:
- The notebook expects to be run from the `notebooks/` directory
- The path `BASE_DIR = Path("..")` assumes you're in `notebooks/`
- If running from root, change to `BASE_DIR = Path(".")`

### Issue: Jupyter doesn't open in browser

**Solution**: 
1. Copy the URL from the terminal (e.g., `http://localhost:8888/?token=...`)
2. Paste it into your browser
3. Or use: `jupyter lab --no-browser` and manually open the URL

### Issue: "Kernel not found" in Jupyter

**Solution**: Install ipykernel in your virtual environment:
```bash
source venv/bin/activate
pip install ipykernel
python -m ipykernel install --user --name=venv
```

Then select the kernel in Jupyter: Kernel → Change Kernel → venv

### Issue: Plot not displaying

**Solution**: 
- In Jupyter, ensure `%matplotlib inline` is in a cell (or use `%matplotlib widget` for interactive plots)
- Check that matplotlib backend is correct: `import matplotlib; print(matplotlib.get_backend())`

## Deactivating Virtual Environment

When done working:

```bash
deactivate  # Removes (venv) from prompt
```

## Updating Dependencies

If requirements.txt is updated:

```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

## Getting Help

- Check `docs/PROJECT_PLAN.md` for project details
- Review `docs/DATA_DICTIONARY.md` for data schema
- See `CONTRIBUTING.md` for development guidelines
- Check `README.md` for project overview

## Next Steps

After setup:
1. Read `docs/PROJECT_PLAN.md` to understand the project
2. Review `docs/DATA_DICTIONARY.md` for data structure
3. Open `notebooks/aavail_eda_assignment.ipynb` to start the assignment
4. Follow the notebook cells in order

