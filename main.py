from openpyxl import load_workbook
from DataPrinter import DataPrinter

file_name = "Copy.xlsx"

data_copy = load_workbook(file_name)
sheet_copy = data_copy.active

data = load_workbook("data.xlsx")
sheet = data.active

added_copy = {}
added = {}
checked = {}
fire = {}

for row in sheet_copy.iter_rows(min_row=2, max_row=sheet_copy.max_row):
    if row[1].value is None:
        break
    added_copy[row[0].value] = row[1].value
    checked[row[0].value] = row[2].value
    fire[row[0].value] = row[3].value

for row in sheet.iter_rows(min_row=2, max_row=sheet_copy.max_row):
    if row[1].value is None:
        break
    added[row[0].value] = row[1].value

checked_list = list(checked.values())
added_copy_list = list(added_copy.values())
added_list = list(added.values())
fire_list = list(fire.values())
calendar = list(checked.keys())

data_printer = DataPrinter(
    calendar,
    file_name,
    (added_copy_list, "Added copy"),
    (added_list, "Added real"),
    (checked_list, "Checked"),
    (fire_list, "Fire")
)
data_printer.do_analytics()
