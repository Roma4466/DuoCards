import numpy as np
from scipy import stats


class DataList:
    def __init__(self, data_list, calendar, name):
        self.data_list = data_list
        self.calendar = calendar
        self.mode = stats.mode(data_list, keepdims=False)[0]
        self.median = np.median(data_list)
        self.mean = np.mean(data_list).round(2)
        self.max_value = max(data_list)
        self.max_date = self.calendar[data_list.index(self.max_value)]
        self.min_value = min(data_list)
        self.min_date = self.calendar[data_list.index(self.min_value)]
        self.name = name
