import numpy as np
from scipy import stats


class DataList:
    def __init__(self, data_list, name):
        self.data_list = data_list
        self.mode = stats.mode(data_list, keepdims=False)[0]
        self.median = np.median(data_list)
        self.mean = np.mean(data_list).round(2)
        self.max_value = max(data_list)
        self.min_value = min(data_list)
        self.name = name
        self.sum = sum(data_list)
