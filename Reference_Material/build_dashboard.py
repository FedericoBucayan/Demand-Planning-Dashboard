import pandas as pd
import json
import math
import os

def build_data():
    # Determine the script directory and root directory dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    excel_path = os.path.join(project_root, "Forecasting_&_Actuals_Database.xlsx")
    
    if not os.path.exists(excel_path):
        excel_path = "Forecasting_&_Actuals_Database.xlsx" # Fallback to CWD
        
    df = pd.read_excel(excel_path, sheet_name="Database")
    
    # 1. Data Hygiene
    # Strip whitespace from string columns
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
    
    # 2. Inject Subcategory
    # The database contains only one Category 'Beverage'.
    # We will classify them into 'Water' and 'Soda' based on the product name for a richer visual dashboard.
    def get_subcategory(product):
        prod_lower = product.lower()
        if 'water' in prod_lower:
            return 'Water'
        elif 'coke' in prod_lower:
            return 'Soda'
        else:
            return 'Other'
            
    df['Subcategory'] = df['Product'].apply(get_subcategory)
    
    # Ensure Numeric fields
    df['Forecast'] = pd.to_numeric(df['Forecast'], errors='coerce').fillna(0).astype(int)
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce') # Leave as float to preserve NaNs (representing future/missing periods)
    
    # 3. Sort records in chronological and hierarchical order
    df['Month_Num'] = df['Month'].map(month_order).fillna(99)
    df = df.sort_values(by=['Year', 'Month_Num', 'Category', 'Subcategory', 'Product'])
    
    # Get lists of unique values for filters
    years = sorted(df['Year'].unique().tolist())
    months = sorted(df['Month'].unique().tolist(), key=lambda m: month_order.get(m, 99))
    categories = sorted(df['Category'].unique().tolist())
    subcategories = sorted(df['Subcategory'].unique().tolist())
    products = sorted(df['Product'].unique().tolist())
    
    # Prepare records
    records = []
    for _, row in df.iterrows():
        sales_val = row['Sales']
        # Convert float NaN to None (null in JSON)
        if pd.isna(sales_val) or math.isnan(sales_val):
            sales_val = None
        else:
            sales_val = float(sales_val)
            
        records.append({
            'category': row['Category'],
            'subcategory': row['Subcategory'],
            'product': row['Product'],
            'year': int(row['Year']),
            'month': row['Month'],
            'packagingUnit': row['Packaging Unit'],
            'forecast': int(row['Forecast']),
            'sales': sales_val
        })
        
    dashboard_data = {
        'years': years,
        'months': months,
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
        'records': records
    }
    
    # 4. Export to data.js
    output_path = os.path.join(script_dir, "data.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("/* Automated export from build_dashboard.py */\n")
        f.write("const DASHBOARD_DATA = ")
        json.dump(dashboard_data, f, indent=2)
        f.write(";\n")
        
    print(f"Data generation complete. Exported {len(records)} records to {output_path}")
    
if __name__ == "__main__":
    build_data()
