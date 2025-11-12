Imputation Case Study – AAVAIL Streaming
========================================

Overview
--------

This repository documents an end‑to‑end missing data remediation and visualization workflow for the fictional AAVAIL streaming service. Following the IBM Data Science Methodology (Agyemang et al., 2020) and Coursera Project Network’s AI Workflow guidance (Coursera Project Network, 2023), we:

- profile the raw customer activity export,
- design and apply transparent imputation rules, and
- deliver stakeholder‑ready visuals for the United States and Singapore markets.

Use the `notebooks/aavail_imputation_workflow.ipynb` notebook as the primary analytical asset.

Repository Structure
--------------------

```
data/
  raw/         # Unmodified source files
  processed/   # Cleaned & imputed datasets
docs/
  DATA_DICTIONARY.md
  PROJECT_PLAN.md
  REFERENCES.md
notebooks/
  aavail_imputation_workflow.ipynb
reports/
  aavail_market_insights.html
```

Environment Setup
-----------------

1. Install Python 3.9+ and create an isolated environment.
2. Install project dependencies:

```
pip install -r requirements.txt
```

3. Optional: launch Jupyter Lab/Notebook for interactive exploration:

```
jupyter lab
```

Reproducing the Analysis
------------------------

1. Review `docs/PROJECT_PLAN.md` to understand the analytical questions, success criteria, and imputation rationale.
2. Execute `notebooks/aavail_imputation_workflow.ipynb` in order. The notebook exports cleaned data to `data/processed/` and regenerates the executive dashboard located in `reports/`.
3. Open `reports/aavail_market_insights.html` in a browser to inspect the visualization deliverable.

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



