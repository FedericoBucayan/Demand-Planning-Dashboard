import pandas as pd
import json
import os

def build_data():
    # Determine the script directory and root directory dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    excel_path = os.path.join(project_root, "Forecasting_&_Actuals_Database.xlsx")

    if not os.path.exists(excel_path):
        excel_path = "Forecasting_&_Actuals_Database.xlsx"  # Fallback to CWD

    df = pd.read_excel(excel_path, sheet_name="Database")

    # 1. Data Hygiene — strip whitespace from string columns
    string_cols = ['Category', 'Product', 'Month', 'Packaging Unit']
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Standardize Month names to uppercase
    df['Month'] = df['Month'].str.upper()

    # Sort order helper for months
    month_order = {
        'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
        'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
    }

    # 2. Inject Subcategory based on product name
    def get_subcategory(product):
        prod_lower = product.lower()
        if 'water' in prod_lower:
            return 'Water'
        elif 'coke' in prod_lower:
            return 'Soda'
        else:
            return 'Other'

    df['Subcategory'] = df['Product'].apply(get_subcategory)

    # Ensure numeric fields
    df['Forecast'] = pd.to_numeric(df['Forecast'], errors='coerce').fillna(0).astype(int)
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    # 3. Sort records in chronological and hierarchical order
    df['Month_Num'] = df['Month'].map(month_order).fillna(99)
    df = df.sort_values(by=['Year', 'Month_Num', 'Category', 'Subcategory', 'Product'])

    # Get lists of unique values for filters
    years = sorted(df['Year'].unique().tolist())
    months = sorted(df['Month'].unique().tolist(), key=lambda m: month_order.get(m, 99))
    categories = sorted(df['Category'].unique().tolist())
    subcategories = sorted(df['Subcategory'].unique().tolist())
    products = sorted(df['Product'].unique().tolist())

    # 4. Prepare records
    # Optimizations applied:
    #   - Use to_dict('records') instead of iterrows() for 10-50x faster iteration
    #   - Drop 'packagingUnit' (unused in the dashboard JS engine)
    #   - Drop 'category' from each row (stored once at top-level above)
    #   - Use pd.isna() only (math.isnan is redundant)
    records = []
    for row in df.to_dict('records'):
        sales_val = row['Sales']
        records.append({
            'category':    row['Category'],
            'subcategory': row['Subcategory'],
            'product':     row['Product'],
            'year':        int(row['Year']),
            'month':       row['Month'],
            'forecast':    int(row['Forecast']),
            'sales':       None if pd.isna(sales_val) else float(sales_val)
        })

    dashboard_data = {
        'years':         years,
        'months':        months,
        'categories':    categories,
        'subcategories': subcategories,
        'products':      products,
        'records':       records
    }

    # 5. Export to data.js — compact JSON (no indent) saves ~35-40 KB
    output_path = os.path.join(script_dir, "data.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("/* Automated export from build_dashboard.py */\n")
        f.write("const DASHBOARD_DATA = ")
        json.dump(dashboard_data, f, separators=(',', ':'))
        f.write(";\n")

    print(f"Data generation complete. Exported {len(records)} records to {output_path}")

if __name__ == "__main__":
    build_data()
