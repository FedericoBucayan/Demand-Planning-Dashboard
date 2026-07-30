import pandas as pd
import numpy as np

excel_path = "Forecasting_&_Actuals_Database.xlsx"
df = pd.read_excel(excel_path, sheet_name="Database")

df['Category'] = df['Category'].astype(str).str.strip()
df['Product'] = df['Product'].astype(str).str.strip()
df['Month'] = df['Month'].astype(str).str.strip().str.upper()

def get_subcategory(product):
    prod_lower = product.lower()
    if 'water' in prod_lower:
        return 'Water'
    elif 'coke' in prod_lower:
        return 'Soda'
    else:
        return 'Other'

df['Subcategory'] = df['Product'].apply(get_subcategory)
df['Forecast'] = pd.to_numeric(df['Forecast'], errors='coerce').fillna(0).astype(int)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

historic = df[df['Sales'].notna()].copy()
future = df[df['Sales'].isna()].copy()

sales_sum = historic['Sales'].sum()
forecast_all = df['Forecast'].sum()
forecast_historic = historic['Forecast'].sum()

raw_error_sum = sales_sum - forecast_historic
abs_error_sum = np.abs(historic['Sales'] - historic['Forecast']).sum()

historic['APE'] = np.where(
    historic['Sales'] > 0,
    np.abs(historic['Sales'] - historic['Forecast']) / historic['Sales'],
    np.where(historic['Forecast'] > 0, 1.0, 0.0)
)

mape = historic['APE'].mean()
accuracy_mape = max(0, 1 - mape)
mad = abs_error_sum / len(historic)
bias = (forecast_historic - sales_sum) / sales_sum if sales_sum > 0 else 0
wape_accuracy = max(0, 1 - (abs_error_sum / sales_sum)) if sales_sum > 0 else 0

print("=== VERIFICATION OF MATHEMATICAL BASELINE METRICS ===")
print(f"Total Forecast (All):        {forecast_all:,.0f}")
print(f"Total Forecast (Historic):   {forecast_historic:,.0f}")
print(f"Total Sales:                 {sales_sum:,.0f}")
print(f"Raw Error:                   {raw_error_sum:,.0f}")
print(f"Abs Error:                   {abs_error_sum:,.0f}")
print(f"MAD:                         {mad:,.2f}")
print(f"Bias %:                      {bias*100:.2f}%")
print(f"MAPE %:                      {mape*100:.2f}%")
print(f"Forecast Accuracy % (MAPE): {accuracy_mape*100:.2f}%")
print(f"WAPE Accuracy %:            {wape_accuracy*100:.2f}%")
print("====================================================")
