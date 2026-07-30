import os
import uuid

def generate_guid():
    return str(uuid.uuid4())

BASE_DIR = r"C:\Users\bucay\OneDrive\Documents\Fede\AI Test\Demand Planning"
MODEL_DIR = os.path.join(BASE_DIR, "Demand_Planning_Dashboard.SemanticModel", "definition")

def build_tmdl_model():
    tables_dir = os.path.join(MODEL_DIR, "tables")
    os.makedirs(tables_dir, exist_ok=True)

    # 1. Fact_Demand.tmdl
    fact_tmdl = f"""table Fact_Demand
	lineageTag: {generate_guid()}

	column Year
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Year

	column Month
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Month

	column Category
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Category

	column Product
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Product

	column Subcategory
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Subcategory

	column 'Packaging Unit'
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Packaging Unit

	column Forecast
		dataType: int64
		formatString: #,0
		lineageTag: {generate_guid()}
		summarizeBy: sum
		sourceColumn: Forecast

	column Sales
		dataType: double
		formatString: #,0
		lineageTag: {generate_guid()}
		summarizeBy: sum
		sourceColumn: Sales

	column MonthNum
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: MonthNum

	column Date
		dataType: dateTime
		formatString: yyyy-mm-dd
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Date

	column MonthYearKey
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: MonthYearKey

	partition Fact_Demand = m
		mode: import
		source =
			let
				Source = Excel.Workbook(File.Contents("C:\\Users\\bucay\\OneDrive\\Documents\\Fede\\AI Test\\Demand Planning\\Forecasting_&_Actuals_Database.xlsx"), null, true),
				Database_Sheet = Source{{[Item="Database",Kind="Sheet"]}}[Data],
				#"Promoted Headers" = Table.PromoteHeaders(Database_Sheet, [PromoteAllScalars=true]),
				#"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{ {{"Year", Int64.Type}}, {{"Month", type text}}, {{"Category", type text}}, {{"Product", type text}}, {{"Packaging Unit", type text}}, {{"Forecast", Int64.Type}}, {{"Sales", type number}} }}),
				#"Trimmed Text" = Table.TransformColumns(#"Changed Type", {{ {{"Month", Text.Trim}}, {{"Category", Text.Trim}}, {{"Product", Text.Trim}} }}),
				#"Upper Month" = Table.TransformColumns(#"Trimmed Text", {{ {{"Month", Text.Upper}} }}),
				#"Added Subcategory" = Table.AddColumn(#"Upper Month", "Subcategory", each if [Product] <> null and Text.Contains(Text.Lower(Text.From([Product])), "water") then "Water" else if [Product] <> null and Text.Contains(Text.Lower(Text.From([Product])), "coke") then "Soda" else "Other", type text),
				#"Added MonthNum" = Table.AddColumn(#"Added Subcategory", "MonthNum", each if [Month] = "JAN" then 1 else if [Month] = "FEB" then 2 else if [Month] = "MAR" then 3 else if [Month] = "APR" then 4 else if [Month] = "MAY" then 5 else if [Month] = "JUN" then 6 else if [Month] = "JUL" then 7 else if [Month] = "AUG" then 8 else if [Month] = "SEP" then 9 else if [Month] = "OCT" then 10 else if [Month] = "NOV" then 11 else if [Month] = "DEC" then 12 else 99, Int64.Type),
				#"Added Date" = Table.AddColumn(#"Added MonthNum", "Date", each #date([Year], [MonthNum], 1), type date),
				#"Added MonthYearKey" = Table.AddColumn(#"Added Date", "MonthYearKey", each [Year] * 100 + [MonthNum], Int64.Type),
				#"Filtered Blanks" = Table.SelectRows(#"Added MonthYearKey", each [Product] <> null and Text.Trim(Text.From([Product])) <> "")
			in
				#"Filtered Blanks"
"""
    with open(os.path.join(tables_dir, "Fact_Demand.tmdl"), "w", encoding="utf-8") as f:
        f.write(fact_tmdl)

    # 2. Dim_Product.tmdl
    dim_product_tmdl = f"""table Dim_Product
	lineageTag: {generate_guid()}

	column Product
		dataType: string
		isKey
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Product

	column Subcategory
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Subcategory

	column Category
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Category

	column 'Packaging Unit'
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Packaging Unit

	partition Dim_Product = m
		mode: import
		source =
			let
				Source = Excel.Workbook(File.Contents("C:\\Users\\bucay\\OneDrive\\Documents\\Fede\\AI Test\\Demand Planning\\Forecasting_&_Actuals_Database.xlsx"), null, true),
				Database_Sheet = Source{{[Item="Database",Kind="Sheet"]}}[Data],
				#"Promoted Headers" = Table.PromoteHeaders(Database_Sheet, [PromoteAllScalars=true]),
				#"Trimmed Text" = Table.TransformColumns(#"Promoted Headers", {{ {{"Category", Text.Trim}}, {{"Product", Text.Trim}} }}),
				#"Added Subcategory" = Table.AddColumn(#"Trimmed Text", "Subcategory", each if [Product] <> null and Text.Contains(Text.Lower(Text.From([Product])), "water") then "Water" else if [Product] <> null and Text.Contains(Text.Lower(Text.From([Product])), "coke") then "Soda" else "Other", type text),
				#"Select Columns" = Table.SelectColumns(#"Added Subcategory", {{"Product", "Subcategory", "Category", "Packaging Unit"}}),
				#"Distinct Products" = Table.Distinct(#"Select Columns"),
				#"Filtered Blanks" = Table.SelectRows(#"Distinct Products", each [Product] <> null and Text.Trim(Text.From([Product])) <> "")
			in
				#"Filtered Blanks"
"""
    with open(os.path.join(tables_dir, "Dim_Product.tmdl"), "w", encoding="utf-8") as f:
        f.write(dim_product_tmdl)

    # 3. Dim_Date.tmdl (spans 2020-2026 to cover all years: 2021, 2022, 2023, 2024!)
    dim_date_tmdl = f"""table Dim_Date
	lineageTag: {generate_guid()}
	dataCategory: Time

	column Date
		dataType: dateTime
		isKey
		formatString: yyyy-mm-dd
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Date

	column Year
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Year

	column Month
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: Month
		sortByColumn: MonthNum

	column MonthNum
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: MonthNum

	column YearMonth
		dataType: string
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: YearMonth

	column MonthYearKey
		dataType: int64
		formatString: 0
		lineageTag: {generate_guid()}
		summarizeBy: none
		sourceColumn: MonthYearKey

	partition Dim_Date = m
		mode: import
		source =
			let
				Source = List.Dates(#date(2020, 1, 1), 2556, #duration(1, 0, 0, 0)),
				#"Converted to Table" = Table.FromList(Source, Splitter.SplitByNothing(), {{"Date"}}, null, ExtraValues.Error),
				#"Changed Type" = Table.TransformColumnTypes(#"Converted to Table",{{ {{"Date", type date}} }}),
				#"Inserted Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
				#"Inserted MonthNum" = Table.AddColumn(#"Inserted Year", "MonthNum", each Date.Month([Date]), Int64.Type),
				#"Inserted MonthName" = Table.AddColumn(#"Inserted MonthNum", "MonthName", each Date.ToText([Date], "MMM"), type text),
				#"Upper Month" = Table.TransformColumns(#"Inserted MonthName", {{ {{"MonthName", Text.Upper}} }}),
				#"Renamed Month" = Table.RenameColumns(#"Upper Month", {{ {{"MonthName", "Month"}} }}),
				#"Inserted YearMonth" = Table.AddColumn(#"Renamed Month", "YearMonth", each Text.From([Year]) & "-" & [Month], type text),
				#"Inserted MonthYearKey" = Table.AddColumn(#"Inserted YearMonth", "MonthYearKey", each [Year] * 100 + [MonthNum], Int64.Type)
			in
				#"Inserted MonthYearKey"
"""
    with open(os.path.join(tables_dir, "Dim_Date.tmdl"), "w", encoding="utf-8") as f:
        f.write(dim_date_tmdl)

    # 4. _Measures.tmdl
    measures_tmdl = f"""table _Measures
	lineageTag: {generate_guid()}

	measure 'Total Sales' = SUM(Fact_Demand[Sales])
		formatString: #,0
		displayFolder: Volume Metrics
		lineageTag: {generate_guid()}

	measure 'Total Forecast' = SUM(Fact_Demand[Forecast])
		formatString: #,0
		displayFolder: Volume Metrics
		lineageTag: {generate_guid()}

	measure 'Total Forecast Historic' = CALCULATE([Total Forecast], NOT(ISBLANK(Fact_Demand[Sales])))
		formatString: #,0
		displayFolder: Volume Metrics
		lineageTag: {generate_guid()}

	measure 'Raw Error' = [Total Sales] - [Total Forecast Historic]
		formatString: #,0
		displayFolder: Error Metrics
		lineageTag: {generate_guid()}

	measure 'Abs Error' = SUMX(FILTER(Fact_Demand, NOT(ISBLANK(Fact_Demand[Sales]))), ABS(Fact_Demand[Sales] - Fact_Demand[Forecast]))
		formatString: #,0
		displayFolder: Error Metrics
		lineageTag: {generate_guid()}

	measure 'MAD' = AVERAGEX(FILTER(Fact_Demand, NOT(ISBLANK(Fact_Demand[Sales]))), ABS(Fact_Demand[Sales] - Fact_Demand[Forecast]))
		formatString: #,0.00
		displayFolder: Error Metrics
		lineageTag: {generate_guid()}

	measure 'Bias %' = DIVIDE([Total Forecast Historic] - [Total Sales], [Total Sales], 0)
		formatString: 0.00%
		displayFolder: Accuracy & Bias
		lineageTag: {generate_guid()}

	measure 'MAPE %' = ```
			VAR HistoricRows = FILTER(Fact_Demand, NOT(ISBLANK(Fact_Demand[Sales])))
			RETURN
				AVERAGEX(
					HistoricRows,
					IF(
						Fact_Demand[Sales] > 0,
						ABS(Fact_Demand[Sales] - Fact_Demand[Forecast]) / Fact_Demand[Sales],
						IF(Fact_Demand[Forecast] > 0, 1.0, 0.0)
					)
				)
		```
		formatString: 0.00%
		displayFolder: Accuracy & Bias
		lineageTag: {generate_guid()}

	measure 'Forecast Accuracy %' = ```
			VAR MapeVal = [MAPE %]
			RETURN IF(ISBLANK(MapeVal), BLANK(), MAX(0, 1 - MapeVal))
		```
		formatString: 0.00%
		displayFolder: Accuracy & Bias
		lineageTag: {generate_guid()}

	measure 'WAPE Accuracy %' = ```
			VAR SalesVal = [Total Sales]
			RETURN IF(SalesVal > 0, MAX(0, 1 - DIVIDE([Abs Error], SalesVal)), BLANK())
		```
		formatString: 0.00%
		displayFolder: Accuracy & Bias
		lineageTag: {generate_guid()}

	measure 'Error Color' = ```
			VAR ErrVal = [Raw Error]
			RETURN IF(ISBLANK(ErrVal), "#64748B", IF(ErrVal < 0, "#EF4444", IF(ErrVal > 0, "#10B981", "#64748B")))
		```
		displayFolder: Formatting Rules
		lineageTag: {generate_guid()}

	measure 'Accuracy Alert Color' = ```
			VAR AccVal = [Forecast Accuracy %]
			RETURN IF(ISBLANK(AccVal), "#64748B", IF(AccVal >= 0.85, "#10B981", IF(AccVal >= 0.70, "#B45309", "#EF4444")))
		```
		displayFolder: Formatting Rules
		lineageTag: {generate_guid()}

	measure 'Bias Color' = ```
			VAR BiasVal = [Bias %]
			RETURN IF(ISBLANK(BiasVal), "#64748B", IF(BiasVal > 0.02, "#EF4444", IF(BiasVal < -0.02, "#10B981", "#0891B2")))
		```
		displayFolder: Formatting Rules
		lineageTag: {generate_guid()}

	partition _Measures = m
		mode: import
		source =
			let
				Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				#"Changed Type" = Table.TransformColumnTypes(Source,{{ {{"Column1", type text}} }}),
				#"Removed Columns" = Table.RemoveColumns(#"Changed Type",{{"Column1"}})
			in
				#"Removed Columns"
"""
    with open(os.path.join(tables_dir, "_Measures.tmdl"), "w", encoding="utf-8") as f:
        f.write(measures_tmdl)

    # 5. relationships.tmdl
    rel_tmdl = f"""relationship Relationship_Product
	fromColumn: Fact_Demand.Product
	toColumn: Dim_Product.Product

relationship Relationship_Date
	fromColumn: Fact_Demand.Date
	toColumn: Dim_Date.Date
"""
    with open(os.path.join(MODEL_DIR, "relationships.tmdl"), "w", encoding="utf-8") as f:
        f.write(rel_tmdl)

    # 6. Update model.tmdl
    model_tmdl = """model Model
	culture: en-US
	defaultPowerBIDataSourceVersion: powerBI_V3
	sourceQueryCulture: en-US
	dataAccessOptions
		legacyRedirects
		returnErrorValuesAsNull

annotation __PBI_TimeIntelligenceEnabled = 0

annotation PBI_ProTooling = ["DevMode"]

ref table Fact_Demand
ref table Dim_Product
ref table Dim_Date
ref table _Measures

ref cultureInfo en-US
"""
    with open(os.path.join(MODEL_DIR, "model.tmdl"), "w", encoding="utf-8") as f:
        f.write(model_tmdl)

    print("Dim_Date updated to cover 2020-2026!")

if __name__ == "__main__":
    build_tmdl_model()
