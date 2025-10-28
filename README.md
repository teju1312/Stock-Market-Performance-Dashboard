# Stock-Market-Performance-Dashboard
Developed a robust analytics workflow for stock market data using Python, SQL, and Power BI.

# 📌 Project Overview
Developed a robust, automated analytics pipeline for stock market data, combining Python for data transformation, MySQL for database management, and Power BI/DAX for interactive visualization. The project delivers end-to-end insights for stock prices, trends, and comparative analytics 

# 🔄 Workflow
Raw stock market data (Excel/CSV) ➡️ Data cleaning and transformation with Python (pandas) ➡️ Data loaded into MySQL database via Python ➡️ Power BI direct query from MySQL ➡️ Power BI Dashboard

# 📊 Dataset
1. Columns: Symbol, Trade Time/Date, Open/High/Low/Close Price, Volume, Price Change, Calculated KPIs.

2. Source: Sample or historical stock data in Excel/CSV, transformed to SQL for centralized access.

3. Format: Cleaned in Python (pandas), stored in relational tables (MySQL), visualized via Power BI.

# 🔧 Steps Involved

1. Cleaned and prepared stock data in Python by fixing missing values and formatting columns.

2. Automated data loading into MySQL and set up a proper database structure.

3. Connected Power BI to MySQL to run live and flexible data queries.

4. Added DAX formulas in Power BI to calculate price changes, ranges, and volatility.

5. Built interactive reports with filters for stock symbols, dates, and metrics.

6. ncluded detailed tables to check individual transactions and ensure data accuracy.

# 📈 Dashboard Pages
1. Stock Dashboard

2. Validation Table

# 🚀 Tools & Technologies
1. Python (pandas)

2. MySQL

3. Power BI 

4. Excel

# 🧠 Learnings
1. Learned to collect, clean, and move financial data using Python and SQL.

2. Linked data with Power BI to build live and flexible financial dashboards.

3. Made clear visuals for quick overviews and detailed accuracy checks.

4. Learned to connect excel and databases and dashboards into one smooth workflow.

# ✅ Page 1: Stock Dashboard

This page provides a high-level summary of stock market performance, delivering essential KPIs for price, volume, and percent change across selected symbols and date ranges.

1. This dashboard shows daily stock performance for different companies.

2. It tracks key metrics like percentage change, average volume, and daily fluctuations.

3. The bar chart compares the price range for each stock symbol.

4. The line chart shows the daily percentage change trend across the year.

5. Filters allow users to select specific companies or time periods to analyze.

6. Overall, it helps to monitor and compare stock trends visually and interactively.

![Stock Dashboard](gifs/Stock_dashboard.gif)

# ✅ Page 2: Validation Table 

Slicer-driven detail tables for result checks.

1. This page shows the detailed stock data in a tabular format.

2. It includes key fields like open price, close price, volume, and daily percentage change.

3. Users can filter by stock symbol or date range using slicers on the right.

4. It helps to analyze exact daily values and verify trends seen in the main dashboard.

5. This page is mainly used for data validation and deeper numeric analysis of stock performance.

![Table](Table.gif)
