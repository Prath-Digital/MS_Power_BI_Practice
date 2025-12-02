# Power BI - Common DAX Functions - Self Exercises

This document contains compact Q&A style explanations, DAX syntax examples, real-world usage scenarios, and best-practice notes for commonly used DAX functions:
- SWITCH, IF comparison
- Text functions (LEFT, RIGHT, CONCATENATE, CONCATENATEX, etc.)
- Date/Time functions (TODAY, NOW, DATEDIFF, etc.)
- RELATED function

---

## Q1. What is the purpose of the SWITCH function in DAX?
**Answer:**
SWITCH simplifies multi-condition branching. It evaluates an expression or a set of boolean tests and returns the first matching result (or a default value if there is no match). There are two typical forms:

- SWITCH(expression, value1, result1, value2, result2, ..., [else_result]) — compares `expression` to each listed value.
- SWITCH(TRUE(), cond1, result1, cond2, result2, ..., [else_result]) — commonly used to check boolean conditions (emulates an IF-ELSE chain).

Examples:
```
-- Match single value
SWITCH( [Region],
		"East", "E",
		"West", "W",
		"Central", "C",
		"Other"
)

-- Use TRUE() to evaluate boolean ranges
SWITCH(
	TRUE(),
	[Revenue] > 1000000, "Platinum",
	[Revenue] > 500000, "Gold",
	[Revenue] > 100000, "Silver",
	"Standard"
)
```

**Why use it:** It makes branching logic much more readable than deep nested IFs when you have many discrete branches.

---

## Q2. How does SWITCH compare to nested IF statements?
**Answer:**

- **Readability:** SWITCH is generally more readable and maintainable for many branches. A SWITCH clause can be read like a table of value->result mappings; nested IFs become indented and hard to follow.
- **Performance:** For a small number of conditions, performance differences are negligible; for many branches, SWITCH can be more performant in practice because the engine can short-circuit efficiently.
- **Use-case differences:** Use nested IFs when your conditions are complex boolean expressions that can't be easily represented via expression-to-value mapping. However, you can also use SWITCH(TRUE(), ...) to emulate nested IF logic in a clearer way.

Example of nested IF vs SWITCH(TRUE()):
```
-- Nested IF (hard to read)
IF([Score] >= 90, "A",
	 IF([Score] >= 80, "B",
			IF([Score] >= 70, "C", "D")))

-- Using SWITCH(TRUE()) (more readable)
SWITCH(
	TRUE(),
	[Score] >= 90, "A",
	[Score] >= 80, "B",
	[Score] >= 70, "C",
	"D"
)
```

---

## Q3. Give a real-life scenario where using SWITCH in Power BI would be more efficient than IF.
**Answer:**

When mapping product categories, status codes, or exact SKU code values to labels. For example, if a company has 8 specific `ProductCategoryCode` values that map to friendly names, SWITCH is much clearer:
```
Product Category Label =
SWITCH(
	[ProductCategoryCode],
	"A1", "Consumables",
	"B2", "Accessories",
	"C3", "Electrical",
	"D4", "Furniture",
	"Unknown"
)
```

This is more maintainable than nested IFs and less error-prone. Also, if mapping needs to be dynamic and subject to change, consider creating a mapping table and using RELATED or LOOKUPVALUE instead (preferred for maintainability and model-driven logic).

---

## Q4. What are some commonly used text functions in DAX, and what are their purposes?
**Answer:**

- **LEFT(text, n):** Returns the first n characters from the left of `text`.
- **RIGHT(text, n):** Returns the last n characters from the right of `text`.
- **MID(text, start, num_chars):** Returns `num_chars` characters starting at `start` position (1-based).
- **LEN(text):** Returns the number of characters (length).
- **TRIM(text):** Removes extra spaces — trims leading and trailing spaces and extra spaces inside? Note: TRIM in DAX removes leading/trailing spaces; use SUBSTITUTE for internal whitespace removal.
- **SUBSTITUTE(text, old_text, new_text, [occurrence]):** Replace text occurrences.
- **REPLACE(old_text, start_num, num_chars, new_text):** Replaces portion of text with new text
- **FIND(substring, text, [start], [not_found_value]) / SEARCH:** Search for substring; SEARCH is case-insensitive, FIND is case-sensitive.
- **CONCATENATE(text1, text2):** Concatenate two strings (legacy) — prefer `&` or `CONCATENATEX` for multiple items.
- **CONCATENATEX(table, expression, delimiter, [orderByExpression], [order])**: Concatenate values from a table column or expression across rows using a delimiter (very powerful for combining row values).
- **UPPER, LOWER, PROPER:** Case conversion functions.
- **FORMAT:** Convert numeric/date values into formatted strings.

Examples:
```
ProductPrefix = LEFT([SKU], 3)
AreaCode = RIGHT([Phone], 4)
FullName = [FirstName] & " " & [LastName]
Tags = CONCATENATEX(FILTER(Products, [Active]=1), [TagName], ", ")
```

---

## Q5. How does the LEFT and RIGHT function help in text transformation?
**Answer:**

LEFT and RIGHT extract substrings from the start or end of a text column — useful for parsing codes, getting prefixes/suffixes, or extracting a fixed-width field from an identifier.

Examples:
```
-- Extract SKU prefix
SKU_Prefix = LEFT([SKU], 2)  -- "BR" for SKU "BR-12345"

-- Extract last 3 digits
Last3 = RIGHT([CardNumber], 3)
```

Tips: Combine with FIND/SEARCH for variable positions (e.g., RIGHT after last hyphen). For complex cases, consider using PATHITEM/ PATH or Power Query text transformations.

---

## Q6. Explain how to use CONCATENATE and CONCATENATEX functions in Power BI.
**Answer:**

