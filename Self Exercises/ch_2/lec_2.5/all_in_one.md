# Power BI - Self Exercises Q&A

### Q.1 What is the difference between appending and merging queries in Power BI?

**Answer:**  
- **Append Queries**: Combines data **vertically** (stacking rows one below the other). Used when you have multiple tables/files with the **same structure/columns** (e.g., monthly sales files from different months or years).  
  → Result: More rows, same columns.

- **Merge Queries**: Combines data **horizontally** (like a SQL JOIN). Used when you need to bring in additional columns from another table based on a common key (e.g., adding customer details to a sales table using CustomerID).  
  → Result: More columns, same or fewer rows depending on the join type.

**In short**: Append = stack tables (union), Merge = join tables (like VLOOKUP or SQL JOIN).

---

### Q.2 How does the “Append Queries” option work in Power Query Editor?

**Answer:**  
There are two options:  
1. **Append Queries** – Combines 2 or more selected queries.  
2. **Append Queries as New** – Creates a new query with the appended result (original queries remain unchanged).

Steps:  
- Go to **Home** → **Append Queries** → Choose the queries to stack → Power Query automatically aligns columns by name or position → Handles mismatched columns by filling nulls.

---

### Q.3 Explain the process of appending multiple files from a folder in Power BI.

**Answer:**  
1. **Get Data** → **Folder**  
2. Select the folder containing similar files (e.g., CSV/Excel sales files)  
3. Click **Combine** → Choose the file type → Select the correct sheet/table  
4. Power BI automatically creates:  
   - A sample query (template)  
   - A function that applies the transformation to every file  
   - Final appended query with all files stacked  
5. Remove unwanted columns (like “Source.Name” if not needed) and filter if required.

This is the most common way to load monthly/weekly files dynamically.

---

### Q.4 Why is it important to ensure file structures are consistent before appending files?

**Answer:**  
- Column names, data types, and column order should be identical (or very similar).  
- If inconsistent:  
  → Mismatched columns get null values  
  → Data type conflicts cause errors or incorrect results  
  → Performance issues and messy data model  
- Consistent structure ensures clean, accurate, and automatic combining without manual fixes every time new files are added.

---

### Q.5 What are Data Source Settings in Power BI, and what can you configure from there?

**Answer:**  
**Data Source Settings** (found in Power BI Desktop: File → Options and settings → Data source settings) allow you to:  
- View and manage all data sources used in the current file  
- Change source (e.g., file path, server name)  
- Edit credentials  
- Set privacy levels  
- Clear permissions  
- Change data source type in some cases  

Very useful when moving reports from development to production.

---

### Q.6 How can you update credentials or privacy levels using Data Source Settings?

**Answer:**  
1. Go to **File** → **Options and settings** → **Data source settings**  
2. Select the data source → Click **Edit Permissions**  
3. Update credentials (e.g., Windows, Organizational account, Database credentials)  
4. Change **Privacy Level** (None, Private, Organizational)  
5. Click OK → Refresh preview if needed  

This fixes most “access denied” or credential errors.

---

### Q.7 What is a parameter in Power BI, and how is it useful for dynamic queries?

**Answer:**  
A **Parameter** is a dynamic value that can be used inside queries (especially in file paths, SQL queries, filters, etc.).  

**Common uses:**  
- Switch between file folders (Dev vs Prod)  
- Dynamic database server/database name  
- Filter data by dynamic date (e.g., last N days)  

Created via: **Home** → **Manage Parameters** → **New Parameter**

---

### Q.8 Explain how parameters can be used to switch between development and production data sources.

**Answer:**  
1. Create two parameters:  
   - `Env` (Type: Text, Suggested values: Any value or List → "Development", "Production")  
   - `Server_Dev`, `Server_Prod`, `Database_Dev`, `Database_Prod`  
2. Create a query that uses conditional logic:  
   ```powerquery
   if Env = "Production" 
   then "Server_Prod" 
   else "Server_Dev"