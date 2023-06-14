import matplotlib.pyplot as plt
import datetime


def show_pie(added_copy):
    # Обчислення загальної суми значень
    total_sum = sum(added_copy.values())

    # Створення списку для місяців та суми значень
    months = []
    sums = []

    # Отримання місяця та суми значень для кожного елемента словника
    for date, value in added_copy.items():
        month = date.strftime('%B')  # Отримання назви місяця
        if month not in months:
            months.append(month)
            sums.append(0)
        index = months.index(month)
        sums[index] += value

    def autopct_format(percentage):
        total = sum(sums)
        value = total * percentage/ 100
        return f'{percentage:.1f}%\n{value:.0f}'

    plt.pie(sums, labels=months, autopct=autopct_format)

    # Додавання заголовка та відображення діаграми
    plt.title('Monthly Distribution')
    plt.show()

