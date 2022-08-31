from classes import *
from numpy import array
import csv
import math
import time


def get_data():

    with open('datasetTimeSmall.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


def calculate_time_diff(a: TimeObj, b: TimeObj):

    time_diff = 0
    if a.hour > b.hour:
        starting = b
        ending = a
    elif a.hour < b.hour:
        starting = a
        ending = b
    else:
        time_diff = abs(a.minute - b.minute)
        return time_diff

    if ending.minute > starting.minute:
        time_diff = abs(a.hour - b.hour) * 60 + abs(a.minute - b.minute)
    elif ending.minute < starting.minute:
        ending.hour -= 1
        ending.minute += 60
        time_diff = abs(a.hour - b.hour) * 60 + abs(a.minute - b.minute)

    return time_diff


def check_r(a, b, r):

    if abs(a - b) < r:
        return True
    else:
        return False


def density_based_outlier_detection(r, time_window, t, data_points):

    outliers = []

    for i in range(len(data_points)):
        entries = []
        for j in range(len(data_points)):
            if check_r(data_points[i][0], data_points[j][0], r):
                if calculate_time_diff(data_points[i][1], data_points[j][1]) < time_window:
                    entries.append(data_points[j])
                else:
                    pass
            else:
                pass

        if len(entries) < t:
            outliers.append([i, data_points[i]])
        else:
            pass

    return outliers


def main():

    # Setting the start time
    start_time = time.time()

    data = get_data()
    d = array(data)
    dimensions = d.shape[1]

    # Change data type for latter use
    for i in range(len(data) - 1):
        for j in range(3):
            data[i + 1][j] = int(data[i + 1][j])

    list_of_data_points = []
    for i in range(len(data)-1):
        list_of_data_points.append([data[i+1][0], TimeObj(data[i+1][1], data[i+1][2])])

    outliers = density_based_outlier_detection(10, 250, 3, list_of_data_points)
    print(len(outliers))
    print(outliers)

    # Getting the end time
    end_time = time.time()
    print("Time needed for code execution: ", end_time - start_time, " seconds.")


if __name__ == '__main__':
    main()