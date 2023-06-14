import numpy as np
from scipy import stats

"""
DTO for data
"""


class DataList:
    def __init__(self, data_list, name):
        self.data_list = data_list
        self.mode = stats.mode(data_list, keepdims=False)[0]
        self.median = np.median(data_list)
        self.mean = np.mean(data_list).round(2)
        self.name = name
        self.sum = sum(data_list)


class DataHolder:
    def __init__(self, calendar, comment, *data_lists):
        self.data_lists = [
            DataList(data_list[0], data_list[1]) for data_list in data_lists
        ]
        self.calendar = calendar
