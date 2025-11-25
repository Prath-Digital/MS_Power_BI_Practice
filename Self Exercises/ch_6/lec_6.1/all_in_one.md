# Power BI - DAX Language and Calculations Self-Exercise

## Q.1 What is DAX, and how is it used in Power BI?

**DAX (Data Analysis Expressions)** is a formula language used in Power BI, Excel Power Pivot, and Analysis Services. It's a collection of functions, operators, and constants that can be used in formulas to calculate and return values.

**How DAX is used in Power BI:**
- Creating calculated columns that add new data to tables
- Creating measures for dynamic calculations in visualizations
- Defining calculated tables based on expressions
- Implementing row-level security rules
- Creating complex business logic and KPIs

DAX formulas are similar to Excel formulas but are specifically designed to work with relational data and perform dynamic aggregations in reports and dashboards.

---

## Q.2 How do DAX functions differ from Excel functions?

While DAX and Excel share some similar function names, they have key differences:

**Context Awareness:**
- DAX operates in row context and filter context, making it context-sensitive
- Excel functions typically work on cell references and ranges

**Relational Data:**
- DAX is designed to work with relational data models and multiple tables
- Excel functions primarily work with cell ranges and worksheets

**Dynamic Calculations:**
- DAX measures recalculate automatically based on filters and slicers
- Excel formulas are static unless explicitly recalculated

**Function Behavior:**
- Similar function names may behave differently (e.g., `SUM` in DAX vs Excel)
- DAX has table functions that return entire tables, not just single values
- DAX includes time intelligence functions not available in Excel

**Performance:**
- DAX is optimized for large datasets through columnar storage
- Excel calculations can become slow with very large datasets

---

## Q.3 Name some common DAX functions for aggregation and filtering data

**Aggregation Functions:**
- `SUM()` - Adds all numbers in a column
- `AVERAGE()` - Calculates the arithmetic mean
- `MIN()` - Returns the smallest value
- `MAX()` - Returns the largest value
- `COUNT()` - Counts the number of rows
- `COUNTROWS()` - Counts rows in a table
- `DISTINCTCOUNT()` - Counts unique values
- `SUMX()` - Iterator function that evaluates an expression for each row

**Filtering Functions:**
- `FILTER()` - Returns a table with rows that meet specific conditions
- `ALL()` - Removes all filters from specified columns or tables
- `ALLEXCEPT()` - Removes all filters except those specified
- `CALCULATE()` - Evaluates an expression with modified filter context
- `CALCULATETABLE()` - Returns a filtered table
- `RELATED()` - Retrieves related values from another table
- `RELATEDTABLE()` - Returns related rows from another table
- `VALUES()` - Returns distinct values from a column
- `DISTINCT()` - Returns unique values from a column

---

## Q.4 How can DAX be used to create custom calculations in Power BI reports?

DAX enables custom calculations through several approaches:

**Calculated Columns:**
```dax
Full Name = [First Name] & " " & [Last Name]
```
- Computed row-by-row when data is loaded
- Stored in the data model
- Available for slicing, filtering, and grouping

**Measures:**
```dax
Total Sales = SUM(Sales[Amount])
```
- Calculated dynamically based on filter context
- Don't consume storage space
- Ideal for aggregations in visuals

**Complex Business Logic:**
```dax
Sales Growth % = 
DIVIDE(
    [Total Sales] - [Total Sales Previous Year],
    [Total Sales Previous Year]
)
```

**Time Intelligence:**
```dax
YTD Sales = TOTALYTD([Total Sales], Calendar[Date])
```

**Conditional Calculations:**
```dax
Sales Category = 
SWITCH(
    TRUE(),
    [Total Sales] > 100000, "High",
    [Total Sales] > 50000, "Medium",
    "Low"
)
```

---

## Q.5 What are the key differences between DAX and M Languages in Power BI?

