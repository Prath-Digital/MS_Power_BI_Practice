# MS_Power_BI_Practice — Repository Overview 🚀📊

Welcome — this repository contains learning resources, data generator scripts, and curated examples to practice Power BI (Power Query, DAX, and report building).

This README is rewritten to be concise, professional, and easy to follow. It includes a collapsible folder structure and clear run instructions.

---

## Quick Links 🔗
- 📁 Project root: `MS_Power_BI_Practice`
- 📂 Data samples: `Data/9.1.xlsx` (workbook with multiple sheets)
- 📝 Key notes: `Self Exercises/ch_6/lec_6.4/all_in_one.md` (DAX Q&A)
- 🛠️ Generator: `Self Exercises/ch_2/lec_2.4/generate_powerbi_qa.py` (creates `powerbi_qa.md`)

---

## Contents (short) 🧭
- Generated sample workbook: `Data/9.1.xlsx` — contains `Customers`, `Products`, `Dates`, `Sales` sheets.
- Calendar: `Data/4.4/Calendar_Unique.csv` — enriched date attributes for time-intelligence.
- DAX reference: `Self Exercises/ch_6/lec_6.4/all_in_one.md` — interview-style Q&A for common DAX functions.

---

## Folder structure (click to expand) 📂👇
<details>
  <summary>📊 <strong>MS_Power_BI_Practice/</strong></summary>

  <details>
    <summary>&nbsp;&nbsp;&nbsp;&nbsp;📁 <strong>Data/</strong></summary>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(All data-related files and generated workbooks.)
  </details>

  <details>
    <summary>&nbsp;&nbsp;&nbsp;&nbsp;📝 <strong>Self_Exercises/</strong></summary>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Practice exercises and scripts for Power BI concepts.)
  </details>

  <details>
    <summary>&nbsp;&nbsp;&nbsp;&nbsp;🧪 <strong>Lab_Work/</strong></summary>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Completed lab tasks and exercises.)
  </details>

  &nbsp;&nbsp;📘 <strong>README.md</strong> — Overview file
</details>


---

## Why this repo is useful 🔍

- Reproducible sample data for Power BI report development.
- Examples of DAX functions and patterns for interview preparation.
- A simple data-generator pipeline you can extend for training or classroom exercises.

---

## Best practices & recommendations ✅

- Use the `Calendar_Unique.csv` (or a proper Date table) for time-intelligence functions and relationship-based calculations.
- Prefer data-driven mappings (lookup tables + relationships) over hard-coded SWITCH statements in measures.
- Use `CONCATENATEX` with caution on very large sets; consider pre-aggregation or sampling for performance testing.

