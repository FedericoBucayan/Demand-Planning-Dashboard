@echo off
echo Cleaning orphaned Power BI background processes...
powershell -Command "Stop-Process -Name PBIDesktop, msmdsrv -Force -ErrorAction SilentlyContinue"
ping 127.0.0.1 -n 2 >nul

echo Opening Demand Planning Dashboard in Power BI Desktop...
start "" "C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe" "%~dp0Demand_Planning_Dashboard.pbip"

exit
