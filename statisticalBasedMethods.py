# Anomaly Detection Methods based on statistical approach

from numpy import array
from classes import*
import csv
import time


def get_data():

    with open('datasetSmall.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


def check_bin(num):

    if 0 < num < 10:
        return 1
    elif 10 <= num < 20:
        return 2
    elif 20 <= num < 30:
        return 3
    elif 30 <= num < 40:
        return 4
    elif 40 <= num < 50:
        return 5
    elif 50 <= num < 60:
        return 6
    elif 60 <= num < 70:
        return 7
    elif 70 <= num < 80:
        return 8
    elif 80 <= num < 90:
        return 9
    elif 90 <= num <= 100:
        return 10


def create_histogram(w, data_points):

    histogram_x = Histogram()
    histogram_y = Histogram()

    for i in range(int(100/w)):
        histogram_x.bins.append(Bin())
        histogram_y.bins.append(Bin())

    for i in range(len(data_points)):
        for j in range(2):
            if j == 0:
                number = data_points[i].values[0]
                bin_num = check_bin(number)
                histogram_x.bins[bin_num-1].points.append(number)
                histogram_x.bins[bin_num-1].height += 1
                data_points[i].bin_x = bin_num
            elif j == 1:
                number = data_points[i].values[1]
                bin_num = check_bin(number)
                histogram_y.bins[bin_num - 1].points.append(number)
                histogram_y.bins[bin_num - 1].height += 1
                data_points[i].bin_y = bin_num

    list_of_histograms = [histogram_x, histogram_y]
    return list_of_histograms


def calculate_scores(data_points, histograms):

    histogram_x = histograms[0]
    histogram_y = histograms[1]
    for i in range(len(data_points)):
        bin_x = data_points[i].bin_x
        bin_y = data_points[i].bin_y
        score = (1/histogram_x.bins[bin_x - 1].height)*(1/histogram_y.bins[bin_y - 1].height)
        data_points[i].score = score

    results = []
    for i in range(len(data_points)):
        element = [i, data_points[i].score]
        results.append(element)

    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    print(sorted_results)


def main():

    # Setting start time
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

    histograms = create_histogram(10, list_of_data_points)
    calculate_scores(list_of_data_points, histograms)

    # Getting end time
    end_time = time.time()
    print("Time needed for code execution: ", end_time - start_time, " seconds.")


if __name__ == "__main__":
    main()