| Aspect | DAX | M (Power Query) |
|--------|-----|-----------------|
| **Purpose** | Analysis and calculations | Data transformation and loading |
| **When Used** | After data is loaded | During data import/refresh |
| **Focus** | Aggregations, measures, KPIs | ETL operations, data cleaning |
| **Language Type** | Functional, formula-based | Functional, query-based |
| **Interface** | Formula bar, measure editor | Power Query Editor |
| **Performance** | Optimized for analytical queries | Optimized for data transformation |
| **Output** | Values, measures, columns | Tables, transformed datasets |
| **Context** | Row and filter context | Step-by-step transformations |

**When to Use Each:**
- Use **M** for data shaping, merging tables, cleaning data, and creating custom columns during import
- Use **DAX** for calculations, aggregations, and measures that respond to user interactions

---

## Q.6 When should you use DAX instead of M in Power BI?

**Use DAX when you need to:**
- Create measures for dynamic calculations in visuals
- Perform aggregations that change based on filters and slicers
- Implement business logic that depends on user interactions
- Create calculated columns based on relationships between tables
- Build time intelligence calculations (YTD, MTD, prior period comparisons)
- Define KPIs and complex analytical calculations
- Create calculations that need to respond to report context

**Use M when you need to:**
- Clean and transform data during import
- Merge or append tables from different sources
- Remove duplicates or filter rows before loading
- Change data types or restructure columns
- Create custom columns based on static logic
- Perform data shaping operations
- Handle data source connections and authentication

**Key Principle:** M transforms data before it enters the model; DAX calculates results within the model during analysis.

---

## Q.7 How does M Language play a role in Power Query, and how does DAX play a role in data modeling?

**M Language in Power Query:**

M is the language behind Power Query, responsible for the ETL (Extract, Transform, Load) process:
- Connects to various data sources
- Performs data cleaning operations (removing nulls, trimming spaces)
- Transforms data structure (pivoting, unpivoting, splitting columns)
- Merges and appends queries
- Creates custom functions for reusable transformations
- Each step in Power Query generates M code behind the scenes

Example M code:
```m
let
    Source = Excel.Workbook(File.Contents("C:\Data.xlsx")),
    Sheet1 = Source{[Name="Sheet1"]}[Data],
    ChangedType = Table.TransformColumnTypes(Sheet1, {{"Date", type date}})
in
    ChangedType
```

**DAX in Data Modeling:**

DAX plays a crucial role in the data model layer:
- Defines relationships and cardinality between tables
- Creates calculated columns that enhance the data model
- Builds measures for analytical calculations
- Implements row-level security expressions
- Creates calculated tables for modeling scenarios
- Defines time intelligence patterns using date tables

DAX works with the imported and transformed data to provide analytical insights, while M prepares the data for analysis.

---

## Q.8 What is a calculated column in Power BI, and when should it be used?

**Calculated Column Definition:**

A calculated column is a column you add to a table using a DAX formula. It's computed row-by-row when data is refreshed and stored in the data model.

**Syntax Example:**
```dax
Profit = Sales[Revenue] - Sales[Cost]
```

**When to Use Calculated Columns:**
- When you need to slice, filter, or group data by the calculated value
- When the calculation depends on values in the same row
- When you need to use the result in relationships
- When creating categorical classifications based on row data
- When building hierarchies that include calculated values

**When NOT to Use Calculated Columns:**
- For simple aggregations (use measures instead)
- When the calculation is too complex (consider M in Power Query)
- When you need dynamic calculations based on filters (use measures)

**Important Considerations:**
- Calculated columns consume memory and increase model size
- They're calculated during data refresh, not during report interaction
- They're stored in the data model like any other column

---

## Q.9 How does a calculated column differ from a measure in DAX?

| Feature | Calculated Column | Measure |
|---------|------------------|---------|
| **Storage** | Stored in data model | Not stored, calculated on-demand |
| **Calculation Time** | During data refresh | During query/visual rendering |
| **Context** | Row context | Filter context |
| **Memory Impact** | Increases model size | Minimal memory footprint |
| **Usage** | Slicers, filters, axes, grouping | Values in visuals, aggregations |
| **Formula Type** | Row-by-row calculation | Aggregation across rows |
| **Performance** | Can slow refresh | Can slow report rendering |
| **Reusability** | Less flexible | Highly reusable |

