# Demand Planning Dashboard

🌐 [Live Interactive Web App Demo](https://federicobucayan.github.io/Demand-Planning-Dashboard/) | 📊 [Power BI Project (`.pbip`)](https://github.com/federicobucayan/Demand-Planning-Dashboard/blob/main/Demand_Planning_Dashboard.pbip)

An end-to-end demand planning solution built across two complementary platforms: a **live interactive web dashboard (`index.html`)** and a **native Power BI project (`Demand_Planning_Dashboard.pbip`)**. 

This repository was designed specifically as a portfolio showcase for recruiters, hiring managers, and supply chain leaders.

---

## 🎯 Executive Value Proposition (For Recruiters & Hiring Managers)

### 1. 📈 Demand Planning Expertise & Decision-Maker Mindset
First and foremost, this project demonstrates deep functional expertise in supply chain demand planning and quantitative performance analytics:
* **Core KPI Analysis**: Calculates and visualizes key planning metrics dynamically—including **Bias %**, **Abs Error / Abs Bias**, **MAPE %**, **WAPE**, and **MAD**.
* **Variance & Exception Identification**: Isolates root causes of forecast deviations across category, subcategory, and SKU levels, highlighting critical over-forecasting and under-forecasting risks.
* **Decision-Support Architecture**: Built from the perspective of an experienced supply chain practitioner and decision-maker. The dashboard is engineered to translate raw demand logs into executive insights, facilitating proactive inventory management, safety stock calibration, and S&OP alignment.

### 2. 🤖 AI-Powered Engineering & Digital Mindset (Co-Created with Google Antigravity)
Second, this repository showcases a forward-thinking digital mindset and passion for modern technology:
* **Transparency Statement**: I built this entire project combining my domain expertise in supply chain, business data analytics, Power BI, Power Query, Power Pivot, and DAX in partnership with **Google Antigravity** (an advanced agentic AI coding assistant).
* **Bridging Data Analytics & Software Engineering**: While I am highly proficient in data modeling, DAX calculations, and business intelligence, I leveraged agentic AI to bridge the gap into full-stack software development—orchestrating Python ETL automation, web application design (HTML5/JS), and Power BI Developer Mode (`.pbip` TMDL/PBIR) structures.
* **AI Enthusiast & Early Adopter**: Demonstrates my eagerness to learn, master, and integrate cutting-edge AI tools into daily workflows—bringing a curious, innovative, and digital-first mindset to any progressive organization.

---

## 🛠️ Key Dashboard Capabilities & Features

### 1. Forecast Bias Status & Thresholds
Automated classification of planning bias to identify inventory risk:
- 🔴 **Over-Forecast (`Bias % > +2%`)**: Forecast significantly exceeds actual sales (risk of excess inventory / working capital tie-up).
- 🟢 **Under-Forecast (`Bias % < -2%`)**: Sales significantly exceed planned forecast (risk of stockouts / lost revenue).
- 🔵 **OK Status (`-2% <= Bias % <= +2%`)**: Forecast is accurately aligned with sales actuals.

### 2. Product Portfolio Accuracy Matrix Quadrants
An interactive bubble chart mapping Sales Cases Volume (Y-Axis) against Forecast Accuracy % (X-Axis), sized by Forecast Volume:
- 🔴 **Top-Left (High Sales, Low Accuracy)**: **Critical Adjustment Zone**. High-volume, low-predictability products. Focus planning adjustments here first for maximum impact.
- 🟡 **Bottom-Left (Low Sales, Low Accuracy)**: **Monitor Zone**. Low accuracy but low sales impact (medium priority).
- 🟢 **Top-Right (High Sales, High Accuracy)**: **Success Zone**. Highly predictable, high-impact products (low risk).

### 3. Granular Demand Metrics Matrix & Alert Levels
An interactive pivot table with collapsible/expandable headers (`Soda Group`, `Water Group`), search filtering, and Export to CSV capability with automated risk indicators:
- 🟢 **Strong Performance** ($\text{Accuracy} \ge 85\%$): Safe, well-calibrated forecast profile.
- 🟡 **Moderate Deviation** ($\text{Accuracy } 70\% \text{ to } 85\%$): Under review for potential adjustments.
- 🔴 **Critical Exception** ($\text{Accuracy} < 70\%$): High error rate, requires immediate planning review.
- ⚪ **Pending Data** (Future periods): Actual sales values are not yet loaded.

---

## 📊 Power BI Project (`Demand_Planning_Dashboard.pbip`)

This project includes a full **Power BI Project (`Demand_Planning_Dashboard.pbip`)** developed using Microsoft's open Developer Mode format (TMDL + PBIR).

### How Recruiters & Engineers Can Open & Inspect the Report:
1. Clone or download this repository:
   ```bash
   git clone https://github.com/federicobucayan/Demand-Planning-Dashboard.git
   ```
2. Double-click **`Demand_Planning_Dashboard.pbip`** to launch the project directly in **Power BI Desktop**.
3. All Star Schema tables (`Fact_Demand`, `Dim_Product`, `Dim_Date`), DAX measures (`WAPE`, `MAD`, `MAPE %`, `Bias %`), dropdown slicers, and visual cards will load automatically.

---

## 💻 Tech Stack & Pipeline

* **Business Intelligence**: Power BI Desktop (PBIP format, TMDL Star Schema, DAX, Power Query M).
* **Web Application**: HTML5, Vanilla JavaScript, Chart.js (v4), Tailwind CSS (v3/v4), Lucide Icons.
* **Backend & Data Pipeline**: Python 3 (Pandas, Openpyxl) processing raw Excel databases (`Forecasting_&_Actuals_Database.xlsx`).

---

## 📂 Repository File Guide

* **`Demand_Planning_Dashboard.pbip`**: Power BI Project file (Developer Mode).
* **`Demand_Planning_Dashboard.SemanticModel/`**: TMDL Star Schema model files (`Fact_Demand`, `Dim_Product`, `Dim_Date`, `_Measures`).
* **`Demand_Planning_Dashboard.Report/`**: PBIR report page layout and visual definitions.
* **`index.html`**: Interactive web dashboard. Open to view the web report offline.
* **`Update_Dashboard.bat`**: Batch script to compile spreadsheet databases and launch the web dashboard.
* **`Forecasting_&_Actuals_Database.xlsx`**: Base Excel database of forecast logs and actual sales records.
* **`README.md`**: Project documentation (this file).

---
*Designed and Developed by Federico Bucayan | © 2026*
