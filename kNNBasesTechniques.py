from numpy import array
from classes import DataPoint
import csv
import math


# Help functions
def get_data():

    with open('datasetSmall.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


# Global techniques

# list = [[1, 3], [2, 4]]
# l = array(list)


def calculate_distance(a: DataPoint, b: DataPoint):
    sum_of_values = 0
    for i in range(a.dimensions):
        sum_of_values += pow(a.values[i] - b.values[i], 2)

    return math.sqrt(sum_of_values)


# def k_nn(list_of_points, k):


def main():
    # Reading data file to retrieve data points/
    data = get_data()
    d = array(data)
    dimensions = d.shape[1]

    # Change data type for latter use
    for i in range(len(data) - 1):
        for j in range(2):
            data[i+1][j] = int(data[i+1][j])

    # Creating data points objects
    list_of_data_points = []

    for i in range(len(data) - 1):
        list_of_data_points.append(DataPoint(dimensions, data[i+1]))

    # for obj in list_of_data_points:
        # print(obj.values)

    for i in range(len(list_of_data_points)):
        for j in range(len(list_of_data_points)):
            list_of_data_points[i].distances.append(calculate_distance(list_of_data_points[i], list_of_data_points[j]))

    for obj in list_of_data_points:
        obj.distances.sort(reverse=True)

    print(list_of_data_points[0].distances)


if __name__ == "__main__":
    main()




