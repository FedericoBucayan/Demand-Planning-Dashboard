# Retail Performance Dashboard

🌐 [Live Interactive Web App Demo](https://federicobucayan.github.io/Retail-Performance-Dashboard/) | 📊 [Power BI Project (.pbip)](./Retail_Performance_Dashboard.pbip) | 📄 [Power BI PDF Report Export](./Retail_Performance_Dashboard_PBI_PDF.pdf)

A comprehensive retail analytics solution delivered through two parallel enterprise platforms: a live interactive web dashboard (`index.html`) and a native Power BI Project (`Retail_Performance_Dashboard.pbip`). The solution aggregates multiyear sales spreadsheets, calculates commercial KPIs dynamically, and displays store, category, and product level insights in a clean corporate interface.

This repository was designed specifically as a portfolio showcase for recruiters, hiring managers, and retail industry leaders.

---

## Executive Value Proposition (For Recruiters & Hiring Managers)

### 1. Retail Analytics & Commercial Planning Expertise
First and foremost, this project demonstrates deep functional expertise in retail commercial analytics and performance measurement:
* **Core KPI Analysis**: Calculates and visualizes key retail planning metrics dynamically including Net Sales (NS), Net Quantity (NQ), Year over Year (YoY) Growth, Average Selling Price (ASP), Standard Margin % (SM%), Conversion Rate % (CR%), Units Per Transaction (UPT), Average Transaction Value (ATV), and Full Price Mix %.
* **Multi-Dimensional Breakdown**: Analyzes commercial performance across stores, product categories, merchandise divisions, gender demographics, and product groups with full YoY comparison at every level.
* **Decision-Support Architecture**: Built from the perspective of an experienced retail planning practitioner and commercial decision-maker. The dashboard is engineered to translate raw sales databases into actionable commercial insights, facilitating strategic decisions around product assortment, channel performance, markdown strategy, and inventory management.

### 2. AI-Powered Engineering & Digital Mindset (Co-Created with Google Antigravity)
Second, this repository showcases a forward-thinking digital mindset and passion for modern technology:
* **Transparency Statement**: I built this entire project combining my expertise in retail planning and commercial analytics in partnership with Google Antigravity (an advanced agentic AI coding assistant).
* **Enterprise Power BI PBIP & Fabric Integration**: The Power BI Project (`Retail_Performance_Dashboard.pbip`) was programmatically authored using the Power BI Modeling MCP Server (`powerbi-modeling-mcp`) and Microsoft's `skills-for-fabric` framework. The semantic model TMDL schema and PBIR report visual definitions were systematically created, compiled, and verified through programmatic MCP tooling.
* **Bridging Data Analytics & Software Engineering**: While I am highly proficient in commercial KPI design, spreadsheet database management, and business intelligence, I leveraged agentic AI to bridge the gap into full stack software development by orchestrating Python ETL automation, web application design, and an automated build and validation pipeline.
* **AI Enthusiast & Early Adopter**: Demonstrates my eagerness to learn, master, and integrate cutting edge AI tools into daily workflows, bringing a curious, innovative, and digital-first mindset to any progressive organization.

---

## Key Dashboard Capabilities and Features

### 1. YoY Performance Comparison Matrix
A full-page comparison matrix showing current year vs. prior year performance per store and in total, across all core KPIs (NS, NQ, ASP, SM%, Traffic, Transactions, CR%, ATV, UPT, FP Mix%). All YoY movements are color-coded with directional badges (▲/▼).

### 2. Sales Monthly Performance Trend
An interactive line chart overlaying current year vs. prior year monthly sales or quantity with a Sales ($) / Qty (Units) toggle and a custom multi-month checkbox filter including seasonal (SS, FW) and quarterly (Q1 to Q4) quick-select shortcuts.

### 3. Categories / Divisions / Gender Comparison Chart
An interactive bar chart with a dimension toggle (Category, Division, Gender) that dynamically regroups and redraws the chart with per-bar YoY growth labels and a detailed tooltip showing both NS YoY Growth % and NQ YoY Growth % on hover.

### 4. Share of Business Doughnut Charts
Three side by side doughnut charts showing the percentage contribution to total sales or quantity by Categories, Divisions, and Gender with a Sales / Qty metric toggle.

### 5. Product Group Benchmarks Table
A sortable breakdown table by Category, Division, or Gender segment with NS, YoY Sales growth, NQ, YoY Qty growth, and Margin % dynamically switching between breakdown dimensions.

### 6. Best Selling Product Groups Ranking
A dynamic ranking table of all product groups sortable by Net Sales or Net Quantity, displaying NS, Sales YoY Growth, NQ, Qty YoY Growth, and Margin % with color-coded growth badges.

---

## Tech Stack & Architecture

* **Power BI Fabric Architecture**: Built as a developer-native Power BI Project (`Retail_Performance_Dashboard.pbip`) powered by TMDL definition files and PBIR visual schemas, authored using the Power BI Modeling MCP Server (`powerbi-modeling-mcp`) and Microsoft `skills-for-fabric` framework.
* **Backend / ETL Pipeline**: Python 3 (Pandas, Openpyxl) aggregating raw Excel databases and compiling structured JSON data arrays.
* **Web Application**: HTML5, Vanilla JavaScript, Chart.js (v4), Chart.js Datalabels Plugin (v2), Vanilla CSS design system.
* **Build Automation**: Automated batch script running data preparation, compilation, schema validation checks, and visual execution in a single click.

---

## Repository File Guide

* **`Retail_Performance_Dashboard.pbip`**: [Power BI Project File (.pbip)](./Retail_Performance_Dashboard.pbip) — Enterprise Power BI Project definition, containing TMDL Semantic Model definition files and PBIR visual report components.
* **`Retail_Performance_Dashboard_PBI_PDF.pdf`**: [Power BI Dashboard PDF](./Retail_Performance_Dashboard_PBI_PDF.pdf) — Exported high-resolution PDF snapshot of the Power BI report.
* **`index.html`**: [Live Interactive Web Dashboard](https://federicobucayan.github.io/Retail-Performance-Dashboard/) — The main compiled interactive web visual dashboard. Open this to view the web report.
* **`Refresh_Retail_Visual_Report.bat`**: Single click batch script to aggregate spreadsheet data, compile the dashboard layout, run validation, and launch the report.
* **`RET_KPI_Sales_Database.xlsx`**: Store level KPI spreadsheet database.
* **`RET_Product_Sales_Database.xlsx`**: Product transaction level spreadsheet database.
* **`README.md`**: Project documentation (this file).

---
*Designed and Developed by Federico Bucayan | © 2026*
