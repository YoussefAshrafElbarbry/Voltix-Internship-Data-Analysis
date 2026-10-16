# Task 1 — Basic Sales Data Analysis

## Project Overview
This project analyzes sales transactions from the EzzSteel dataset using Python and Pandas. The goal is to clean the data, calculate key sales metrics, visualize sales performance, and extract business insights.

## Objectives
- Clean missing, duplicate, and invalid data.
- Check and correct data types.
- Calculate total sales and total profit.
- Identify the top-performing category, product, region, and month.
- Create visualizations and summarize key findings.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Dataset
The analysis uses the `Sales_Transactions` sheet from `EzzSteel_Full_Dataset.xlsx`. The original Excel workbook is included with the project.

## Data Cleaning
The notebook covers:
- Checking missing values and duplicate records.
- Converting `Invoice_Date` to datetime.
- Converting `Revenue_EGP` to numeric.
- Correcting quantity values affected by a kilograms-to-tons unit mix-up.
- Filling missing quantities using revenue and unit price where applicable.
- Handling negative quantity records.
- Correcting invalid discount values, such as `150` entered instead of `1.5`.
- Validating the cleaned dataset.

## Key Results
- **Total Sales:** 49,646,540,830.00 EGP
- **Top Product Category:** Long Steel
- **Top-Selling Product (Steel Grade):** B500C — 6,486,900,589.00 EGP in sales
- **Top Region:** Qalyubia — 3,888,339,007.00 EGP in sales
- **Best Month:** September 2023 — 2,234,642,872.00 EGP in sales
- **Total Profit:** See the final results section in the notebook.

## Business Insights
1. Long Steel generated the highest sales among the analyzed product categories.
2. B500C was the top-selling steel grade, generating approximately 6.49 billion EGP.
3. Qalyubia was the highest-performing region, with approximately 3.89 billion EGP in sales.
4. September 2023 recorded the highest monthly sales, reaching approximately 2.23 billion EGP.
5. Total sales reached approximately 49.65 billion EGP across the analyzed transactions.

## Visualizations
The `Chart` folder contains:
- Sales by Product Category
- Sales Over Time
- Top 10 Products by Sales
- Sales by Region

## Project Structure
```text
Task_1_Sales_Analysis_Python/
├── Sales_Data_Analysis.ipynb
├── EzzSteel_Full_Dataset.xlsx
├── README.md
└── Chart/
    ├── Sales_by_Category.png
    ├── Sales_Over_Time.png
    ├── Top_10_Products.png
    └── Sales_by_Region.png
```

## How to Run
1. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib openpyxl
   ```
2. Open `Sales_Data_Analysis.ipynb` in Jupyter Notebook or JupyterLab.
3. Keep `EzzSteel_Full_Dataset.xlsx` in the same folder as the notebook.
4. Run the notebook cells from top to bottom.

## Notes
- Profit is taken from the workbook's financial sheet because `Sales_Transactions` does not contain a direct profit column.
- The regional analysis uses `Governorate`; placeholder values such as `-` or `Unknown` should not be treated as actual regions.