- **CONCATENATE(text1, text2)** — simple two-argument concatenation. A more common and flexible way is to use the `&` operator: `text1 & text2`.
- **CONCATENATEX(table, expression, delimiter, [orderByExpression], [order])** — iterates over rows in a table and concatenates the evaluation of `expression` for each row with a delimiter. This is excellent for creating a single text string of values from related rows.

Example: Join product tags for a product
```
ProductTags = CONCATENATEX(
	FILTER(ProductTags, ProductTags[ProductID] = Products[ProductID]),
	ProductTags[Tag], ", ",
	ProductTags[Tag],
	ASC
)
```

**Important:** CONCATENATEX is an iterator and can be expensive on large tables, so use it carefully and consider paging or aggregation when necessary.

---

## Q7. What are some basic Date and Time functions used in Power BI DAX?
**Answer:**

- **TODAY()** — returns current date (no time component).
- **NOW()** — returns current date and time.
- **DATE(year, month, day)** — builds a date value.
- **TIME(hour, minute, second)** — builds a time value.
- **YEAR(date), MONTH(date), DAY(date)** — extract date parts.
- **HOUR, MINUTE, SECOND** — extract time parts.
- **EOMONTH(start_date, months)** — end-of-month offset.
- **DATEADD(date, number_of_intervals, unit)** — shift dates by specified interval.
- **DATEDIFF(start, end, unit)** — returns integer difference by unit (DAY, HOUR, MONTH, etc.).
- **WEEKNUM, WEEKDAY** — week number and day-of-week functions.
- **STARTOFMONTH/ENDOFMONTH/STARTOFYEAR/ENDOFYEAR** — time intelligence helpers used by CALCULATE.

---

## Q8. How does the TODAY() function differ from NOW()?
**Answer:**

- **TODAY()** returns only the current date with time component set to midnight (00:00:00). It is commonly used when you need comparisons at a day granularity.
- **NOW()** returns the current date and the current time (timestamp). Use NOW() when you need time-of-day precision.

Additional notes: Both are volatile and evaluated at query runtime; their values will change if the report is refreshed or recalculated. In Power BI Service, these functions use service time which may differ from your local machine's time.

---

## Q9. Describe how the DATEDIFF() function works with an example.
**Answer:**

DATEDIFF(start_date, end_date, interval) returns the count of boundary crossings (integer) between two dates at the granularity of `interval` (SECOND|MINUTE|HOUR|DAY|WEEK|MONTH|QUARTER|YEAR).

Example:
```
DiffDays = DATEDIFF([OrderDate], [ShipDate], DAY)
```

If `OrderDate` is 2024-01-01 and `ShipDate` is 2024-01-04, this returns 3. For months:
```
DATEDIFF(DATE(2024,1,1), DATE(2024,3,1), MONTH)  -- returns 2
```

Tip: Use DATEDIFF for simple calculations; for more advanced inclusive/exclusive logic or custom business logic use calculate or arithmetic with serial date numbers and calendar tables.

---

## Q10. What is the purpose of the RELATED() function in Power BI DAX?
**Answer:**

RELATED retrieves a value from a related row (from the other side of a relationship). It’s used when a row in the current table has a defined relationship to a single related row in another table (most commonly ‘many’ -> ‘one’ direction) and you need to include a column from that related table.

Example: In a `Sales` table with relationship Sales[ProductID] -> Products[ProductID], to get the product category on the Sales row:
```
ProductCategory = RELATED(Products[Category])
```

This returns the single Category value for the related Product row.

---

## Q11. How does the RELATED function make use of relationships in the data model?
**Answer:**

RELATED uses a defined relationship to navigate from the current row to a related single row in another table. For RELATED to work:
- There must be a relationship in the data model (either direct or via chained relationships).
- The relationship cardinality must be compatible (typically many -> one when you're using RELATED in the many side).
- If there’s no related row, RELATED returns BLANK().

When using DirectQuery, RELATED may translate to joins in the back-end SQL query — this can affect performance, so keep relations and filters efficient.

If you need to bring data from the many-side to the one-side (reverse navigation), use RELATEDTABLE or aggregation functions.

---

## Q12. Provide an example of when and why you would use RELATED to fetch data from a related table.
**Answer:**

Use RELATED to denormalize a read-only value from a lookup table into a fact table when creating a calculated column or measure for ease of use or display. For example, when you have a `Sales` table and a `Customers` table:
```
-- Add customer's Region to each sale
CustomerRegion = RELATED(Customers[Region])
```

Why do this:
- It is easier to display and filter by `CustomerRegion` in visuals or further calculations.
- It avoids duplicating complex lookup logic across multiple measures.

Alternative: Instead of precomputing, you can reference RELATED in a measure or use relationships with slicers and measures directly; if the mapping is dynamic or large, consider a mapping table + LOOKUPVALUE or relationship table.

---

## Final tips & best practices
- Prefer lookup tables with relationships (and `RELATED`) over hard-coded SWITCH mappings when the mapping may change.
- Use SWITCH for clarity when mapping a handful of static values. For large or dynamic maps, create a separate table.
- Use CONCATENATEX for row-level aggregation of text values, but be mindful of resource usage on large sets.
- Use DATE and TIME DAX functions consistently together with a date (calendar) table for reliable time intelligence (and use model relationships with the calendar table).
- When in doubt, aim for model-driven solutions (lookup tables + relationships) for maintainability and performance.

---

If you'd like, I can also:
- Provide a downloadable example PBIX or sample dataset with these functions implemented as calculated columns and measures.
- Convert these questions into a printable single-page cheat sheet.

💡 Tip: For interview-style questions, include both short definitions and short code examples — hiring managers like to see both.


