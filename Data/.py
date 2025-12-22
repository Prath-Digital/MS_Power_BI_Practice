import pandas as pd
import glob

# -----------------------------------------
# CONFIG
# -----------------------------------------
input_folder = "./"           # folder where your CSVs are located
output_file = "Combined_Data.xlsx"   # final Excel file name

# -----------------------------------------
# COMBINE CSV → EXCEL (multiple sheets)
# -----------------------------------------
csv_files = glob.glob(input_folder + "/*.csv")

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for file in csv_files:
        sheet_name = file.split("/")[-1].replace(".csv", "")[:31]  # Excel sheet name limit
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"All CSV files combined into: {output_file}")
