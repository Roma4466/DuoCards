import pandas as pd
from openpyxl import Workbook, load_workbook
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from datetime import datetime
from analitics import DataAnalyzer

data = load_workbook('Copy.xlsx')
sheet = data.active

added = {}
checked = {}
fire = {}

for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row):
    if row[1].value is None:
        break
    added[row[0].value] = row[1].value
    checked[row[0].value] = row[2].value
    fire[row[0].value] = row[3].value

checked_list = list(checked.values())
added_list = list(added.values())
fire_list = list(fire.values())
calendar = list(checked.keys())

data = DataAnalyzer(checked_list, added_list, fire_list, calendar)
data.do_analitic()