import datetime

import matplotlib.pyplot as plt
from DataList import DataList
import numpy as np
from scipy.stats import linregress
from matplotlib.dates import date2num
import pandas as pd
from matplotlib.animation import FuncAnimation
from statsmodels.tsa.arima_model import ARIMA


class DataAnalyzer:
    def __init__(self, calendar, comment, *data_lists):
        self.data_lists = [
            DataList(data_list[0], data_list[1]) for data_list in data_lists
        ]
        self.calendar = calendar
        print(comment, end="\n" * 3)

    @staticmethod
    def print_values(data_list, calendar):
        print(data_list.name, end="\n" * 2)
        # print('Mode:', data_list.mode)
        # print('Median:', data_list.median)
        print('Mean:', data_list.mean)
        print('Max:', data_list.max_value, calendar[data_list.data_list.index(data_list.max_value)].strftime("%d/%m"))
        print('Min:', data_list.min_value, calendar[data_list.data_list.index(data_list.min_value)].strftime("%d/%m"))
        print('Sum:', data_list.sum)
        print()

    def week_analytics(self, data_list, calendar):
        data = list()
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        calendars = []
        for i in range(7):
            data.append(list())
            calendars.append(list())

        for i, day in enumerate(calendar):
            data[day.weekday()].append(data_list.data_list[i])
            calendars[day.weekday()].append(day)

        analyzed_data = [
            DataList(future_analyzed_list, data_list.name + " " + weekdays[i]) for i, future_analyzed_list in
            enumerate(data)
        ]

        for i in range(7):
            self.print_values(analyzed_data[i], calendars[i])

    def do_analytics(self):
        self.prints_lists_values()
        # self.linregress()
        # self.moving_average()
        # self.arima(5, 0, 0)

    def prints_lists_values(self):
        for data_list in self.data_lists:
            # self.print_values(data_list, self.calendar)
            self.week_analytics(data_list, self.calendar)

    def update_plot(self, j, lines, x_data, y_data):
        for k, line in enumerate(lines):
            x_data = self.calendar.strftime("%d/%m")

            slope, intercept, r_value, p_value, std_err = linregress(x_data[:j + 1],
                                                                     self.data_lists[k].data_list[:j + 1])
            line.set_data(x_data[:j + 1], slope * x_data[:j + 1] + intercept)
        return lines

    def linregress_animation(self):
        fig, axs = plt.subplots(len(self.data_lists), 1)

        lines = []
        for i, data_list in enumerate(self.data_lists):
            x_data = date2num(self.calendar)
            y_data = data_list.data_list
            axs[i].scatter(x_data, y_data)
            line, = axs[i].plot(x_data, y_data, 'r-')
            lines.append(line)

        anim = FuncAnimation(fig, self.update_plot, fargs=(lines, x_data, y_data), frames=len(x_data) - 1, interval=200,
                             blit=True)

        plt.show()

    def linregress(self):
        fig, axs = plt.subplots(len(self.data_lists), 1)

        for i, data_list in enumerate(self.data_lists):
            x_data = date2num(self.calendar)

            for j in range(1, len(data_list.data_list)):
                slope, intercept, r_value, p_value, std_err = linregress(x_data[:j], data_list.data_list[:j])

                axs[i].cla()
                axs[i].scatter(x_data[:j], data_list.data_list[:j])
                axs[i].plot(self.calendar[:j], slope * x_data[:j] + intercept, 'r')
                plt.pause(0.2)

        plt.show()

    def moving_average(self):
        fig, axs = plt.subplots(len(self.data_lists), 1)

        for i, data_list in enumerate(self.data_lists):
            for j in range(1, len(data_list.data_list)):
                axs[i].cla()
                rolling_mean = pd.Series(data_list.data_list[:j]).rolling(window=7).mean()

                axs[i].plot(self.calendar[:j], data_list.data_list[:j])
                axs[i].plot(self.calendar[:j], rolling_mean, 'r')
                axs[i].set_ylabel(data_list.name)
                axs[i].set_xlabel('Date')
                plt.pause(0.2)
        plt.show()

    def arima(self, p, d, q):
        fig, axs = plt.subplots(len(self.data_lists), 1)

        for i, data_list in enumerate(self.data_lists):
            model = ARIMA(data_list.data_list, order=(p, d, q))
            model_fit = model.fit(disp=0)

            for j in range(len(data_list.data_list)):
                axs[i].cla()
                axs[i].plot(self.calendar[:j], data_list.data_list[:j], label='Actual')
                axs[i].plot(self.calendar[:j], model_fit.predict(start=0, end=j), label='Predicted')
                axs[i].set_ylabel(data_list.name)
                axs[i].set_xlabel('Date')
                axs[i].legend()
                plt.pause(0.2)
        plt.show()
