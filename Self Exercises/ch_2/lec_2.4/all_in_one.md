# Power BI - Self Exercises Q&A

## Q1. What is an Index Column in Power BI and how is it useful?
An Index Column is a sequential identifier added to rows in Power Query. It is useful for maintaining order, supporting merges, defining row uniqueness, and detecting patterns.

## Q2. How do you create a Conditional Column in Power BI?
Go to Power Query Editor → Add Column → Conditional Column → Define rules → Apply.

## Q3. Explain a real-world use case for using Conditional Columns.
Example: Customer segmentation based on revenue (Platinum/Gold/Standard).

## Q4. What is the difference between a Calculated Column and a Measure?
Calculated Column: row-level, stored, static.
Measure: dynamic, context-aware, calculated during interactions.

## Q5. Best practices when creating Calculated Columns.
Prefer Power Query when possible, minimize added columns, use simple DAX, add only required fields.

## Q6. When should you avoid using Calculated Columns?
Avoid when computation can be done in Power Query or when dynamic recalculation is required.

## Q7. How do you group data in Power BI using Power Query?
Home → Group By → Choose columns → Select aggregation → Apply.

## Q8. Aggregation options available while grouping.
Sum, Min, Max, Average, Median, Count, Count Distinct, All Rows.

## Q9. Scenario where grouping is necessary.
Summarizing sales per customer, preparing dimension tables, reducing row-level granularity.

## Q10. Difference between Pivoting and Unpivoting in Power BI.
Pivot: turns row values into columns.
Unpivot: turns columns into rows (normalizes data).

## Q11. How does Unpivoting help normalize tabular data?
It converts wide-format data into tidy long-format, enabling proper analysis and modeling.

## Q12. What is the purpose of merging queries in Power BI?
To combine tables based on keys, enrich datasets, and integrate multiple sources.

## Q13. How is Merge different from Append in Power Query?
Merge = join tables side-by-side.
Append = stack tables vertically.

## Q14. Types of join operations available during Merge.
Left Outer, Right Outer, Full Outer, Inner, Left Anti, Right Anti.
