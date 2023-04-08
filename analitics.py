import matplotlib.pyplot as plt

from DataList import DataList


class DataAnalyzer:
    def __init__(self, checked_list, added_list, fire_list, calendar):
        self.checked_list = DataList(checked_list, calendar)
        self.added_list = DataList(added_list, calendar)
        self.fire_list = DataList(fire_list, calendar)
        self.calendar = calendar

    @staticmethod
    def print_values(data_list, comment):
        print(comment)
        print('Mode:', data_list.mode)
        print('Median:', data_list.median)
        print('Mean:', data_list.mean)
        print('Max:', data_list.max_value, data_list.max_date.strftime("%d/%m"))
        print('Min:', data_list.min_value, data_list.min_date.strftime("%d/%m"))
        print('\n')

    def do_analitic(self):
        # Create a figure with three subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
        ax3.set_xlabel('Date')

        # Plot data on each subplot
        ax1.plot(self.calendar, self.added_list.data_list)
        ax2.plot(self.calendar, self.checked_list.data_list)
        ax3.plot(self.calendar, self.fire_list.data_list)

        # Set labels for each subplot
        ax1.set_ylabel('Added')
        ax2.set_ylabel('Checked')
        ax3.set_ylabel('Fire')
        ax3.set_xlabel('Date')

        self.print_values(self.added_list, 'Added')
        self.print_values(self.checked_list, 'Checked')
        self.print_values(self.fire_list, 'Fire')
        plt.show()
