
# Power BI – Questions and Answers (All-in-One)

---

## Q1. What is a Top N Text Card in Power BI, and how is it used?

**Answer:**  
A **Top N Text Card** is a technique (usually using a Card or Multi-row Card visual with DAX) to display the top *N* items as text based on a ranking measure (such as Sales, Profit, or Quantity). Instead of showing a chart, it presents ranked results in a concise textual format.

**Usage:**
- Display top-performing products, customers, or regions
- Provide executive summaries
- Save dashboard space while highlighting key contributors

---

## Q2. How can you create a Top N value display using DAX with a Card visual?

**Answer:**  
You create a DAX measure that ranks values and concatenates the top results into a single text output.

```DAX
Top 3 Products =
VAR RankedTable =
    TOPN(
        3,
        SUMMARIZE(
            Sales,
            Product[Product Name],
            "TotalSales", [Total Sales]
        ),
        [TotalSales], DESC
    )
RETURN
CONCATENATEX(
    RankedTable,
    Product[Product Name] & " - " & FORMAT([TotalSales], "#,##0"),
    ", "
)
```

Place this measure into a **Card** visual.

---

## Q3. What are the use cases of Top N Text Cards in business dashboards?

**Answer:**  
- Executive KPI summaries  
- Identifying top customers or products  
- Highlighting best-performing regions  
- Mobile-optimized reporting  
- Storytelling dashboards where text insights are preferred

---

## Q4. What are the different types of Map visuals available in Power BI?

**Answer:**  
Power BI provides several map visuals:
- **Map (Bubble Map)**
- **Filled Map (Choropleth)**
- **Azure Maps**
- **Shape Map**
- **ArcGIS Maps for Power BI**

Each visual supports different geographic analysis needs.

---

## Q5. How does Power BI handle geographical data in map visuals?

**Answer:**  
Power BI uses geocoding services (Bing Maps / Azure Maps) to translate location fields into latitude and longitude. It supports:
- Country, State, City, Postal Code
- Explicit Latitude and Longitude fields
- Automatic resolution when data categories are set correctly

---

## Q6. What are the key considerations for enabling accurate mapping in Power BI?

**Answer:**  
- Correct **Data Category** assignment  
- Avoid ambiguous place names  
- Use ISO country codes when possible  
- Provide latitude and longitude for precision  
- Ensure consistent naming and spelling  

---

## Q7. What is a slicer in Power BI and how does it function in a report?

**Answer:**  
A **Slicer** is an interactive filtering visual that allows users to filter report data dynamically.

**Functions:**
- Filters one or more visuals
- Supports single-select and multi-select
- Enables self-service analysis
- Improves report interactivity

---

## Q8. What are the differences between visual-level and report-level slicers?

**Answer:**  

| Filter Level | Scope |
|-------------|-------|
| Visual-level | Affects a single visual |
| Page-level | Affects all visuals on a page |
| Report-level | Affects all pages in the report |

Slicers commonly operate at page or report level.

---

## Q9. How can you customize slicers for a better user experience in interactive reports?

**Answer:**  
- Change slicer orientation (horizontal/vertical)
- Use dropdown slicers for compact layouts
- Enable search
- Sync slicers across pages
- Apply formatting (colors, fonts, borders)
- Combine slicers with bookmarks and buttons

---

## Q10. What are Gauge charts used for in Power BI reports?

**Answer:**  
Gauge charts are used to show **progress toward a goal or target**.

**Common scenarios:**
- Sales vs Target
- Revenue achievement
- KPI performance tracking
- Capacity utilization

---

## Q11. How can you represent target vs actual values using a Gauge chart?

**Answer:**  
You bind:
- **Value** → Actual measure (e.g., Sales)
- **Target Value** → Target measure
- **Minimum** → Usually 0
- **Maximum** → Target or projected maximum

This visually shows how close the actual value is to the target.

---

## Q12. Explain the concept of Advanced Conditional Formatting and give an example of how it can enhance table/matrix visuals in Power BI.

**Answer:**  
**Advanced Conditional Formatting** allows dynamic formatting of visuals based on rules or DAX measures.

**Capabilities:**
- Color scales
- Data bars
- Icons
- Rule-based formatting
- Measure-driven formatting

**Example:**  
Highlight sales performance:
- Green if Sales > Target
- Yellow if Sales within 90–100% of Target
- Red if Sales < 90% of Target

This improves readability and draws attention to critical insights instantly.

---
