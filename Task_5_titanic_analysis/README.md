# 🚢 Task 5 — Titanic Data Cleaning, Analysis & Interactive Dashboard

## 📌 Project Overview

This project uses **Python only** to audit and clean Titanic passenger data, handle missing values, engineer useful features, calculate KPIs, and explore the dataset through an interactive dashboard.

The dashboard is built with **Streamlit and Plotly**. No Excel, Power BI, Tableau, or other data-analysis software is used.

## 🎯 Objectives

- Audit the dataset and identify data-quality issues.
- Handle missing values using approaches appropriate to each column.
- Identify and investigate fare outliers without automatically deleting legitimate values.
- Create useful features for passenger demographics and travel patterns.
- Calculate summary KPIs and explore patterns with charts.
- Build an interactive dashboard with filters and multiple analysis sections.
- Export the cleaned dataset for reuse.

## 🧰 Tools & Libraries

- **Python**
- **Pandas** — data manipulation and cleaning
- **NumPy** — numerical operations
- **Matplotlib & Seaborn** — exploratory visualizations in the notebook
- **Plotly** — interactive charts
- **Streamlit** — interactive dashboard interface
- **Jupyter Notebook** — analysis workflow

## 📂 Project Files

Recommended filenames and folder layout:

```text
Task-5-Titanic-Analytics/
├── README.md
├── File_3.csv
├── titanic_analysis.ipynb
├── titanic_cleaned.csv
├── app_streamlit.py
└── eda_overview.png          # generated when the notebook visualization cell runs
```

The uploaded files currently have slightly different names (`File 3.csv`, `titanic_analysis(2).ipynb`, `titanic_cleaned(2).csv`, and `app_streamlit(1).py`). Rename them to the names shown above, or update the corresponding file paths in the notebook and dashboard before running.

## 🧹 Data Cleaning & Preparation

The notebook applies the following steps:

1. **Data-quality audit**
   - Checks dataset dimensions, duplicate rows, duplicate passenger IDs, and missing-value counts and percentages.
   - The provided raw dataset contains **418 rows and 12 columns**.
   - No duplicate rows or duplicate `PassengerId` values were found.

2. **Text normalization**
   - Trims whitespace from column names and text values.
   - Converts empty strings and string representations of missing values to actual missing values.

3. **Title extraction**
   - Extracts passenger titles from `Name`.
   - Groups uncommon titles into a `Rare` category and standardizes variants such as `Mlle`, `Ms`, and `Mme`.

4. **Missing-value handling**
   - **Age:** imputes using the median for the matching `Title` and `Pclass` group, then falls back to the passenger-class median and overall median.
   - **Fare:** fills missing values using the median fare for the passenger class. Non-positive fares are treated as invalid and imputed using the class median.
   - **Embarked:** uses the mode when values are missing.
   - **Cabin:** because cabin data is very sparse, creates `Deck` and `HasCabin` features instead of imputing cabin identifiers, then drops the original `Cabin` column.

5. **Outlier treatment**
   - Uses the IQR rule to identify unusually high fares.
   - Creates `Fare_capped` for visualizations, while retaining the original `Fare` values rather than deleting potentially genuine high fares.

6. **Feature engineering**
   - Creates `FamilySize` and `IsAlone`.
   - Groups passengers into `AgeGroup` and `FareBand`.
   - Adds readable labels for passenger class, embarkation port, and outcome.
   - Adds `TicketGroup` to show how many records share a ticket.

The cleaned dataset contains **418 rows and 23 columns**, with **no missing values** in the exported file.

## 📊 KPIs

The provided cleaned dataset produces the following overall metrics:

| KPI | Result |
|---|---:|
| Total passenger records | 418 |
| Records labelled “Survived” | 152 |
| Records labelled “Died” | 266 |
| Labelled survival rate | 36.36% |
| Average age after imputation | 29.39 years |
| Median fare | 14.46 |
| Travelling alone | 60.53% |
| Average family size | 1.84 people |

