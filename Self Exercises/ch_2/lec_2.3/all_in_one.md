# Power BI Questions and Answers

## Q1. What are Text Tools in Power BI and where can you find them?
Text tools in Power BI include functions like Trim, Clean, Split Column, and more, used for text manipulation. You can find them in the "Transform Data" section under the Power Query Editor.

## Q2. How can you split a column using a delimiter in Power BI?
To split a column using a delimiter, open the Power Query Editor, select the column, go to the "Home" tab, click "Split Column," and choose "By Delimiter." Select your delimiter and apply the changes.

## Q3. What is the purpose of the "Trim" and "Clean" text functions?
The "Trim" function removes leading and trailing spaces from text, while the "Clean" function removes non-printable characters, ensuring cleaner data for analysis.

## Q4. Explain how to extract part of a text string using Power Query Editor.
In Power Query Editor, select the column, go to "Add Column" > "Extract," and choose options like "Text Range" or "First Characters." Define the range or position to extract and apply the transformation.

## Q5. What transformations can be performed using numerical tools in Power BI?
Numerical tools in Power BI allow transformations like rounding, scientific formatting, adding or subtracting values, and converting data types within the Power Query Editor.

## Q6. How do you apply rounding functions (Round, Round Down, Round Up) to a numerical column?
In Power Query Editor, select the numerical column, go to "Add Column" > "Rounding," and choose "Round," "Round Down," or "Round Up." Set the precision and apply the function.

## Q7. What is the difference between Standard and Scientific number formatting?
Standard formatting displays numbers in a typical decimal form (e.g., 1234.56), while Scientific formatting uses exponential notation (e.g., 1.23E+03) for very large or small numbers.

## Q8. How do you extract the day, month, or year from a Date column in Power BI?
In Power Query Editor, select the Date column, go to "Add Column" > "Date," and choose "Day," "Month," or "Year" to extract the desired part into a new column.

## Q9. What is the difference between "Date", "Date/Time", and "Duration" data types?
- "Date" stores only the date (e.g., 08/08/2025).
- "Date/Time" includes both date and time (e.g., 08/08/2025 09:15 PM).
- "Duration" represents a time span (e.g., 5 hours).

## Q10. Explain how Power BI can be used to calculate the difference between two dates.
In Power BI, use DAX to calculate the difference between two dates with the DATEDIFF function. Example: `DATEDIFF(Date1, Date2, DAY)` returns the difference in days.

## Q11. What is the use of "Change Type with Locale" in Power BI?
"Change Type with Locale" adjusts data type conversions based on regional settings, ensuring correct interpretation of formats like dates or currency for different locales.

## Q12. Why is it important to set the correct locale when dealing with regional data (e.g., dates, currency)?
Setting the correct locale ensures proper formatting and interpretation of regional data, avoiding errors in date order (e.g., MM/DD/YYYY vs. DD/MM/YYYY) or currency symbols.