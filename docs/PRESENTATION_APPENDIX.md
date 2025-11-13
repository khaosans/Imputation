# Presentation Appendix: Technical Details

## Overview

This document provides technical details and methodology for the AAVAIL Market Analysis presentation. It serves as a supplement to the RISE slideshow presentation.

## Data Ingestion & Missing Value Handling

### Data Source
- **File:** `data/raw/aavail_customer_activity.csv`
- **Records:** 1,000 customer records
- **Markets:** United States (700 records) and Singapore (300 records)
- **Collection Period:** Not specified in dataset

### Missing Value Analysis

#### Missing Value Summary
| Column | Missing Count | Missing Percentage | Data Type |
|--------|---------------|-------------------|-----------|
| `subscriber_type` | 72 | 7.2% | Categorical |
| `num_streams` | 46 | 4.6% | Numeric |
| **Total Missing** | **118** | **1.69%** | - |

#### Missing Value Patterns
- `subscriber_type`: Missing values likely associated with non-subscribers or data entry issues
- `num_streams`: Missing values distributed across both markets and subscription statuses
- No systematic pattern detected in missing data (random missingness)

### Imputation Methodology

#### Numeric Variable: `num_streams`
- **Method:** Median imputation
- **Rationale:** 
  - Median is robust to outliers
  - Preserves central tendency without influence from extreme values
  - Appropriate for skewed distributions
- **Imputed Value:** 19.0 streams
- **Values Imputed:** 46 records

#### Categorical Variable: `subscriber_type`
- **Method:** Mode imputation
- **Rationale:**
  - Standard approach for categorical data
  - Uses most frequent category
  - Maintains distribution characteristics
- **Imputed Value:** 'aavail_basic' (most frequent plan)
- **Values Imputed:** 72 records

#### Imputation Validation
- Post-imputation: 0 missing values remaining
- Distribution analysis: Imputation maintained data integrity
- No significant distortion of variable distributions

### Data Cleaning

#### Columns Dropped
- **`customer_name`**: Removed for privacy (PII) and analytical purposes
  - Not needed for analysis
  - Contains personally identifiable information
  - No impact on analytical capabilities

#### Final Dataset Structure
- **Columns Retained:** 7
  - `customer_id`
  - `country_name`
  - `age`
  - `is_subscriber`
  - `subscriber_type`
  - `num_streams`
- **Records:** 1,000 (complete, no missing values)

## Singapore Market Investigation

### Market Comparison Framework

#### Market Size
- **United States:** 700 customers (70% of total)
- **Singapore:** 300 customers (30% of total)

#### Key Metrics Comparison

| Metric | United States | Singapore |
|--------|---------------|-----------|
| Total Customers | 700 | 300 |
| Subscriber Rate | ~85% | ~60% |
| Median Age | ~24 | ~27 |
| Median Streams | ~19 | ~19 |

### Factor Analysis: Singapore Market

#### Factor 1: Plan Popularity Patterns
**Finding:** Singapore shows similar plan preferences to US market
- Premium plan: Most popular in both markets
- Basic plan: Second most common
- Unlimited plan: Smallest customer base

**Interpretation:** Consistent global preferences suggest universal value proposition

#### Factor 2: Streaming Behavior
**Finding:** Unlimited plan underperforms in Singapore
- Unlimited plan shows LOWER median streams than basic/premium
- All plans have similar streaming distributions
- Outlier detected: Singapore unlimited plan has customer with near 0 streams

**Interpretation:** Unlimited plan not delivering expected value proposition

#### Factor 3: Subscriber Conversion Rates
**Finding:** High conversion rates in both markets
- Singapore: ~60% subscriber rate
- United States: ~85% subscriber rate
- Both markets show effective platform conversion

**Interpretation:** Strong engagement despite market size differences

#### Factor 4: Age Demographics
**Finding:** Consistent demographic profiles
- Core demographic: 19-35 age group in both markets
- Median age: ~24-27 years
- Some older outliers in Singapore (up to 70s)

**Interpretation:** Global user base with consistent characteristics

#### Factor 5: Churn Analysis
**Finding:** Similar churn patterns across markets
- Churn rates comparable between US and Singapore
- Plan-specific churn variations exist
- Streaming activity correlates with churn risk

**Interpretation:** Market-agnostic retention strategies may be effective

## Statistical Methods

### Descriptive Statistics
- **Central Tendency:** Mean, median
- **Dispersion:** Standard deviation, range
- **Distribution:** Histograms, box plots
- **Categorical:** Frequency tables, proportions

### Visualization Techniques
- **Missing Data:** Heatmaps
- **Distributions:** Histograms, box plots, violin plots
- **Comparisons:** Side-by-side bar charts, grouped comparisons
- **Relationships:** Scatter plots, correlation analysis

### Analysis Tools
- **Python Libraries:**
  - `pandas`: Data manipulation and analysis
  - `numpy`: Numerical computations
  - `matplotlib`: Basic plotting
  - `seaborn`: Statistical visualizations

## Limitations & Assumptions

### Data Limitations
1. **Missing Data:** 7.2% missing subscriber_type may introduce bias
2. **Imputation Assumptions:** Mode/median imputation assumes missing at random
3. **Temporal Context:** No time-series information available
4. **Sample Size:** Singapore market (300 records) smaller than US (700)

### Methodological Assumptions
1. **Imputation:** Missing values are missing at random (MAR)
2. **Churn Definition:** Based on `is_subscriber` flag only
3. **Market Segmentation:** Binary country-based segmentation
4. **Plan Value:** Assumes streaming activity reflects plan value

## Recommendations Summary

### Immediate Actions
1. **User Research:** Investigate unlimited plan subscriber motivations
2. **Data Quality:** Audit source systems for missing subscriber_type data
3. **Market Strategy:** Develop Singapore-specific growth initiatives

### Long-term Initiatives
1. **Plan Optimization:** Re-evaluate unlimited plan value proposition
2. **Data Governance:** Implement validation at data ingestion
3. **Analytics Enhancement:** Longitudinal analysis and feature usage tracking

## References

### Data Sources
- `data/raw/aavail_customer_activity.csv`: Raw customer data
- `data/processed/aavail_data_imputed.csv`: Processed dataset with imputed values

### Analysis Notebooks
- `notebooks/aavail_imputation_workflow.ipynb`: Primary imputation workflow
- `notebooks/aavail_eda_assignment.ipynb`: Exploratory data analysis
- `notebooks/aavail_presentation.ipynb`: RISE presentation notebook

### Documentation
- `docs/DATA_DICTIONARY.md`: Complete data dictionary
- `docs/PROJECT_PLAN.md`: Project methodology and plan
- `docs/REFERENCES.md`: Academic and technical references

## Contact & Further Information

For questions about this analysis or to request additional details, please refer to the main project documentation in the `docs/` directory or review the analysis notebooks in the `notebooks/` directory.

