# Demand Planning Dashboard

🌐 [Live Interactive Web App Demo](https://federicobucayan.github.io/Demand-Planning-Dashboard/) | 📊 [Power BI Project (.pbip)](https://github.com/federicobucayan/Demand-Planning-Dashboard/blob/main/Demand_Planning_Dashboard.pbip) | 📄 [Power BI PDF Report Export](https://github.com/federicobucayan/Demand-Planning-Dashboard/blob/main/Demand_Planning_Dashboard_PBI_PDF.pdf)

An end to end demand planning solution built across two complementary platforms: a live interactive web dashboard (index.html) and a native Power BI project (Demand_Planning_Dashboard.pbip).

This repository was designed specifically as a portfolio showcase for recruiters, hiring managers, and supply chain leaders.

---

## Executive Value Proposition for Recruiters and Hiring Managers

### 1. Demand Planning Expertise and Decision-Maker Mindset
First and foremost, this project demonstrates deep functional expertise in supply chain demand planning and quantitative performance analytics:
* **Core KPI Analysis**: Calculates and visualizes key planning metrics dynamically including Bias %, Abs Error / Abs Bias, MAPE %, WAPE, and MAD.
* **Variance and Exception Identification**: Isolates root causes of forecast deviations across category, subcategory, and SKU levels, highlighting critical over forecasting and under forecasting risks.
* **Decision Support Architecture**: Built from the perspective of an experienced supply chain practitioner and decision maker. The dashboard is engineered to translate raw demand logs into executive insights, facilitating proactive inventory management, safety stock calibration, and S&OP alignment.

### 2. AI-Powered Engineering and Digital Mindset (Co-Created with Google Antigravity)
Second, this repository showcases a forward thinking digital mindset and passion for modern technology:
* **Transparency Statement**: I built this entire project combining my expertise in supply chain planning, business data analytics and Power BI in partnership with Google Antigravity (an advanced agentic AI coding assistant).
* **Bridging Data Analytics and Software Engineering**: While I am highly proficient in data modeling, DAX calculations, and business intelligence, I leveraged agentic AI to bridge the gap into full stack software development by orchestrating Python ETL automation, web application design (HTML5/JS), and Power BI Developer Mode (.pbip TMDL/PBIR) structures.
* **AI Enthusiast and Early Adopter**: Demonstrates my eagerness to learn, master, and integrate cutting edge AI tools into daily workflows, bringing a curious, innovative, and digital first mindset to any progressive organization.

---

## Technical Framework and Power BI Architecture

The Power BI Project (.pbip) in this repository was constructed and programmatically validated using the **Power BI Modeling MCP Server** and the **skills-for-fabric** framework.

This architecture enforces developer mode best practices, establishing a clean Star Schema data model in TMDL format alongside modular PBIR visual container definitions.

### How Recruiters and Engineers Can Open and Inspect the Report:
1. Clone or download this repository:
   ```bash
   git clone https://github.com/federicobucayan/Demand-Planning-Dashboard.git
   ```
2. Double click **Demand_Planning_Dashboard.pbip** to launch the project directly in **Power BI Desktop** (or use **Launch_PowerBI.bat**).
3. All Star Schema tables (Fact_Demand, Dim_Product, Dim_Date), DAX measures (WAPE, MAD, MAPE %, Bias %), dropdown slicers, and visual cards will load automatically.
4. Alternatively, view the exported **[Demand_Planning_Dashboard_PBI_PDF.pdf](https://github.com/federicobucayan/Demand-Planning-Dashboard/blob/main/Demand_Planning_Dashboard_PBI_PDF.pdf)** file directly on GitHub for a quick visual overview.

---

## Key Dashboard Capabilities and Features

### 1. Forecast Bias Status and Thresholds
Automated classification of planning bias to identify inventory risk:
* 🔴 **Over-Forecast (Bias % > +2%)**: Forecast significantly exceeds actual sales, indicating a risk of excess inventory or working capital tie up.
* 🟢 **Under-Forecast (Bias % < -2%)**: Sales significantly exceed planned forecast, indicating a risk of stockouts or lost revenue.
* 🔵 **OK Status (-2% <= Bias % <= +2%)**: Forecast is accurately aligned with sales actuals.

### 2. Product Portfolio Accuracy Matrix Quadrants
An interactive bubble chart mapping Sales Cases Volume (Y-Axis) against Forecast Accuracy % (X-Axis), sized by Forecast Volume:
* 🔴 **Top-Left (High Sales, Low Accuracy)**: Critical Adjustment Zone. High volume, low predictability products. Focus planning adjustments here first for maximum impact.
* 🟡 **Bottom-Left (Low Sales, Low Accuracy)**: Monitor Zone. Low accuracy but low sales impact (medium priority).
* 🟢 **Top-Right (High Sales, High Accuracy)**: Success Zone. Highly predictable, high impact products (low risk).

### 3. Granular Demand Metrics Matrix and Alert Levels
An interactive pivot table with collapsible and expandable headers (Soda Group, Water Group), search filtering, and Export to CSV capability with automated risk indicators:
* 🟢 **Strong Performance (Accuracy >= 85%)**: Safe, well-calibrated forecast profile.
* 🟡 **Moderate Deviation (Accuracy 70% to 85%)**: Under review for potential adjustments.
* 🔴 **Critical Exception (Accuracy < 70%)**: High error rate, requires immediate planning review.
* ⚪ **Pending Data (Future periods)**: Actual sales values are not yet loaded.

---

## Tech Stack and Pipeline

* **Business Intelligence**: Power BI Desktop (PBIP format, TMDL Star Schema, DAX, Power Query M built with Power BI Modeling MCP Server and skills-for-fabric framework).
* **Web Application**: HTML5, Vanilla JavaScript, Chart.js (v4), Tailwind CSS (v3/v4), Lucide Icons.
* **Backend and Data Pipeline**: Python 3 (Pandas, Openpyxl) processing raw Excel databases (Forecasting_&_Actuals_Database.xlsx).

---

## Repository File Guide

* **Demand_Planning_Dashboard.pbip**: Power BI Project file (Developer Mode).
* **Demand_Planning_Dashboard_PBI_PDF.pdf**: Exported PDF version of the Power BI report for quick visual inspection.
* **Demand_Planning_Dashboard.SemanticModel/**: TMDL Star Schema model files (Fact_Demand, Dim_Product, Dim_Date, _Measures).
* **Demand_Planning_Dashboard.Report/**: PBIR report page layout and visual definitions.
* **Launch_PowerBI.bat**: Batch script to clear background locks and open the Power BI report smoothly.
* **index.html**: Interactive web dashboard. Open to view the web report offline.
* **Update_Dashboard.bat**: Batch script to compile spreadsheet databases and launch the web dashboard.
* **Forecasting_&_Actuals_Database.xlsx**: Base Excel database of forecast logs and actual sales records.
* **scripts/**: Automation scripts for model generation, report layout creation, and metric verification.
* **README.md**: Project documentation (this file).

---
Designed and Developed by Federico Bucayan | Copyright 2026