---
<details>
  <summary><h2>📊 Power BI Lab & Practice Progress <code>(click to expand)</code></h2></summary>
  <img src="https://img.shields.io/badge/Lab%20work%20and%20Self%20exercises-f2c811?logo=googleanalytics&logoColor=f2c811&label=Power%20BI" alt="Power BI Lab work and Self exercises">
  <hr style="background:transparent;">
  <table style="width:100%;border-collapse:collapse;font-family:'cascadia code','Segoe UI',Arial,sans-serif;">
  <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">1</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Introduction Microsoft Power Bi</b></td>
      </tr>
      <tr style="background:#fff; color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">1.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#d32f2f;">What is Power BI</span></li>
            <li><span style="color:#1976d2;">Application of Power BI</span></li>
            <li><span style="color:#388e3c;">Installation of Power BI</span></li>
            <li><span style="color:#fbc02d;">Business Analyst v/s Data Analyst</span></li>
            <li><span style="color:#d32f2f;">Power BI Components</span></li>
            <li><span style="color:#1976d2;">Tableau V/s Power BI</span></li>
            <li><span style="color:#388e3c;">Power BI Desktop Interface & Workflow</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_1/lec_1.1/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_1/lec_1.1/">Self Exercises</a></span>
        </td>
      </tr>
      <tr>
        <td colspan="2" style="background:#000;">
          <hr style="border:1px solid #fff; background:transparent; margin:4px 0;">
        </td>
      </tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">2</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Connecting & Shaping Data</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">2.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Types of Data Connectors</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">The Power Query Editor</span></li>
            <li><span style="color:#388e3c;">Table Transformations
            </span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_2/lec_2.1/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_2/lec_2.1/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">2.2</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Storage & Connection Modes</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Connecting to a Database</span></li>
            <li><span style="color:#388e3c;">Extracting Data from the Web</span></li>
            <li><span style="color:#fbc02d;">Data QA & Profiling Tools</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_2/lec_2.2/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_2/lec_2.2/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">2.3</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Text Tools</span></span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Numerical Tools</span></li>
            <li><span style="color:#388e3c;">Date & Time Tools</span></li>
            <li><span style="color:#fbc02d;">Change Type with Locale</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_2/lec_2.3/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_2/lec_2.3/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">2.4</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Index & Conditional Columns</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Calculated Column Best Practices</span></li>
            <li><span style="color:#388e3c;">Grouping & Aggregating</span></li>
            <li><span style="color:#fbc02d;">Pivoting & Unpivoting</span></li>
            <li><span style="color:#7b1fa2;">Merging Queries</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_2/lec_2.4/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_2/lec_2.4/">Self Exercises</a></span>
          <br>
          <span style="color:#ffffff;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/ffffff/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 1 Data Leverager
          </span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">2.5</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Appending Queries</span></span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Appending Files from a Folder</span></li>
            <li><span style="color:#388e3c;">Data Source Settings</span></li>
            <li><span style="color:#fbc02d;">Data Source Parameters</span></li>
            <li><span style="color:#7b1fa2;">Refreshing Queries</span></li>
            <li><span style="color:#d32f2f;">Importing Excel Models</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_2/lec_2.5/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_2/lec_2.5/">Self Exercises</a></span>
          <br>
          <span style="color:#222;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/000000/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 1 Data Leverager
          </span>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">3</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Pr. 1 Data Leverager</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">3.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#d32f2f;"><img src="https://img.icons8.com/ios-filled/16/ff0000/settings.png" style="vertical-align:middle;margin-right:4px;">Submission Of Pr. 1 Data Leverager</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="https://github.com/Prath-Digital/MS_Power_BI_PR.-1-Data-Leverager" target="_blank">Code</a></span>
              </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">4</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Data Modelling</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">4.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Data Modeling</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Database Normalization</span></li>
            <li><span style="color:#388e3c;">Fact & Dimension Tables</span></li>
            <li><span style="color:#fbc02d;">Primary & Foreign Keys</span></li>
            <li><span style="color:#7b1fa2;">Relationships vs. Merged Tables</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_4/lec_4.1/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_4/lec_4.1/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">4.2</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Creating Table Relationships</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Managing & Editing Relationships</span></li>
            <li><span style="color:#388e3c;">Star & Snowflake Schemas</span></li>
            <li><span style="color:#fbc02d;">Active & Inactive Relationships</span></li>
            <li><span style="color:#7b1fa2;">Relationship Cardinality</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_4/lec_4.2/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_4/lec_4.2/">Self Exercises</a></span>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">4.3</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Connecting Multiple Fact Tables</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;"></span>Filter Context & Filter Flow</li>
            <li><span style="color:#388e3c;"></span>Bi-Directional Filters & Ambiguity</li>
            <li><span style="color:#fbc02d;"></span>Hiding Fields from Report View</li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_4/lec_4.3/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_4/lec_4.3/">Self Exercises</a></span>
          <br>
          <span style="color:#000000;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/000000/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 2 Data Modeler
          </span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">4.4</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Model Layouts</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Data Formats & Categories</span></li>
            <li><span style="color:#388e3c;">Creating Hierarchies</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_4/lec_4.4/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_4/lec_4.4/">Self Exercises</a></span>
          <br>
          <span style="color:#ffffff;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/ffffff/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 2 Data Modeler
          </span>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
        <tr style="background:#000;color:#fff;">
          <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
          <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
        </tr>
      </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">5</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>PR. 2 Data Modeler</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">5.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#d32f2f;"><img src="https://img.icons8.com/ios-filled/16/ff0000/settings.png" style="vertical-align:middle;margin-right:4px;">Submission Of Pr. 2 Data Modeler</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="https://github.com/Prath-Digital/MS_Power_BI_PR.-2-Data-Modeler" target="_blank">Code</a></span>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
        <tr style="background:#000;color:#fff;">
          <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
          <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
        </tr>
      </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">6</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>DAX Fundamentals</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">6.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Data Analysis Expressions</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">DAX vs. M Languages</span></li>
            <li><span style="color:#388e3c;">Intro to DAX Calculated Columns</span></li>
            <li><span style="color:#fbc02d;">Intro to DAX Measures</span></li>
            <li><span style="color:#7b1fa2;">Implicit vs. Explicit Measures</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.1/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.1/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">6.2</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Quick Measures</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Calculated Columns vs. Measures</span></li>
            <li><span style="color:#388e3c;">Dedicated Measure Tables</span></li>
            <li><span style="color:#fbc02d;">Understanding Filter Context</span></li>
            <li><span style="color:#7b1fa2;">Step-by-Step DAX Measure Calculation</span></li>
            <li><span style="color:#d32f2f;">DAX Syntax & Operators</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.2/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.2/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">6.3</td>
        <td style="padding:10px 8px;border:2px solid #000;">
            <span style="color:#d32f2f;">Common DAX Function Categories</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Basic Math & Stats Functions</span></li>
            <li><span style="color:#388e3c;">Counting Functions</span></li>
            <li><span style="color:#fbc02d;">Conditional & Logical Functions</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.3/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.3/">Self Exercises</a></span>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">6.4</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">The SWITCH Function</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Common Text Functions</span></li>
            <li><span style="color:#388e3c;">Basic Date & Time Functions</span></li>
            <li><span style="color:#fbc02d;">Joining Data with RELATED</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.4/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.4/">Self Exercises</a></span>
          <br>
          <span style="color:#fff;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/ffffff/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 3 DAX Depo
          </span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">6.5</td>
        <td style="padding:10px 8px;border:2px solid #000;">
            <span style="color:#d32f2f;">The CALCULATE Function</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">DAX Measure Totals</span></li>
            <li><span style="color:#388e3c;">The ALL Function</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.5/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.5/">Self Exercises</a></span>
          <br>
          <span style="color:#222;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/000000/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 3 DAX Depo
          </span>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">6.6</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">The FILTER Function</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Iterator (X) Functions</span></li>
            <li><span style="color:#388e3c;">Time Intelligence Patterns</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_6/lec_6.6/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_6/lec_6.6/">Self Exercises</a></span>
          <br>
          <span style="color:#fff;font-weight:bold;display:inline-block;margin-top:8px;margin-left:8px;">
            <img src="https://img.icons8.com/ios-filled/16/ffffff/settings.png" style="vertical-align:middle;margin-right:4px;">
            PR. 3 DAX Depo
          </span>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">7</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>PR. 3 DAX Depo</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">7.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#d32f2f;"><img src="https://img.icons8.com/ios-filled/16/ff0000/settings.png" style="vertical-align:middle;margin-right:4px;">Submission Of Pr. 3 DAX Depo</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="https://github.com/Prath-Digital/MS_Power_BI_PR.-3-DAX-Depo" target="_blank">Code</a></span>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">8</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Assignment</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">8.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#d32f2f;"><img src="https://img.icons8.com/ios-filled/16/ff0000/book.png" style="vertical-align:middle;margin-right:4px;">Assignment</span></li>
            <li><span style="color:#222;font-weight:bold;"><img src="https://img.icons8.com/ios-filled/16/000000/settings.png" style="vertical-align:middle;margin-right:4px;">PR. Final Project</span></li>
          </ul>
        </td>
      </tr>
      <tr><td colspan="2" style="background:#000;"><hr style="border:1px solid #fff;"></td></tr>
      <thead>
      <tr style="background:#000;color:#fff;">
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">No.</th>
        <th style="padding:10px 8px;border:2px solid #fff;background:#000;">Topics</th>
      </tr>
    </thead>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">9</td>
        <td style="padding:10px 8px;border:2px solid #fff;"><b>Visualizing Data With Report</b></td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">9.1</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">The Key Questions</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Dashboard Design Framework</span></li>
            <li><span style="color:#388e3c;">Sketching the Dashboard Layout</span></li>
            <li><span style="color:#fbc02d;">Adding Report Pages & Objects</span></li>
            <li><span style="color:#7b1fa2;">Naming & Grouping Objects</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.1/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.1/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">9.2</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Cards & Multi-Row Cards</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Building & Formatting Charts</span></li>
            <li><span style="color:#388e3c;">Line Charts</span></li>
            <li><span style="color:#fbc02d;">Trend Lines & Forecasts</span></li>
            <li><span style="color:#7b1fa2;">KPI Cards</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.2/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.2/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">9.3</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Bar & Donut Charts</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Basic Filtering Options</span></li>
            <li><span style="color:#388e3c;">Table & Matrix Visuals</span></li>
            <li><span style="color:#fbc02d;">Conditional formatting</span></li>
            <li><span style="color:#7b1fa2;">Top N Filtering</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.3/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.3/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">9.4</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Top N Text Cards</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Map Visuals</span></li>
            <li><span style="color:#388e3c;">Report Slicers</span></li>
            <li><span style="color:#fbc02d;">Gauge Charts</span></li>
            <li><span style="color:#7b1fa2;">Advanced Conditional Formatting</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.4/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.4/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">9.5</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Area Charts</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Drill Up & Drill Down</span></li>
            <li><span style="color:#388e3c;">Drillthrough Filters</span></li>
            <li><span style="color:#fbc02d;">Editing Report Interactions</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.5/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.5/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#222;color:#fff;">
        <td style="padding:10px 8px;border:2px solid #fff;">9.6</td>
        <td style="padding:10px 8px;border:2px solid #fff;">
            <span style="color:#d32f2f;">Adding Bookmarks</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Custom Navigation Buttons</span></li>
            <li><span style="color:#388e3c;">Slicer Panels</span></li>
            <li><span style="color:#fbc02d;">Numeric Range Parameters</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.6/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.6/">Self Exercises</a></span>
        </td>
      </tr>
      <tr style="background:#fff;color:#000;">
        <td style="padding:10px 8px;border:2px solid #000;">9.7</td>
        <td style="padding:10px 8px;border:2px solid #000;">
        <span style="color:#d32f2f;">Fields Parameters</span>
          <ul style="margin:0;padding-left:18px;">
            <li><span style="color:#1976d2;">Custom Tool Tips</span></li>
            <li><span style="color:#388e3c;">Importing Custom Visuals</span></li>
            <li><span style="color:#fbc02d;">Managing & Viewing Roles</span></li>
            <li><span style="color:#7b1fa2;">Mobile Layouts</span></li>
          </ul>
          <span style="color:#fff;background:#7b1fa2;padding:2px 6px;border-radius:4px;"><a style="color:#fff;text-decoration:none;" href="Lab Work/ch_9/lec_9.7/">Lab Work</a></span>
          <span style="color:#fff;background:#43a047;padding:2px 6px;border-radius:4px;margin-left:8px;"><a style="color:#fff;text-decoration:none;" href="Self Exercises/ch_9/lec_9.7/">Self Exercises</a></span>
        </td>
      </tr>
    </tbody>
  </table>
  <hr style="background:transparent;">
  <blockquote>
    <b>Note:</b> This table tracks my Power BI learning progress, including lab work and self exercises for each topic. I keep updating as I complete more sections!
  </blockquote>
  <br>
  <blockquote>
    <b>Tip:</b> <br>
    If you want any data you can get data from <a href="Data">Data</a>
  </blockquote>
  <br>
  <blockquote>
    <b>Sample Project Creating wile learing:</b> <a href="./AdventureWorks%20Project/AdventureWorks.txt">More Info (Click Here)</a>
  </blockquote>
</details>
