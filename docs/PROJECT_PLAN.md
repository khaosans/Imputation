PROJECT PLAN – IBM DATA SCIENCE METHODOLOGY ALIGNMENT
=====================================================

Problem Definition
------------------

- **Business goal:** Quantify viewing engagement and subscription penetration for AAVAIL’s U.S. and Singapore markets despite missing operational data.  
- **Success criteria:** Deliver (a) a reproducible imputation workflow, (b) a processed dataset for downstream analytics, and (c) a stakeholder‑ready visualization comparing markets.

Analytic Approach
-----------------

- Adopt IBM’s Data Science Methodology phases (Agyemang et al., 2020): problem understanding, data understanding, data preparation, modeling (imputation logic), evaluation, and deployment (reporting deliverables).
- Employ Coursera AI Workflow playbook for structured EDA, imputation design, and storytelling (Coursera Project Network, 2023).

Data Requirements
-----------------

- Source: `data/raw/aavail_customer_activity.csv` (synthetic customer activity export).  
- Mandatory fields: `country_name`, `is_subscriber`, `subscriber_type`, `num_streams`, `age`.  
- Governance: Preserve raw extract; document all transformations in notebooks.

Tools and Environment
---------------------

- Python 3.9+ with `pandas`, `numpy`, `matplotlib`, `seaborn`, `jupyter`, and `chart-studio` (for optional interactive visuals).  
- Version control: Git with conventional commit messages referencing tasks.  
- Documentation: Markdown with APA citations.

Imputation Strategy
-------------------

1. **Subscriber type:** Substitute missing values using the modal plan conditioned on `is_subscriber`; mark non‑subscribers as `not_subscribed` to maintain clarity.  
2. **Streaming counts:** Fill missing `num_streams` with the median within each `(country_name, is_subscriber)` cohort. Fallback to global median if necessary.  
3. Log imputation counts and rationale in notebook outputs and `docs/DATA_DICTIONARY.md`.

Visualization Deliverables
--------------------------

- Comparative KPIs (user count, average streams, subscriber percentage) by country.  
- Bar charts for average streams and subscription penetration using accessible color palettes and descriptive captions.  
- Distribution plots (optional) for age and streams to support deeper dives.

Validation & QA
---------------

- Check completeness post-imputation (no blanks in targeted fields).  
- Review summary statistics before and after imputation to confirm minimal distortion.  
- Peer review notebook markdown for clarity and citation accuracy.

Deployment & Handoff
--------------------

- Persist processed data to `data/processed/aavail_data_imputed.csv`.  
- Publish stakeholder dashboard at `reports/aavail_market_insights.html`.  
- Document run book and references in `README.md` and `docs/REFERENCES.md`.




