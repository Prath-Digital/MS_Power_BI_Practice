# Power BI Questions and Answers

## Q1: What are the different storage modes available in Power BI?
- **Import Mode**: Data is imported and stored in Power BI's in-memory engine.
- **DirectQuery Mode**: Data is queried directly from the source in real-time.
- **Dual Mode**: Combines both Import and DirectQuery modes for flexibility.

## Q2: Differentiate between Import Mode, DirectQuery Mode, and Dual Mode in Power BI.
- **Import Mode**: Loads data into Power BI for fast performance but requires refreshes.
- **DirectQuery Mode**: Queries data live from the source, ideal for real-time data with no storage limit.
- **Dual Mode**: Allows mixing imported data with live queries for optimized performance.

## Q3: What factors should you consider while choosing a storage mode for your dataset?
- Data refresh frequency.
- Size and volume of data.
- Real-time data needs.
- Performance requirements.
- Source system limitations.

## Q4: Explain the steps to connect Power BI to a MySQL database.
1. Open Power BI Desktop.
2. Click "Get Data" and select "MySQL database".
3. Enter the server name and database credentials.
4. Provide authentication details (e.g., username and password).
5. Select the tables or views to import and click "Load" or "Transform Data".

## Q5: What security considerations should be taken into account while connecting to a database from Power BI?
- Use encrypted connections (e.g., SSL/TLS).
- Implement strong authentication (e.g., OAuth, Windows Auth).
- Restrict access with role-based security.
- Regularly update credentials and permissions.
- Monitor data access logs.

## Q6: What are the common methods to extract data from a website into Power BI?
- Web connector using URLs.
- Power Query to scrape HTML tables.
- API integration for structured data.

## Q7: Explain the concept of scraping a web table into Power BI using Power Query.
Scraping a web table involves using Power Query to connect to a webpage, navigate to the table, and extract its data into Power BI for analysis. This is done by selecting the web connector, entering the URL, and choosing the table to import.

## Q8: What limitations should you consider while extracting data from the web?
- Website structure changes can break connections.
- Rate limits or CAPTCHA protections.
- Incomplete or inconsistent data.
- Legal and ethical restrictions on data usage.

## Q9: What is Data Quality Assessment (QA) in the context of Power BI?
Data Quality Assessment (QA) in Power BI involves evaluating data accuracy, completeness, consistency, and reliability before or during analysis to ensure reliable insights.

## Q10: List some Data Profiling tools available in Power Query Editor.
- Column Quality.
- Column Distribution.
- Column Profile.
- Value Distribution.

## Q11: How does the Column Quality and Column Distribution feature help in improving data quality in Power BI?
- **Column Quality**: Identifies null values, errors, and empty rows to clean data.
- **Column Distribution**: Shows value distribution to detect outliers or inconsistencies, aiding in data refinement.