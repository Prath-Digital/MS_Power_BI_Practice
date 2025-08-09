# Power BI Questions and Answers

## Q1. What are data connectors in Power BI, and why are they important?
Data connectors in Power BI are tools that allow you to import data from various sources such as databases, cloud services, and files. They are important because they enable seamless integration of diverse data, making it easier to analyze and visualize information from multiple platforms.

## Q2. List some common types of data connectors available in Power BI.
- SQL Server
- Excel
- SharePoint
- Azure
- Google Analytics
- Salesforce

## Q3. How does Power BI support connection to cloud-based and on-premises data sources?
Power BI supports cloud-based data sources through online services like Azure and Google BigQuery, using direct query or import methods. For on-premises data, it uses the On-premises Data Gateway to securely connect to local databases and servers, ensuring real-time or scheduled data updates.

## Q4. What is the role of the Power Query Editor in Power BI?
The Power Query Editor is a tool in Power BI used for data transformation and preparation. It helps clean, shape, and model data before loading it into reports, ensuring the data is in an optimal format for analysis.

## Q5. What are the basic steps involved in loading data using Power Query Editor?
1. Open Power BI and select "Get Data".
2. Choose the data source and connect to it.
3. Load the data into the Power Query Editor.
4. Apply transformations as needed.
5. Click "Close & Apply" to load the data into Power BI.

## Q6. How does the Power Query Editor help in cleaning and transforming data?
The Power Query Editor provides features like removing duplicates, filtering rows, splitting columns, and changing data types, which help clean and transform raw data into a structured format suitable for analysis.

## Q7. What is the difference between applying changes and discarding changes in Power Query Editor?
Applying changes saves and implements the transformations to the data model in Power BI, while discarding changes reverts to the original data state, undoing all modifications made in the editor.

## Q8. What is meant by table transformation in Power BI?
Table transformation in Power BI refers to the process of modifying a table's structure or content, such as adding columns, removing rows, or changing data types, using the Power Query Editor to prepare data for analysis.

## Q9. List common table transformations that can be performed in the Power Query Editor.
- Remove duplicates
- Filter rows
- Split columns
- Change data types
- Merge tables
- Pivot or unpivot columns

## Q10. How can you remove duplicates from a table using Power Query Editor?
Select the table, go to the "Home" tab, click "Remove Rows," and choose "Remove Duplicates" to eliminate duplicate entries based on selected columns.

## Q11. Explain how to merge two tables using Power Query Editor.
1. Load both tables into the Power Query Editor.
2. Go to the "Home" tab and select "Merge Queries."
3. Choose the two tables, select the matching columns, and pick a join type (e.g., Inner Join).
4. Click "OK" to merge, then apply the changes.

## Q12. How can you split a column into multiple columns in the Power Query Editor?
Select the column, go to the "Home" tab, click "Split Column," and choose an option like "By Delimiter." Specify the delimiter (e.g., comma), and the column will split into multiple columns accordingly.