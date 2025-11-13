Imputation Case Study – AAVAIL Streaming
========================================

Overview
--------

This repository documents an end‑to‑end missing data remediation and visualization workflow for the fictional AAVAIL streaming service. Following the IBM Data Science Methodology (Agyemang et al., 2020) and Coursera Project Network’s AI Workflow guidance (Coursera Project Network, 2023), we:

- profile the raw customer activity export,
- design and apply transparent imputation rules, and
- deliver stakeholder‑ready visuals for the United States and Singapore markets.

Use the `notebooks/aavail_imputation_workflow.ipynb` notebook as the primary analytical asset. The `notebooks/aavail_eda_assignment.ipynb` notebook contains comprehensive exploratory data analysis and visualizations. The `notebooks/aavail_presentation.ipynb` notebook provides a RISE slideshow presentation for deliverables.

Repository Setup
----------------

This repository is initialized with Git. To connect it to a private remote repository (e.g., GitHub, GitLab):

1. **Create a private repository** on your preferred Git hosting service (GitHub, GitLab, Bitbucket, etc.)

2. **Add the remote** (replace `<your-repo-url>` with your actual repository URL):
   ```bash
   git remote add origin <your-repo-url>
   ```

3. **Push to the remote**:
   ```bash
   git branch -M main
   git push -u origin main
   ```

4. **Verify the connection**:
   ```bash
   git remote -v
   ```

**Note**: Ensure your remote repository is set to **private** in the repository settings on your Git hosting platform.

Repository Structure
--------------------

```
Imputation/
├── data/
│   ├── raw/                               # Unmodified source files
│   │   └── aavail_customer_activity.csv   # Raw customer data
│   └── processed/                         # Cleaned & imputed datasets
│       └── aavail_data_imputed.csv        # Processed data (generated)
├── docs/
│   ├── DATA_DICTIONARY.md                 # Data schema and imputation notes
│   ├── PROJECT_PLAN.md                    # Project methodology and plan
│   ├── PRESENTATION_APPENDIX.md           # Technical appendix for presentation
│   ├── PRESENTATION_README.md             # RISE presentation guide
│   ├── PRESENTATION_CHECKLIST.md          # Pre-presentation checklist
│   ├── REFERENCES.md                      # APA citations
│   └── VIEW_PRESENTATION.md               # Browser viewing instructions
├── notebooks/
│   ├── aavail_imputation_workflow.ipynb   # Primary imputation workflow
│   ├── aavail_eda_assignment.ipynb        # EDA and visualization analysis
│   └── aavail_presentation.ipynb          # RISE slideshow presentation
├── reports/
│   ├── aavail_market_insights.html        # Executive dashboard
│   ├── aavail_eda_assignment.html         # EDA report export
│   ├── aavail_presentation.html           # Browser-viewable presentation
│   ├── view_presentation.html             # Presentation viewer page
│   └── assets/                            # Visualization images
│       ├── age_by_subscriber_type.png
│       ├── age_distribution_by_country.png
│       ├── avg_streams_by_tier.png
│       ├── churn_analysis.png
│       ├── imputation_comparison.png
│       ├── missingness_heatmap.png
│       └── [other visualization files]
├── scripts/
│   ├── create_simple_html.py              # HTML presentation generator
│   ├── export_to_html.py                  # Presentation export utility
│   ├── export_presentation.sh             # Export script (bash)
│   └── verify_setup.py                    # Environment verification
├── .gitignore                             # Git ignore rules
├── requirements.txt                       # Python dependencies
├── README.md                              # This file
├── SETUP.md                               # Detailed setup instructions
├── CONTRIBUTING.md                        # Contribution guidelines
└── LICENSE                                # MIT License
```

Environment Setup
-----------------

### Prerequisites

- **Python 3.9 or higher** (Python 3.9+ recommended)
- **Git** (for cloning the repository)
- **pip** (Python package installer)

### Step-by-Step Setup

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd Imputation
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # Using venv (built-in)
   python3 -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install project dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify installation**:
   ```bash
   # Run the verification script (recommended)
   python scripts/verify_setup.py
   
   # Or verify manually
   python -c "import pandas, numpy, matplotlib, seaborn, jupyter; print('All packages installed successfully!')"
   ```

5. **Launch Jupyter Lab/Notebook** for interactive exploration:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

### Running the Notebooks

1. **Start Jupyter Lab/Notebook** from the repository root:
   ```bash
   jupyter lab
   ```

2. **Open the assignment notebook**:
   - Navigate to `notebooks/aavail_eda_assignment.ipynb`
   - Execute cells in order (Shift+Enter or Run All)

3. **Verify data files are present**:
   - Raw data: `data/raw/aavail_customer_activity.csv`
   - Processed data: `data/processed/aavail_data_imputed.csv` (generated after running imputation workflow)

### Troubleshooting

- **Import errors**: Ensure virtual environment is activated and all packages are installed
- **Path errors**: Run notebooks from the repository root directory, or ensure `BASE_DIR = Path("..")` is correct
- **Missing data files**: Verify `data/raw/aavail_customer_activity.csv` exists in the repository

Reproducing the Analysis
------------------------

1. Review `docs/PROJECT_PLAN.md` to understand the analytical questions, success criteria, and imputation rationale.
2. Execute `notebooks/aavail_imputation_workflow.ipynb` in order. The notebook exports cleaned data to `data/processed/` and regenerates the executive dashboard located in `reports/`.
3. Open `reports/aavail_market_insights.html` in a browser to inspect the visualization deliverable.

Viewing the Presentation
------------------------

The RISE presentation can be viewed in multiple ways:

1. **Browser (HTML)**: Open `reports/aavail_presentation.html` in any web browser
   - See `docs/VIEW_PRESENTATION.md` for detailed instructions
   
2. **Interactive RISE**: Open `notebooks/aavail_presentation.ipynb` in Jupyter
   - Install RISE: `pip install RISE`
   - Run all cells, then click RISE button or press `Alt+R`
   - See `docs/PRESENTATION_README.md` for full guide

3. **Regenerate HTML**: Run `python scripts/create_simple_html.py` to recreate the HTML version

Data Governance
---------------

- Raw data remains immutable in `data/raw/`.
- Processed outputs are versioned in `data/processed/` with descriptive filenames.
- All transformation logic lives in notebooks/scripts that accompany clear markdown rationale for transparency and auditability.

Contributing
------------

1. Fork or branch from `main`.
2. Ensure notebooks are cleared of extraneous output before committing (`jupyter nbconvert --ClearOutput`).  
3. Run linters/tests as defined in future CI workflows.
4. Submit a pull request referencing relevant issues and include updates to `docs/REFERENCES.md` if new external sources are cited.

References
----------

Full APA citations are maintained in `docs/REFERENCES.md`. Cite each source inline when extending notebooks or documentation.



