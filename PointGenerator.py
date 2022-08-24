import random
import csv
import pandas as pd


def random_points(start, end, num):
    random_list = []
    for i in range(num):
        random_element = []
        for j in range(2):
            random_element.append(random.randint(start, end))
        random_list.append(random_element)

    return random_list


def main():
    header = ['X', 'Y']

    random_list = random_points(1, 100, 100)
    #for i in range(len(random_list)):
        #print(random_list[i])

    with open("datasetSmall.csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(random_list)

    df = pd.read_csv('datasetSmall.csv')
    modifieddf = df.dropna()
    modifieddf.to_csv('datasetSmall.csv', index=False)


if __name__ == "__main__":
    main()
