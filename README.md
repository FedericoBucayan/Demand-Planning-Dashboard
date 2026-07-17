# Demand Planning Dashboard

🔗 [Live Interactive Dashboard Demo](https://federicobucayan.github.io/Retail-Performance-Dashboard/)

An interactive demand planning and Forecast Value Add (FVA) dashboard that aggregates monthly forecast and sales databases, calculates forecasting accuracy metrics (WAPE, MAD, Bias %, Abs Error) dynamically, and displays category and product-level insights in a clean corporate visual interface.

## 🤖 Co-Created with AI (Vibe Coding Showcase)

### Transparency Statement
I built this entire project acting as the product manager and system coordinator in partnership with Google Antigravity (an agentic AI coding assistant).

Instead of writing the code line-by-line, I used natural language instructions ("vibe coding") to guide the AI to implement:
* **Single-Select Year Slicers**: One-click filter controls that instantly update all forecast accuracy KPIs, product portfolio matrices, trend lines, and table grids based on the selected year.
* **Product Portfolio Accuracy Matrix**: An interactive bubble chart mapping Cases Volume (Y-Axis) against Forecast Accuracy % (X-Axis), with bubble size representing forecast volume. Includes an interactive hover tooltip detailing Critical Adjustment, Monitor, and Success quadrants.
* **Granular Demand Metrics Matrix**: An interactive pivot table with collapsible and expandable headers for Soda Group and Water Group, dynamic search filters, and an Export to CSV function.
* **Forecast Alert Indicators**: Automated visual risk indicators representing planning performance:
  - 🟢 **Strong Performance** (Accuracy $\ge$ 85%): Safe, well-calibrated forecast profile.
  - 🟡 **Moderate Deviation** (Accuracy 70% to 85%): Under review.
  - 🔴 **Critical Exception** (Accuracy &lt; 70%): High error rate, requires immediate planning review.
* **Corporate Tailwind & Inter Styling**: Modern light-mode styling utilizing a sleek slate and white color scheme, high-contrast dark navy header strip, and clean teal accents with the global Inter typography.

This repository demonstrates the power of AI-assisted engineering and showcases how a retail and supply chain expert can orchestrate, test, and deploy a fully functional dashboard application from scratch.

---

## 🛠️ How It Works (The Pipeline)

1. **Spreadsheet Inputs**: The database consists of two core Excel files: `Forecasting_&_Actuals_Database.xlsx` (forecast vs sales logs) and `Reference_Formulas.xlsx` (mathematical logic).
2. **Database Aggregator**: Python loads the Excel records, performs data hygiene (stripping whitespaces, standardizing month formats), classifies product subgroups, and outputs compact data structures to `data.js`.
3. **Interactive Dashboard**: Launches a fully self-contained visual report (`index.html`) that runs offline in any browser.

## How to Update the Dashboard with New Data

If you update the Excel database with new sales or forecast records, you can refresh the dashboard in one of two ways:

### Method A: One-Click Update (Recommended)
Simply double-click the **`Update_Dashboard.bat`** file in the root folder. This will automatically:
1. Run the Python aggregator script.
2. Regenerate the `data.js` database.
3. Automatically launch the updated **`index.html`** in your default web browser.

### Method B: Manual Command Line Update
If you prefer running it manually from your terminal:
1. **Aggregate the spreadsheet data**:
   ```bash
   python build_dashboard.py
   ```
2. **Refresh the page**: Open or refresh **`index.html`** in your browser.

---

## 💻 Tech Stack

* **Backend/ETL**: Python 3, Pandas, Openpyxl.
* **Frontend**: HTML5, Vanilla JavaScript, Chart.js (v4), Tailwind CSS (v3/v4), Lucide Icons.

---

## 📂 Repository File Guide

* **`index.html`**: The main interactive visual dashboard. Open this to view the report.
* **`Update_Dashboard.bat`**: One-click batch script to compile the Excel workbook database and launch the report.
* **`Forecasting_&_Actuals_Database.xlsx`**: Excel database of forecast and actual sales records.
* **`README.md`**: Project documentation (this file).
* **`reference_material/`**: Directory containing backend, source, and visual reference assets:
  * **`build_dashboard.py`**: Python ETL script to aggregate and clean spreadsheet data.
  * **`data.js`**: Compiled JSON database loaded dynamically by the dashboard.
  * **`Reference_Formulas.xlsx`**: Excel reference workbook with mathematical formulas.
  * **`Profile_Pic.jpg`**: Creator profile picture.
  * **`dashboard_screenshot.png`**: Verified screenshot of the report dashboard.
  * **`Forecasting_Reference_*.jpeg`**: Reference mockup design files.

---
*Designed and Developed by Federico Bucayan | © 2026*
