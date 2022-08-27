import random
import pandas as pd
import csv
from classes import TimeObj


# Random data generator. It creates univariate time data using the TimeObj Class.
def random_time_points(start, end, num):
    random_list = []

    # Creating |num| data points that contain an X variable and a TimeObj object.
    for i in range(num):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        random_element = [random.randint(start, end), TimeObj(hour, minute)]
        random_list.append(random_element)

    # Returning the list of random data to main function.
    return random_list


#
def main():
    header = ['X', 'H', 'M']

    random_list = random_time_points(1, 100, 100)
    save_list = []

    for i in range(len(random_list)):
        element = [random_list[i][0], random_list[i][1].hour, random_list[i][1].minute]
        save_list.append(element)

    with open("datasetTimeSmall.csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(save_list)

    df = pd.read_csv('datasetTimeSmall.csv')
    modifieddf = df.dropna()
    modifieddf.to_csv('datasetTimeSmall.csv', index=False)


if __name__ == '__main__':
    main()