**Example Calculated Column:**
```dax
Total Price = Products[Unit Price] * Products[Quantity]
```
- Calculates for each row
- Can be used in slicers
- Takes up storage

**Example Measure:**
```dax
Total Sales = SUM(Sales[Amount])
```
- Calculates based on current filters
- Dynamic and context-aware
- No storage impact

**Rule of Thumb:** Use calculated columns for attributes; use measures for metrics.

---

## Q.10 What are the limitations of using calculated columns in Power BI?

**Performance Limitations:**
- Increases data model size significantly, especially with large datasets
- Slows down data refresh times as each row must be calculated
- Can impact query performance if overused
- Consumes more RAM when the model is loaded

**Functional Limitations:**
- Cannot use time intelligence functions directly
- Cannot dynamically change based on user filters in visuals
- Limited to row context, making cross-table aggregations complex
- Cannot be used for measures that need to respond to slicer selections

**Design Limitations:**
- Not ideal for calculations that should vary by visual context
- Increases model complexity and maintenance overhead
- Cannot reference measures directly
- May duplicate logic that could be handled in Power Query more efficiently

**Best Practices:**
- Consider creating calculated columns in Power Query using M instead
- Use measures when aggregation or filter context is needed
- Limit calculated columns to essential categorizations and groupings
- Evaluate whether the calculation truly needs to be row-by-row

---

## Q.11 What is the purpose of a measure in Power BI, and how is it different from a calculated column?

**Purpose of a Measure:**

Measures are dynamic DAX formulas designed to perform aggregations and calculations that respond to the current filter context. They're the primary tool for creating analytical metrics in Power BI.

**Key Purposes:**
- Calculate KPIs and business metrics (sales, profit, growth rates)
- Perform aggregations across filtered data
- Create ratio and percentage calculations
- Implement time intelligence (YTD, MTD, previous period)
- Build conditional calculations based on context
- Display values in cards, tables, and charts

**Differences from Calculated Columns:**

**Calculation Timing:**
- Measures: Calculated when visualizations render
- Calculated Columns: Calculated during data refresh

**Context Type:**
- Measures: Work with filter context (respond to slicers and filters)
- Calculated Columns: Work with row context (calculated row-by-row)

**Storage:**
- Measures: No storage required; calculated on-demand
- Calculated Columns: Stored in the model, consuming memory

**Use Cases:**
- Measures: "What is the total sales?" (aggregation)
- Calculated Columns: "What category does this sale belong to?" (classification)

**Flexibility:**
- Measures: Highly dynamic, change with every filter
- Calculated Columns: Static once calculated

---

## Q.12 How are measures used in visualizations and aggregations in Power BI?

**In Visualizations:**

Measures are the primary way to display quantitative values in Power BI visuals:

**Card Visuals:**
```dax
Total Revenue = SUM(Sales[Amount])
```
- Displays a single aggregated value
- Updates based on page/report filters

**Tables and Matrices:**
```dax
Average Order Value = DIVIDE([Total Revenue], [Order Count])
```
- Shows measures broken down by dimensions
- Calculated for each row/column intersection

**Charts (Bar, Line, Pie):**
```dax
Profit Margin % = DIVIDE([Total Profit], [Total Revenue])
```
- Measures appear on values axis
- Aggregate according to categories

**In Aggregations:**

Measures handle complex aggregation scenarios:

**Filtered Aggregations:**
```dax
Online Sales = CALCULATE([Total Sales], Sales[Channel] = "Online")
```

**Time-Based Aggregations:**
```dax
YTD Sales = TOTALYTD([Total Sales], Calendar[Date])
Previous Year Sales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date]))
```

**Conditional Aggregations:**
```dax
High Value Sales = SUMX(FILTER(Sales, Sales[Amount] > 1000), Sales[Amount])
```

**Percentage Calculations:**
```dax
Sales % of Total = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Products)))
```

Measures automatically adjust to the filter context created by slicers, page filters, visual-level filters, and row/column selections in tables, making them essential for interactive reporting.