'''

'openpyxl' is Python library used to work with excels, spreadsheets
create new Excel files,read existing Excel files,write data into cells
delete rows and column, work with multiple sheets
'''
#How to install :python -m pip install openpyxl
import openpyxl
#Reading an existing Excel file
workbook=openpyxl.load_workbook("C:\\Users\\Ammu\\Downloads\\student_data.xlsx")
sheet=workbook["data"]
print(sheet["A2"].value)
print(sheet["B2"].value)

#Reading all rows from excel file
for row in sheet.iter_rows(values_only=True):
    print(row)
print(sheet.max_row)
print(sheet.max_column)
