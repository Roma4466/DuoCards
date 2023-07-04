import matplotlib
import matplotlib.pyplot as plt
import datetime


def show_pies(*tuples):
    for dictionary_and_name in tuples:
        show_pie(dictionary_and_name[0], dictionary_and_name[1])


def show_pie(dictionary, name):
    months = []
    sums = []

    for date, value in dictionary.items():
        month = date.strftime('%B')
        if month not in months:
            months.append(month)
            sums.append(0)
        index = months.index(month)
        sums[index] += value

    def autopct_format(percentage):
        total = sum(sums)
        value = total * percentage / 100
        return f'{percentage:.1f}%\n{value:.0f}'

    plt.pie(sums, labels=months, autopct=autopct_format)

    plt.title(f'Monthly Distribution of {name}')
    plt.show()
