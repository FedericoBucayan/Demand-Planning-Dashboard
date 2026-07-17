@echo off
title Demand Intelligence Dashboard Updater
color 0A
echo ===================================================
echo   DEMAND INTELLIGENCE DASHBOARD DATA UPDATER
echo ===================================================
echo.
echo Processing Excel data source...
echo.

:: Run Python script
py -V >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    py "reference_material\build_dashboard.py"
) else (
    python "reference_material\build_dashboard.py"
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ===================================================
    echo  [ERROR] Failed to update the dashboard dataset!
    echo ===================================================
    echo.
    echo Possible causes:
    echo 1. The Excel file "Forecasting_&_Actuals_Database.xlsx" is open in Microsoft Excel. 
    echo    Please close Excel and run this script again.
    echo 2. Python is not installed or the "pandas" package is missing.
    echo.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ===================================================
echo  [SUCCESS] Database exported to data.js successfully!
echo ===================================================
echo.
echo Launching your updated Demand Planning Dashboard...
start index.html
echo.
ping 127.0.0.1 -n 4 >nul
