import matplotlib.pyplot as plt

from DataList import DataList


class DataPrinter:
    def __init__(self, calendar, comment, *data_lists):
        self.data_lists = [
            DataList(data_list[0], calendar, data_list[1]) for data_list in data_lists
        ]
        self.calendar = calendar
        print(comment, end="\n" * 3)

    @staticmethod
    def print_values(data_list, comment):
        print(comment, end="\n" * 2)
        print('Mode:', data_list.mode)
        print('Median:', data_list.median)
        print('Mean:', data_list.mean)
        print('Max:', data_list.max_value, data_list.max_date.strftime("%d/%m"))
        print('Min:', data_list.min_value, data_list.min_date.strftime("%d/%m"))
        print('Sum:', sum(data_list.data_list))
        print()

    def do_analytics(self):
        for data_list in self.data_lists:
            self.print_values(data_list, data_list.name)

        fig, axs = plt.subplots(len(self.data_lists), 1)

        for i, data_list in enumerate(self.data_lists):
            axs[i].plot(self.calendar, data_list.data_list)
            axs[i].set_ylabel(data_list.name)
            axs[i].set_xlabel('Date')

        plt.show()
