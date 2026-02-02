#xlrd wont support xlsx innew versions , so degrade to pip install xlrd==1.2.0 or else use
import xlrd
location="C:\\Users\\pcinthamani\\Desktop\\Partner Team Management\\Python_learning\\Works\\python_input.xlsx"
open_excel=xlrd.open_workbook(location)
open_sheet=open_excel.sheet_by_index(0)
print(open_sheet.ncols)
print(open_sheet.nrows)
for i in range(open_sheet.ncols):
    print(open_sheet.col_values(i,0))