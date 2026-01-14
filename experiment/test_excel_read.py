import pandas as pd

# Read the Excel file
file_path = r'D:\Code\DataAgent\ExcelData\Covid Dashboard.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Extract the first row data
first_row_data = df.iloc[0].tolist()

# Display the first row data
print("First row data:", first_row_data)
