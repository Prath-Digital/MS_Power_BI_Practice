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

## Getting started — run the generators ⚙️

Prerequisites:

- Python 3.8+ installed ✅
- Install required packages:

```bash
python -m pip install pandas openpyxl pypandoc
# (Optional) Install the pandoc binary from https://pandoc.org/installing.html
```

Generate the sample Excel workbook (`Data/9.1.xlsx`):

```bash
cd Data
python .py
```

Generate the Power BI Q&A markdown (writes `powerbi_qa.md`):

```bash
python "Self Exercises/ch_2/lec_2.4/generate_powerbi_qa.py"
```

Notes:
- If `pypandoc`/`pandoc` are not available the script will fall back to writing the markdown file directly.
- `Data/9.1.xlsx` is small and intended for learning and demos — feel free to regenerate.

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

## Next steps I can help with 🧩

- Add a `requirements.txt` and pin package versions.
- Commit `Data/9.1.xlsx` to the repo if you want the workbook tracked (otherwise it can be regenerated).
- Create a sample PBIX with a few measures and visuals using the generated data.

---

If you want this README adjusted (tone, more emojis, fewer emojis, or more technical detail), tell me which style you prefer and I'll update it. 🙌
