DATA DICTIONARY – AAVAIL STREAMING SAMPLE
==========================================

| Column Name       | Type      | Description                                                                 | Source                | Notes on Imputation                                     |
|-------------------|-----------|-----------------------------------------------------------------------------|-----------------------|---------------------------------------------------------|
| `customer_id`     | Integer   | Unique identifier per customer record.                                      | Raw CSV export        | No missing values.                                      |
| `country_name`    | Category  | Customer’s market segment (`united_states`, `singapore`).                   | Raw CSV export        | No missing values.                                      |
| `age`             | Float     | Customer age in years.                                                      | Raw CSV export        | No missing values detected.                             |
| `customer_name`   | String    | Synthetic first and last name.                                              | Raw CSV export        | No missing values.                                      |
| `is_subscriber`   | Boolean   | Indicates whether the customer currently holds an AAVAIL subscription.     | Raw CSV export        | No missing values.                                      |
| `subscriber_type` | Category  | Subscription plan label (`aavail_basic`, `aavail_premium`, `aavail_unlimited`). | Raw CSV export        | 72 blanks filled with modal plan by subscriber status; non‑subscribers labeled `not_subscribed`. |
| `num_streams`     | Float     | Streams completed by the customer in the snapshot period.                   | Raw CSV export        | 46 blanks filled with median streams for `(country, is_subscriber)` group. |

File Inventory
--------------

- `data/raw/aavail_customer_activity.csv`: Original unaltered export.  
- `data/processed/aavail_data_imputed.csv`: Cleaned file with imputed columns following the strategy above.

Revision History
----------------

- 2025‑11‑12 – Initial release accompanying `aavail_imputation_workflow.ipynb`.




