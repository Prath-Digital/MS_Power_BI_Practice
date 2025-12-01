# DAX Questions and Answers (All-in-One)

## Q1. What is the purpose of mathematical functions in DAX, and give two commonly used functions.
**A:** Mathematical functions in DAX are used to perform arithmetic calculations on numeric data. They help derive new metrics, KPIs, and computed values.  
Common examples: `SUM()`, `ROUND()`.

---

## Q2. How does the ROUND() function work in DAX?
**A:** `ROUND(number, num_digits)` rounds a number to the specified number of decimal places.  
- Positive `num_digits` → decimals  
- Zero → nearest whole number  
- Negative → round to tens/hundreds/etc.

---

## Q3. Explain the use of SUMX() and how it differs from SUM().
**A:** `SUMX(table, expression)` iterates row-by-row over a table, evaluates the expression for each row, then sums the results.  
`SUM(column)` simply adds up the values in a single column.  
Use `SUMX()` when a calculation must occur per row before summing.

---

## Q4. How does AVERAGE() differ from AVERAGEX() in DAX?
**A:**  
- `AVERAGE(column)` computes the mean of values in a column.  
- `AVERAGEX(table, expression)` evaluates an expression per row, then averages the results.  
Use `AVERAGEX()` when the value being averaged is derived.

---

## Q5. What does the COUNT() function return in DAX?
**A:** `COUNT(column)` returns the number of non-blank numeric values in a column.

---

## Q6. When would you use COUNTA() over COUNT()?
**A:** Use `COUNTA()` when you want to count **non-blank values of any data type**, not just numbers.

---

## Q7. How is COUNTROWS() used in Power BI reports?
**A:** `COUNTROWS(table)` returns the number of rows in a table or table expression. It’s useful for counting transactions, rows after filtering, or table outputs of DAX functions like `FILTER()`.

---

## Q8. What’s the purpose of DISTINCTCOUNT() in analyzing data?
**A:** `DISTINCTCOUNT(column)` counts the number of unique values in a column. Useful for counting unique customers, unique products, unique logins, etc.

---

## Q9. What is the syntax of the IF() function in DAX, and how is it used?
**A:**  
```
IF(condition, true_result, false_result)
```
It evaluates a condition and returns one value when the condition is true and another when false. Used for conditional calculations.

---

## Q10. Explain the difference between IF() and SWITCH() in Power BI.
**A:**  
- `IF()` handles simple true/false logic.  
- `SWITCH()` is better for multiple conditions or mapping one value to several outputs, making formulas cleaner.

---

## Q11. How do logical operators like && and || function in DAX formulas?
**A:**  
- `&&` = logical AND (both conditions must be true).  
- `||` = logical OR (at least one condition must be true).  
Used in filtered expressions and conditional logic.

---

## Q12. Give an example scenario where IFERROR() is useful in DAX calculations.
**A:** `IFERROR(value, alternateResult)` is useful when a formula may produce invalid outputs (division by zero, blank lookups, etc.).  
Example:  
```
IFERROR([Total Sales] / [Order Count], 0)
```
Prevents report errors by replacing them with a fallback value.