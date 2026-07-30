import os
import uuid
import json

BASE_DIR = r"C:\Users\bucay\OneDrive\Documents\Fede\AI Test\Demand Planning"
REPORT_DIR = os.path.join(BASE_DIR, "Demand_Planning_Dashboard.Report", "definition")
PAGE_DIR = os.path.join(REPORT_DIR, "pages", "fe675277dec6b24d23ad")
THEME_DIR = os.path.join(BASE_DIR, "Demand_Planning_Dashboard.Report", "StaticResources", "RegisteredResources")

def build_custom_theme():
    os.makedirs(THEME_DIR, exist_ok=True)
    theme_data = {
        "name": "DemandPlanningTheme",
        "dataColors": [
            "#064E3B", # Forest Green (Sales)
            "#C5A880", # Warm Bronze/Tan (Forecast)
            "#1E88E5", # Electric Blue (Header / Accent)
            "#EF4444", # Crimson Red (Over Forecast / Risk)
            "#10B981", # Emerald Green (Strong Performance)
            "#B45309", # Dark Amber (Moderate Exception)
            "#0F172A", # Slate Header
            "#64748B"  # Muted Slate
        ],
        "background": "#F1F5F9",
        "foreground": "#0F172A",
        "tableAccent": "#0891B2",
        "visualStyles": {
            "*": {
                "*": {
                    "background": [{"color": {"solid": {"color": "#FFFFFF"}}}],
                    "border": [{"show": True, "color": {"solid": {"color": "#CBD5E1"}}, "radius": 8}],
                    "dropShadow": [{"show": True, "color": {"solid": {"color": "#0000001A"}}, "position": "Outer", "preset": "BottomRight"}]
                }
            },
            "page": {
                "*": {
                    "background": [{"color": {"solid": {"color": "#F1F5F9"}}, "transparency": 0}]
                }
            },
            "slicer": {
                "*": {
                    "general": [
                        {
                            "properties": {
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Dropdown'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
    with open(os.path.join(THEME_DIR, "DemandTheme.json"), "w", encoding="utf-8") as f:
        json.dump(theme_data, f, indent=2)
    print("DemandTheme.json custom theme written successfully!")

def create_visual_json(name, x, y, width, height, visual_type, query_dict=None, objects_dict=None, container_objects_dict=None):
    vis_dir = os.path.join(PAGE_DIR, "visuals", name)
    os.makedirs(vis_dir, exist_ok=True)

    if query_dict is None:
        query_dict = {"queryState": {}}
    elif "queryState" not in query_dict:
        query_dict["queryState"] = {}

    vis_data = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.7.0/schema.json",
        "name": name,
        "position": {
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "z": 1000
        },
        "visual": {
            "visualType": visual_type,
            "query": query_dict,
            "objects": objects_dict or {},
            "visualContainerObjects": container_objects_dict or {}
        }
    }

    with open(os.path.join(vis_dir, "visual.json"), "w", encoding="utf-8") as f:
        json.dump(vis_data, f, indent=2)

def build_report_visuals():
    build_custom_theme()

    # Update page.json
    page_json_path = os.path.join(PAGE_DIR, "page.json")
    page_data = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json",
        "name": "fe675277dec6b24d23ad",
        "displayName": "Demand Planning Dashboard",
        "displayOption": "FitToPage",
        "height": 900,
        "width": 1600
    }
    with open(page_json_path, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2)

    # Standard container objects for cards/slicers with rounded border (8D) and drop shadow
    card_slicer_container_objects = {
        "border": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "color": {"solid": {"color": {"expr": {"ThemeDataColor": {"ColorId": 0, "Percent": 0}}}}},
                    "radius": {"expr": {"Literal": {"Value": "8D"}}}
                }
            }
        ],
        "dropShadow": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}}
                }
            }
        ]
    }

    chart_container_objects = {
        "border": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "color": {"solid": {"color": {"expr": {"ThemeDataColor": {"ColorId": 0, "Percent": 0}}}}},
                    "radius": {"expr": {"Literal": {"Value": "8D"}}}
                }
            }
        ]
    }

    # 1. Main Title Header (Vivid Electric Blue background #1E88E5, rounded border 10D, white text #FFFFFF)
    create_visual_json(
        name="title_header",
        x=20, y=10, width=1560, height=50,
        visual_type="textbox",
        objects_dict={
            "general": [
                {
                    "properties": {
                        "paragraphs": [
                            {
                                "textRuns": [
                                    {
                                        "value": "DEMAND PLANNING DASHBOARD",
                                        "textStyle": {
                                            "fontWeight": "bold",
                                            "fontSize": "18pt",
                                            "fontFamily": "Segoe UI",
                                            "color": "#ffffff"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        },
        container_objects_dict={
            "background": [
                {
                    "properties": {
                        "color": {
                            "solid": {
                                "color": {
                                    "expr": {
                                        "ThemeDataColor": {
                                            "ColorId": 2,
                                            "Percent": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            ],
            "border": [
                {
                    "properties": {
                        "show": {"expr": {"Literal": {"Value": "true"}}},
                        "color": {
                            "solid": {
                                "color": {
                                    "expr": {
                                        "ThemeDataColor": {
                                            "ColorId": 2,
                                            "Percent": 0
                                        }
                                    }
                                }
                            }
                        },
                        "radius": {"expr": {"Literal": {"Value": "10D"}}}
                    }
                }
            ]
        }
    )

    # Helper objects dict for Dropdown Slicer style matching Power BI Desktop saved schema
    slicer_dropdown_objects = {
        "general": [{"properties": {}}],
        "data": [
            {
                "properties": {
                    "mode": {
                        "expr": {
                            "Literal": {
                                "Value": "'Dropdown'"
                            }
                        }
                    }
                }
            }
        ]
    }

    # 2. Top Slicers Bar (y=65, height=70)
    create_visual_json(
        name="slicer_year",
        x=20, y=65, width=180, height=70,
        visual_type="slicer",
        query_dict={
            "queryState": {
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Date"}},
                                    "Property": "Year"
                                }
                            },
                            "queryRef": "Dim_Date.Year"
                        }
                    ]
                }
            }
        },
        objects_dict=slicer_dropdown_objects,
        container_objects_dict=card_slicer_container_objects
    )

    create_visual_json(
        name="slicer_month",
        x=210, y=65, width=280, height=70,
        visual_type="slicer",
        query_dict={
            "queryState": {
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Date"}},
                                    "Property": "Month"
                                }
                            },
                            "queryRef": "Dim_Date.Month"
                        }
                    ]
                }
            }
        },
        objects_dict=slicer_dropdown_objects,
        container_objects_dict=card_slicer_container_objects
    )

    create_visual_json(
        name="slicer_category",
        x=500, y=65, width=260, height=70,
        visual_type="slicer",
        query_dict={
            "queryState": {
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Category"
                                }
                            },
                            "queryRef": "Dim_Product.Category"
                        }
                    ]
                }
            }
        },
        objects_dict=slicer_dropdown_objects,
        container_objects_dict=card_slicer_container_objects
    )

    create_visual_json(
        name="slicer_subcategory",
        x=770, y=65, width=260, height=70,
        visual_type="slicer",
        query_dict={
            "queryState": {
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Subcategory"
                                }
                            },
                            "queryRef": "Dim_Product.Subcategory"
                        }
                    ]
                }
            }
        },
        objects_dict=slicer_dropdown_objects,
        container_objects_dict=card_slicer_container_objects
    )

    create_visual_json(
        name="slicer_product",
        x=1040, y=65, width=540, height=70,
        visual_type="slicer",
        query_dict={
            "queryState": {
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Product"
                                }
                            },
                            "queryRef": "Dim_Product.Product"
                        }
                    ]
                }
            }
        },
        objects_dict=slicer_dropdown_objects,
        container_objects_dict=card_slicer_container_objects
    )

    # 3. KPI Cards Strip (y=145, height=90)
    kpi_configs = [
        ("card_forecast", "Total Forecast", 20, "_Measures", "Total Forecast"),
        ("card_sales", "Total Sales", 245, "_Measures", "Total Sales"),
        ("card_error", "Raw Error", 470, "_Measures", "Raw Error"),
        ("card_bias", "Bias %", 695, "_Measures", "Bias %"),
        ("card_abs_error", "Abs Error", 920, "_Measures", "Abs Error"),
        ("card_mad", "MAD", 1145, "_Measures", "MAD"),
        ("card_accuracy", "Forecast Accuracy %", 1370, "_Measures", "Forecast Accuracy %")
    ]

    for name, title, x_pos, entity, property_name in kpi_configs:
        create_visual_json(
            name=name,
            x=x_pos, y=145, width=210, height=90,
            visual_type="card",
            query_dict={
                "queryState": {
                    "Fields": {
                        "projections": [
                            {
                                "field": {
                                    "Measure": {
                                        "Expression": {"SourceRef": {"Entity": entity}},
                                        "Property": property_name
                                    }
                                },
                                "queryRef": f"{entity}.{property_name}"
                            }
                        ]
                    }
                }
            },
            container_objects_dict=card_slicer_container_objects
        )

    # 4. Combo Line & Bar Chart (y=245, height=320)
    create_visual_json(
        name="combo_sales_forecast_accuracy",
        x=20, y=245, width=1000, height=320,
        visual_type="lineStackedColumnComboChart",
        query_dict={
            "queryState": {
                "Category": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Date"}},
                                    "Property": "Month"
                                }
                            },
                            "queryRef": "Dim_Date.Month"
                        }
                    ]
                },
                "Y": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Sales"
                                }
                            },
                            "queryRef": "_Measures.Total Sales"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Forecast"
                                }
                            },
                            "queryRef": "_Measures.Total Forecast"
                        }
                    ]
                },
                "Y2": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Forecast Accuracy %"
                                }
                            },
                            "queryRef": "_Measures.Forecast Accuracy %"
                        }
                    ]
                }
            }
        },
        container_objects_dict=chart_container_objects
    )

    # 5. Bias Horizontal Bar Chart (y=245, height=320)
    create_visual_json(
        name="bar_bias_chart",
        x=1035, y=245, width=545, height=320,
        visual_type="barChart",
        query_dict={
            "queryState": {
                "Category": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Date"}},
                                    "Property": "Month"
                                }
                            },
                            "queryRef": "Dim_Date.Month"
                        }
                    ]
                },
                "Y": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Bias %"
                                }
                            },
                            "queryRef": "_Measures.Bias %"
                        }
                    ]
                }
            }
        },
        container_objects_dict=chart_container_objects
    )

    # 6. Scatter / Bubble Chart (y=575, height=310)
    create_visual_json(
        name="scatter_product_accuracy",
        x=20, y=575, width=500, height=310,
        visual_type="scatterChart",
        query_dict={
            "queryState": {
                "X": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "WAPE Accuracy %"
                                }
                            },
                            "queryRef": "_Measures.WAPE Accuracy %"
                        }
                    ]
                },
                "Y": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Sales"
                                }
                            },
                            "queryRef": "_Measures.Total Sales"
                        }
                    ]
                },
                "Size": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Forecast"
                                }
                            },
                            "queryRef": "_Measures.Total Forecast"
                        }
                    ]
                },
                "Series": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Product"
                                }
                            },
                            "queryRef": "Dim_Product.Product"
                        }
                    ]
                }
            }
        },
        container_objects_dict=chart_container_objects
    )

    # 7. Matrix Data Table Visual (y=575, height=310)
    create_visual_json(
        name="matrix_demand_metrics",
        x=535, y=575, width=1045, height=310,
        visual_type="pivotTable",
        query_dict={
            "queryState": {
                "Rows": {
                    "projections": [
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Subcategory"
                                }
                            },
                            "queryRef": "Dim_Product.Subcategory"
                        },
                        {
                            "field": {
                                "Column": {
                                    "Expression": {"SourceRef": {"Entity": "Dim_Product"}},
                                    "Property": "Product"
                                }
                            },
                            "queryRef": "Dim_Product.Product"
                        }
                    ]
                },
                "Values": {
                    "projections": [
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Sales"
                                }
                            },
                            "queryRef": "_Measures.Total Sales"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Total Forecast"
                                }
                            },
                            "queryRef": "_Measures.Total Forecast"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Raw Error"
                                }
                            },
                            "queryRef": "_Measures.Raw Error"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Bias %"
                                }
                            },
                            "queryRef": "_Measures.Bias %"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "MAPE %"
                                }
                            },
                            "queryRef": "_Measures.MAPE %"
                        },
                        {
                            "field": {
                                "Measure": {
                                    "Expression": {"SourceRef": {"Entity": "_Measures"}},
                                    "Property": "Forecast Accuracy %"
                                }
                            },
                            "queryRef": "_Measures.Forecast Accuracy %"
                        }
                    ]
                }
            }
        },
        container_objects_dict=chart_container_objects
    )

    print("Updated scripts/build_pbi_report.py to mirror vivid blue header and card container styling!")

if __name__ == "__main__":
    build_report_visuals()
