from numpy import array
from classes import DataPoint
import csv
import math
import time


# Help functions
def get_data():

    with open('dataset.csv', newline='') as f:
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


# Global method -Outlier score is set to  be the average to distance to the average distance
# of the data point to its k-nearest neighbors.
def k_nn(list_of_data_points, k):

    scores = []
    sum_of_dist = 0
    for obj in list_of_data_points:
        for i in range(k):
            sum_of_dist += obj.distances[i]
        avg_distance = sum_of_dist/k
        scores.append([list_of_data_points.index(obj), avg_distance])
        sum_of_dist = 0

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print(sorted_scores)


# Global method - Outlier score is set to be the distance to the k-th neighbor
def k_nn_th(list_of_data_points, k):

    scores = []
    i = 0
    for obj in list_of_data_points:
        scores.append([list_of_data_points.index(obj), obj.distances[k-1]])
        i += 1
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print(sorted_scores)


def main():
    # Setting the start time
    start_time = time.time()

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
            list_of_data_points[i].distances.append(calculate_distance
                                                    (list_of_data_points[i], list_of_data_points[j]))

    for obj in list_of_data_points:
        obj.distances.sort()

    k_nn_th(list_of_data_points, 5)
    # Getting the end time
    end_time = time.time()
    print("Time needed for code execution: ", end_time - start_time, " seconds.")


if __name__ == "__main__":
    main()
