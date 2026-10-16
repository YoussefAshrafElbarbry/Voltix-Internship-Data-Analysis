# 🏙️ NYC Airbnb Market Analysis | Voltix Task 12

An end-to-end data analysis project exploring Airbnb listings across New York City using **Python, Pandas, and Power BI**. The project focuses on listing distribution, pricing patterns, availability, reviews, and neighborhood-level insights.

---

## 📊 Dashboard Preview

### 1. NYC Airbnb Market Overview

![NYC Airbnb Market Overview](Market%20Overview.png)

This page provides a market-level view of NYC Airbnb listings, including:
- Total listings, average price, average availability, total reviews, and estimated occupancy rate.
- Listing distribution across boroughs.
- Top 10 neighborhoods by listing count.
- Geographic distribution of listings across NYC.
- Average listed price comparison between boroughs.

### 2. NYC Airbnb Pricing & Performance

![NYC Airbnb Pricing and Performance](Pricing%20%26%20Performance.png)

This page focuses on pricing and listing performance, including:
- Listings with more than 50 reviews (used as the project's active-listing proxy).
- Average price and average availability.
- Estimated annual revenue proxy and estimated occupancy rate.
- Average availability by room type.
- Distribution of listings by price tier.
- Average price by last-review date.
- Average price by borough and host-level summary table.

---

## 🎯 Project Objectives

- Understand listing distribution across NYC boroughs and neighborhoods.
- Compare average listed prices across boroughs.
- Analyze availability patterns by room type.
- Explore Budget, Standard, and Luxury price tiers.
- Identify business insights for further market analysis.
- Present findings through an interactive Power BI dashboard.

## 🧰 Tools & Technologies

- **Python** — data cleaning and exploratory data analysis.
- **Pandas** — data manipulation and analysis.
- **Power BI** — interactive dashboard and visual storytelling.
- **CSV** — cleaned dataset format.

## 🧹 Data Preparation

The workflow includes:
- Standardizing text columns and removing embedded line breaks and excess whitespace.
- Parsing `last_review` as a date.
- Handling missing review-related values where appropriate.
- Creating analytical flags for zero-price listings and IQR-based outliers in `price` and `minimum_nights`.
- Retaining outlier flags for investigation rather than automatically removing all extreme values.

**Dataset:** Airbnb NYC 2019 listings dataset.

- Original dataset: **48,895 rows and 16 columns**.
- Cleaned analysis table: **48,895 rows and 19 columns**, including additional analytical flags.

## 📌 Key Metrics

| Metric | Result | Interpretation |
|---|---:|---|
| Total Listings | 48,895 | Number of listing records in the dataset |
| Average Price | $152.72 | Mean listed price; not a confirmed transaction price |
| Average Availability | 112.78 days | Average availability in the 365-day availability field |
| Total Reviews | 1,138,005 | Sum of listing review counts |
| Estimated Occupancy Rate | 69.10% | `(365 - Average Availability) / 365`; estimate only |
| Estimated Annual Revenue | ~2bn (dashboard display) | Price-and-availability proxy, not verified revenue |

> **Important:** Occupancy and revenue are estimates based on listing availability and price. Unavailable dates may be blocked rather than booked, so these measures must not be interpreted as confirmed bookings or actual revenue.

## 💡 Business Insights

1. **Manhattan has the highest average listed price.** The dashboard shows approximately **$211.79** in Manhattan, noticeably above the other boroughs.
2. **Budget and Standard listings dominate.** Under the project's price-tier rules, Budget listings represent about **44.74%**, Standard about **48.39%**, and Luxury about **6.87%**. Budget and Standard together account for about **93.13%** of listings.
3. **Listing supply is concentrated in a few neighborhoods.** Williamsburg, Bedford-Stuyvesant, and Harlem lead the displayed Top 10 chart. These areas are useful candidates for deeper comparisons of price, room type, and availability.
4. **Availability differs by room type.** Shared rooms show higher average availability than entire homes/apartments and private rooms in the dashboard. Availability alone does not prove lower demand or lower occupancy.
5. **Reviews are not revenue.** Review counts provide context about guest activity but do not directly measure bookings, income, or current listing activity.
6. **The review-date line chart is not a historical price series.** It groups listings by their last-review date and should not be interpreted as proof of how prices changed over time.

## ⚠️ Limitations

- The dataset represents **2019**, not the current Airbnb market.
- Listing price is not necessarily the price paid in a completed booking.
- The dataset does not verify booked nights or realized revenue.
- The dashboard's `Active Listings` measure is based on listings with more than 50 reviews; it does not confirm current activity.
- Listings without a valid `last_review` date are not represented in the date-based trend.

## 📁 Suggested Repository Structure

```text
NYC-Airbnb-Market-Analysis/
├── README.md
├── AB_NYC_2019.csv
├── AB_NYC_2019_Cleaned.csv
├── Airbnb_NYC_Final_Analysis.ipynb
├── NYC_Airbnb_Final_Report.pdf
├── Market Overview.png
├── Pricing & Performance.png
└── Airbnb_NYC_Dashboard.pbix
```

> Keep the image filenames exactly as shown above so the Markdown previews work on GitHub. Update notebook and PBIX filenames in the structure if yours differ.

## 📄 Final Report

The report documents the methodology, key findings, business insights, recommendations, and limitations.

**File:** `NYC_Airbnb_Final_Report.pdf`

## 🚀 Conclusion

This project highlights geographic differences in listing prices, a market mix dominated by Budget and Standard listings, and concentration of supply in several NYC neighborhoods. The dashboard enables interactive exploration while the limitations above help ensure estimated occupancy and revenue are interpreted carefully.

---

**Project:** Voltix Internship — Task 12  
**Domain:** Data Analysis & Business Intelligence  
**Tools:** Python, Pandas, Power BI
