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


def calculate_time_diff(a:TimeObj, b:TimeObj):

    time_diff = abs(a.hour - b.hour)*60 + abs(a.minute - b.minute)
    if a.hour > b.hour:
        if(a.minute >)
    elif a.hour < b.hour:

    return time_diff

def main():

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

    #print(list_of_data_points[0][1].hour)
    a = TimeObj(12, 15)
    b = TimeObj(10, 10)
    print(calculate_time_diff(a, b))


if __name__ == '__main__':
    main()