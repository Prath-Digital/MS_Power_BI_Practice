# Database Normalization & Data Modeling in Power BI - Q&A Summary

Here is a complete, friendly, and easy-to-read Markdown guide answering all your questions about database normalization, star schema, and Power BI data modeling.

## Q.1 What is database normalization and why is it important in data modeling?

**Answer:**  
Database normalization is the process of organizing data in a relational database by splitting large tables into smaller, related tables and defining relationships between them using rules called **normal forms**.  

**Why it’s important:**
- Eliminates data redundancy (no repeated data)
- Prevents update/delete/insert anomalies
- Improves data integrity and consistency
- Makes the database easier to maintain and query efficiently

In data warehousing and Power BI, we usually stop at **3NF** and then **denormalize slightly** to create star schemas for better analytics performance.

---

## Q.2 Describe the first three normal forms (1NF, 2NF, 3NF) with examples.

**Answer:**

| Normal Form | Rule | Example (Before → After) |
|-------------|------|---------------------------|
| **1NF** | No repeating groups or arrays. Every column must be atomic (single value). | Before: Customer with phone numbers "123, 456, 789" → After: Separate row for each phone |
| **2NF** | Must be in 1NF + No partial dependency (non-key attributes depend on entire primary key) | Order table with OrderID+ProductID as PK, but CustomerName depends only on CustomerID → Split into Orders and Customers |
| **3NF** | Must be in 2NF + No transitive dependency (non-key attributes don’t depend on other non-key attributes) | Employee → Department → DepartmentLocation → Move DepartmentLocation to separate Department table |

---

## Q.3 How does normalization help reduce data redundancy and improve consistency?

**Answer:**  
- **Reduces redundancy**: Same data is stored only once (e.g., customer address appears in one table instead of every order row).  
- **Improves consistency**: When you update data (e.g., customer phone), you update it in only one place → no risk of having different values in different rows (update anomaly).

---

## Q.4 What is the difference between a Fact Table and a Dimension Table?

**Answer:**

| Aspect                | Fact Table                              | Dimension Table                          |
|-----------------------|-----------------------------------------|------------------------------------------|
| Purpose               | Stores measurable events (transactions) | Stores descriptive attributes            |
| Size                  | Usually very large (millions of rows)   | Smaller (thousands of rows)              |
| Columns               | Foreign keys + measures (SalesAmount, Quantity) | Primary key + descriptive fields (Name, Category, Date) |
| Example               | FactSales                               | DimCustomer, DimProduct, DimDate         |
| Granularity           | Lowest level (one row per transaction)  | Higher level (one row per customer)      |

---

## Q.5 Explain the role of Fact Tables in a star schema.

**Answer:**  
Fact tables are the **center** of a star schema. They contain:
- Quantitative metrics (sales amount, quantity sold, profit)
- Foreign keys linking to dimension tables

They represent **business processes** or events (sales, orders, shipments, website clicks, etc.). Multiple fact tables can exist (e.g., FactSales, FactInventory).

---

## Q.6 Give an example of a business scenario where Dimension Tables are used for filtering and categorization.

**Answer:**  
**Scenario:** Retail company analyzing sales performance  

**Dimension tables used:**
- **DimDate** → Filter by year, quarter, holiday season
- **DimProduct** → Filter by category (Electronics, Clothing), brand, color
- **DimCustomer** → Filter by age group, loyalty status, region
- **DimStore** → Filter by city, store type (online vs physical)

Users can slice and dice sales data effortlessly in Power BI reports.

---

## Q.7 What is a Primary Key and how is it different from a Foreign Key?

**Answer:**

| Feature             | Primary Key (PK)                     | Foreign Key (FK)                          |
|---------------------|--------------------------------------|-------------------------------------------|
| Uniqueness          | Must be unique in its table          | Can have duplicates                       |
| Null values         | Cannot be NULL                       | Can be NULL (optional relationship)       |
| Purpose             | Uniquely identifies each row         | Links to PK in another table              |
| Example             | CustomerID in DimCustomer            | CustomerKey in FactSales                  |

---

## Q.8 How do Primary and Foreign Keys help maintain referential integrity in relational models?

**Answer:**  
Referential integrity ensures that relationships between tables remain consistent:
- You cannot add a row in the fact table with a foreign key value that doesn’t exist in the dimension table.
- You cannot delete a dimension row if it’s still referenced by a fact row (unless cascading rules are set).

This prevents orphan records and guarantees reliable joins.

---

## Q.9 Why is it important to identify keys when building relationships between tables in Power BI?

**Answer:**  
Power BI uses keys to:
- Create correct relationships (one-to-many is most common)
- Enable proper filtering (from dimension → fact)
- Optimize DAX performance
- Prevent ambiguous or incorrect aggregations

Without proper keys, you’ll get errors like “cardinality issues” or wrong numbers in visuals.

---

## Q.10 What is the difference between using Relationships and Merged Tables in Power BI?

**Answer:**

| Aspect                  | Relationships (Recommended)               | Merged Tables (Query Editor)             |
|-------------------------|--------------------------------------------|------------------------------------------|
| Performance             | Much faster (uses Vertipaq engine)         | Slower, increases model size             |
| Flexibility             | Easy to filter in any direction            | Fixed at refresh time                    |
| Storage                 | Efficient (no duplication)                 | Duplicates data → larger file            |
| Maintenance             | Easy to manage                             | Hard to update when source changes       |
| Best for                | Star schema modeling                       | Rare cases (e.g., role-playing dimensions without workaround) |

**Rule of thumb:** Use relationships whenever possible. Merge only when absolutely necessary.

---

## Q.11 When should you prefer creating a relationship instead of merging tables?

**Answer:**  
Prefer relationships in almost all cases, especially when:
- You have a classic star schema (fact + dimensions)
- You want fast performance and small file size
- You need bidirectional filtering or many-to-many with bridge tables
- Data changes frequently

Only merge if:
- You need to bring in a small lookup table that has no common key
- You’re doing complex transformations that can’t be done with DAX

---

## Q.12 What are the implications of using multiple relationships vs. merged queries on performance and data modeling flexibility?

**Answer:**

| Aspect                     | Multiple Relationships (in model)               | Merged Queries (in Power Query)            |
|----------------------------|--------------------------------------------------|--------------------------------------------|
| Model size                 | Smaller                                          | Larger (data duplication)                  |
| Refresh speed              | Faster                                           | Slower (extra transformation steps)        |
| Report performance         | Excellent (relationships are optimized)          | Can be slower                              |
| Flexibility                | Very high – can activate/deactivate with USERELATIONSHIP in DAX | Low – data is physically combined          |
| Complexity for beginners   | Slightly higher (need to understand active/inactive) | Simpler concept                            |

**Best practice:** Keep data normalized with relationships → use DAX (like USERELATIONSHIP, bridge tables, or role-playing dimensions via calculated tables) instead of merging.

---

Hope this helps you ace your interview or project!  
Feel free to copy this entire Markdown file into your notes or GitHub repo. Good luck! 🚀