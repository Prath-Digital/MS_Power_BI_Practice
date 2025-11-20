# Power BI Relationships & Schema — Full Q&A

## Q1. How do you create a relationship between two tables in Power BI?

You create a relationship by going to Model view, selecting a field from one table, and dragging it onto the matching field in another table. You can also use Manage Relationships → New.

## Q2. What are the necessary conditions for creating a relationship between tables?

Columns must have compatible data types, one side must contain unique values for one-to-many relationships, and keys should be clean without duplicates.

## Q3. How can you view and edit existing relationships in Power BI?

Open Model view and click any relationship line. Or go to Manage Relationships to delete, edit, or create relationships.

## Q4. What are common errors or issues faced while managing relationships, and how can they be resolved?

Common issues include mismatched data types, duplicate keys, incorrect cardinality, and ambiguous relationships. Clean data and adjust relationship settings to fix.

## Q5. What is a Star Schema? Explain with an example.

A Star Schema has a central fact table connected to multiple dimension tables. Example: Sales fact linked to Date, Product, and Customer dimensions.

## Q6. What is a Snowflake Schema? How is it different from a Star Schema?

Snowflake Schema normalizes dimensions into additional lookup tables. It is more complex than a Star Schema but reduces redundancy.

## Q7. Which schema (Star or Snowflake) is generally preferred in Power BI and why?

Star Schema is preferred because it improves performance, simplifies modeling, and works better with DAX and Power BI’s storage engine.

## Q8. What is the difference between active and inactive relationships in Power BI?

Active relationships filter visuals automatically. Inactive relationships exist but do not apply filters unless activated with DAX like USERELATIONSHIP.

## Q9. How can you activate an inactive relationship using DAX functions?

Use USERELATIONSHIP inside CALCULATE to activate a specific relationship for that calculation.

## Q10. What does cardinality mean in the context of table relationships?

Cardinality describes how data in one table relates to another: One-to-One, One-to-Many, or Many-to-Many.

## Q11. Explain different types of relationship cardinality in Power BI.

One-to-One: Unique keys in both tables.  
One-to-Many: One table has unique keys; the other has repeated keys.  
Many-to-Many: Both tables contain repeated values.

## Q12. How does incorrect cardinality affect the results of a data model or report?

It can cause duplicated values, incorrect aggregations, unwanted filter propagation, and inaccurate visuals.
