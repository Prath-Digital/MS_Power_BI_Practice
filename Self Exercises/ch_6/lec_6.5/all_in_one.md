# DAX Q&A – All-in-One Markdown

## Q1. What is the purpose of the `CALCULATE()` function in DAX?
`CALCULATE()` changes the filter context and then evaluates an expression under the new filters.

---

## Q2. How does `CALCULATE()` modify filter context in Power BI?
It overrides existing filters or adds new filters before the measure is calculated.

---

## Q3. Provide a simple example of a DAX formula using `CALCULATE()` to compute conditional totals.
```DAX
Total Electronics Sales =
CALCULATE([Total Sales], Products[Category] = "Electronics")
```

---

## Q4. Explain the importance of using `CALCULATE()` in complex DAX measures.
It allows conditional logic, context transition, dynamic filtering, and advanced calculations that depend on custom contexts.

---

## Q5. What are “Measure Totals” in DAX and how do they differ from column totals?
- Column totals = sum of each row in a column.
- Measure totals = recalculated using the **total filter context**, not row-by-row summation.

---

## Q6. Why might a DAX measure not return the expected total value in a visual?
Because totals recompute using a different filter context, not the sum of displayed rows.

---

## Q7. How can you fix incorrect total values in DAX measures in Power BI?
Use functions like:
- `HASONEVALUE()`
- `ISINSCOPE()`
- `SUMX()` over a filtered table  
to control behavior in total rows.

---

## Q8. Explain how `HASONEVALUE()` can help manage total logic in custom DAX measures.
It checks if a column has exactly one value in the current context, letting you return:
- detailed calculation for rows,
- a different calculation for totals.

---

## Q9. What is the purpose of the `ALL()` function in DAX?
It removes filters from columns or tables, allowing full-context calculations.

---

## Q10. How does `ALL()` affect filter context in a visual or calculation?
It clears filters, so the measure is evaluated on the entire dataset instead of the current filtered slice.

---

## Q11. Give an example of using `ALL()` to calculate a grand total or percentage of total.
```DAX
Sales % of Total =
DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Products)))
```

---

## Q12. What is the difference between `ALL()` and `REMOVEFILTERS()` in terms of filter removal?
- `ALL()` removes filters **and returns a table** (useful in iterators).
- `REMOVEFILTERS()` removes filters **only**, without returning a table.
