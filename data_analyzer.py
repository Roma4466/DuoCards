import matplotlib.pyplot as plt
from data_list import *
import numpy as np
from scipy.stats import linregress
from matplotlib.dates import date2num
import pandas as pd
from matplotlib.animation import FuncAnimation
from statsmodels.tsa.arima_model import ARIMA

from data_printer import print_values


def draw_graphics(data_holder, pause_time):
    # lingeress_without_animation(data_holder)
    # moving_average_several_windows(data_holder, pause_time)
    moving_average_several_windows_instant(data_holder)
    # print_ratio(data_holder.data_lists[2].data_list, data_holder.data_lists[0].data_list, data_holder.calendar)


def update_plot(self, j, lines, x_data, y_data):
    for k, line in enumerate(lines):
        x_data = self.calendar.strftime("%d/%m")
        slope, intercept, r_value, p_value, std_err = linregress(x_data[:j + 1],
                                                                 self.data_lists[k].data_list[:j + 1])
        line.set_data(x_data[:j + 1], slope * x_data[:j + 1] + intercept)
    return lines


def linregress_animation(data_holder):
    fig, axs = plt.subplots(len(data_holder.data_lists), 1)
    lines = []
    for i, data_list in enumerate(data_holder.data_lists):
        x_data = date2num(data_holder.calendar)
        y_data = data_list.data_list
        axs[i].scatter(x_data, y_data)
        line, = axs[i].plot(x_data, y_data, 'r-')
        lines.append(line)
    anim = FuncAnimation(fig, update_plot, fargs=(lines, x_data, y_data), frames=len(x_data) - 1, interval=200,
                         blit=True)
    plt.show()


def lingeress_without_animation(data_holder):
    fig, axs = plt.subplots(len(data_holder.data_lists), 1)
    for i, data_list in enumerate(data_holder.data_lists):
        x_data = date2num(data_holder.calendar)
        for j in range(1, len(data_list.data_list)):
            slope, intercept, r_value, p_value, std_err = linregress(x_data[:j], data_list.data_list[:j])
            axs[i].cla()
            axs[i].scatter(x_data[:j], data_list.data_list[:j])
            axs[i].plot(data_holder.calendar[:j], slope * x_data[:j] + intercept, 'r')
            plt.pause(0.2)
    plt.show()


def moving_average_several_windows(data_holder, pause_time):
    for i, data_list in enumerate(data_holder.data_lists):
        plt.figure()  # Create a new figure for each graph
        for j in range(1, len(data_list.data_list)):
            plt.cla()
            rolling_mean = pd.Series(data_list.data_list[:j]).rolling(window=7).mean()

            plt.plot(data_holder.calendar[:j], data_list.data_list[:j], label="Values line")
            plt.plot(data_holder.calendar[:j], rolling_mean, 'r', label="Rolling mean line")

            plt.axhline(data_list.mean, linestyle='--', color='red', label='Mean')

            cumulative_mean = pd.Series(data_list.data_list[:j]).expanding().mean()  # Calculate cumulative mean
            plt.plot(data_holder.calendar[:j], cumulative_mean, 'y', label="Mean line")  # Plot cumulative mean

            plt.ylabel(data_list.name)
            plt.xlabel('Date')
            plt.legend()
            plt.pause(pause_time)
    plt.show()


def moving_average_several_windows_instant(data_holder):
    for i, data_list in enumerate(data_holder.data_lists):
        plt.figure()  # Create a new figure for each graph

        rolling_mean = pd.Series(data_list.data_list).rolling(window=7).mean()
        plt.plot(data_holder.calendar, data_list.data_list, label="Values line")
        plt.plot(data_holder.calendar, rolling_mean, 'r', label="Rolling mean line")
        plt.axhline(data_list.mean, linestyle='--', color='red', label='Mean')
        cumulative_mean = pd.Series(data_list.data_list).expanding().mean()  # Calculate cumulative mean
        plt.plot(data_holder.calendar, cumulative_mean, 'y', label="Mean line")  # Plot cumulative mean
        plt.ylabel(data_list.name)
        plt.xlabel('Date')
        plt.title(data_holder.comment)
        plt.legend()

    plt.show()


def moving_average_one_window(data_holder):
    fig, axs = plt.subplots(len(data_holder.data_lists), 1)
    for i, data_list in enumerate(data_holder.data_lists):
        for j in range(1, len(data_list.data_list)):
            axs[i].cla()
            rolling_mean = pd.Series(data_list.data_list[:j]).rolling(window=7).mean()
            axs[i].plot(data_holder.calendar[:j], data_list.data_list[:j])
            axs[i].plot(data_holder.calendar[:j], rolling_mean, 'r')
            axs[i].axhline(data_list.mean, linestyle='--', color='red', label='Full Sample Mean')
            cumulative_mean = pd.Series(data_list.data_list[:j]).expanding().mean()  # Calculate cumulative mean
            axs[i].plot(data_holder.calendar[:j], cumulative_mean, 'y')  # Plot cumulative mean
            axs[i].set_ylabel(data_list.name)
            axs[i].set_xlabel('Date')
            plt.pause(0.2)
    plt.show()


def print_ratio(checked, added, calendar):
    new_list = DataList([
        (checked[i] / added[i]).round(2) for i in range(len(checked))
    ], "Ratio: checked / added")
    print_values(new_list, calendar)
    # show_data_on_graphic(new_list.data_list, calendar)
    moving_average_several_windows(DataHolder(calendar, "Checked / added ratio", new_list.data_list), 0.01)


def show_data_on_graphic(data_list, calendar):
    plt.plot(calendar, data_list)
    plt.show()

#%%
