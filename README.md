# project-marketing-eda
End‑to‑end cleaning + EDA of a real‑world marketing‑campaign dataset — reproducible Python workflow, data‑quality tests, and business insights

# Marketing Campaign — Data Cleaning & Exploratory Analysis

This project takes a **messy, real‑world marketing‑campaign dataset** and walks it through a fully reproducible pipeline:

1. **Raw → Clean:** rigorous data‑quality checks with [pandera](https://pandera.readthedocs.io/)  
2. **Exploratory Data Analysis (EDA):** quick insights in Jupyter Notebooks  
3. **Business Findings:** actionable metrics that a marketing manager can use today  

> **Why it exists:**  
> Marketing teams often sit on noisy data that hides great insights; this repo proves how a single junior analyst (me!) can transform that data into value in hours, following senior‑level best practices (version control, environment isolation, documented assumptions).

---

## Project structure

project‑marketing‑eda/ ├── data/ │ ├── raw/ # untouched CSV / ZIP from source │ └── processed/ # cleaned & typed parquet/CSV ├── notebooks/ │ ├── 00_initial_inspection.ipynb │ └── 01_cleaning_eda.ipynb ├── src/ # reusable Python modules │ └── data_utils.py ├── requirements.txt ├── Makefile # one‑command workflow (make all) └── README.md