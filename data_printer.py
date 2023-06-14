from data_list import DataList


def prints_lists_values(data_holder):
    for data_list in data_holder.data_lists:
        print_values(data_list, data_holder.calendar)
        # week_analytics(data_list, data_holder.calendar)


def print_values(data_list, calendar):
    print(data_list.name, end="\n" * 2)
    print('Mode:', data_list.mode)
    print('Median:', data_list.median)
    print('Mean:', data_list.mean)
    max_value = max(data_list.data_list)
    min_value = min(data_list.data_list)
    print('Max:', max_value, calendar[data_list.data_list.index(max_value)].strftime("%d/%m"))
    print('Min:', min_value, calendar[data_list.data_list.index(min_value)].strftime("%d/%m"))
    print('Sum:', data_list.sum)
    print()


def week_analytics(data_list, calendar):
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
        print_values(analyzed_data[i], calendars[i])
