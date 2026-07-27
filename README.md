# Demand Planning & Intelligence Dashboard

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
* **Agentic AI Collaboration**: Both the web application and the Power BI Developer Project (`.pbip` Star Schema TMDL model and DAX calculations) were co-created in partnership with **Google Antigravity** (an advanced agentic AI coding assistant).
* **AI Enthusiast & Early Adopter**: Demonstrates Federico's eagerness to learn, master, and integrate cutting-edge AI tools into daily workflows—bringing a curious, innovative, and digital-first mindset to any progressive organization.

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

## 🛠️ Key Dashboard Capabilities & Features

* **Single-Select & Dropdown Slicers**: One-click filter controls (`Year`, `Category`, `Subcategory`, `Product`, `Month`) that update all KPIs, portfolio matrices, trend lines, and data grids.
* **Product Portfolio Accuracy Matrix**: An interactive bubble chart mapping Cases Volume (Y-Axis) against Forecast Accuracy % (X-Axis), with bubble size representing forecast volume. Includes hover tooltips for risk quadrant analysis.
* **Granular Demand Metrics Matrix**: An interactive pivot table with collapsible/expandable headers (`Soda Group`, `Water Group`), search filtering, and Export to CSV capability.
* **Automated Forecast Risk Alerts**: Visual indicators representing planning performance:
  - 🟢 **Strong Performance** ($\ge 85\%$ Accuracy): Well-calibrated forecast profile.
  - 🟡 **Moderate Deviation** ($70\% \text{ to } 85\%$ Accuracy): Under review.
  - 🔴 **Critical Exception** ($< 70\%$ Accuracy): High error rate, requires immediate planning review.

---

## 💻 Tech Stack & Pipeline

* **Business Intelligence**: Power BI Desktop (PBIP format, TMDL Star Schema, DAX).
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