> **Important data-integrity warning:** The `Survived` column in this file is perfectly determined by `Sex`: all 152 female records are labelled `1` and all 266 male records are labelled `0`. This is consistent with a gender-based baseline submission label, not reliable historical survival outcomes. Therefore, the survival KPIs and charts describe the supplied labels and must not be presented as factual historical survival statistics. This limitation is explicitly highlighted in the notebook and dashboard.

## 🔎 Key Insights

- **The outcome label has a major limitation:** it perfectly matches gender, so comparisons involving `Survived` cannot establish real historical survival patterns.
- **Third class is the largest passenger group:** 218 of 418 records, approximately **52.15%**.
- **Age required thoughtful imputation:** 86 age values were missing in the raw data. Imputing within title and passenger class helps preserve meaningful differences between passenger groups.
- **Cabin information is sparse:** 327 of 418 raw records have no cabin value. `Deck` and `HasCabin` preserve the available cabin signal without inventing cabin numbers.
- **Fare values are right-skewed:** 55 fares exceed the IQR upper fence. They are capped in a separate plotting column rather than removed from the original fare data.
- **Many passengers are recorded as travelling alone:** approximately **60.53%** based on the engineered `IsAlone` feature.
- **Southampton is the most common embarkation port:** 270 records, compared with 102 from Cherbourg and 46 from Queenstown.

These findings are descriptive of the supplied dataset. In particular, any finding based on `Survived` must be interpreted in light of the label limitation above.

## 📈 Interactive Dashboard

The Streamlit dashboard includes sidebar filters for:

- Passenger class
- Sex
- Port of embarkation
- Age range
- Travel status (all passengers, travelling alone, or travelling with family)

It displays KPI cards and four tabs:

### 1. Overview
- Labelled survival rate by passenger class
- Labelled outcome by sex
- Passenger count and labelled rate by embarkation port
- Correlation with the supplied `Survived` label

### 2. Demographics
- Age distribution by labelled outcome
- Labelled rate by age group
- Labelled rate by family size
- Extracted passenger titles

### 3. Class & Fare
- Fare distribution by passenger class using `Fare_capped`
- Age versus fare
- Labelled outcome by cabin availability
- Distribution of known deck letters

### 4. Insights
- Displays the main findings and prominently warns that the `Survived` field is not a reliable historical outcome label.

## ▶️ How to Run

Use Python in an environment where the project files are in the same folder.

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
```

### 2. Run the notebook

Open `titanic_analysis.ipynb` in Jupyter and run the cells in order. The notebook expects the raw dataset to be named `File_3.csv` and exports `titanic_cleaned.csv`. It also generates `kpis.json` and `eda_overview.png` when the relevant cells run.

```bash
jupyter notebook titanic_analysis.ipynb
```

### 3. Launch the interactive dashboard

Make sure `titanic_cleaned.csv` is in the same folder as `app_streamlit.py`, then run:

```bash
streamlit run app_streamlit.py
```

Streamlit will open the dashboard in your browser. Use the sidebar controls to filter the records; the KPIs and charts update for the selected subset.

## ⚠️ Notes & Limitations

- The notebook currently sets `RAW = "File_3.csv"`, while the uploaded raw file is named `File 3.csv`. Rename the raw file or change `RAW` to match its actual filename.
- The dashboard reads `titanic_cleaned.csv`, while the uploaded cleaned file is named `titanic_cleaned(2).csv`. Rename it or update the path in `app_streamlit.py`.
- The dashboard code expects the cleaned dataset to include the columns generated by the notebook.
- The supplied `Survived` values appear to be gender-based baseline labels. Use a dataset with verified historical outcomes if the goal is to analyze actual Titanic survival.

## ✅ Deliverables

- **Python analysis:** `titanic_analysis.ipynb`
- **Interactive dashboard:** `app_streamlit.py`
- **Cleaned dataset:** `titanic_cleaned.csv`
- **Raw dataset:** `File_3.csv`
- **Key KPIs and insights:** documented in this README and explored in the dashboard

---

*Built with Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit.*
