import random
import csv
import pandas as pd


# Random points generator, returns list that contains the random points to  main  function
def random_points(start, end, num):
    random_list = []
    for i in range(num):
        random_element = []
        for j in range(2):
            random_element.append(random.randint(start, end))
        random_list.append(random_element)

    return random_list


# Main function. Gets random points, formats them and saves them in a csv file.
def main():

    # Setting header for csv file
    header = ['X', 'Y']

    # Getting random points
    random_list = random_points(1, 100, 100)

    # Creating the csv file, and inserting data
    with open("datasetSmall.csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(random_list)

    # Using pandas dataframe functions to modify the content of the file
    df = pd.read_csv('datasetSmall.csv')
    modifieddf = df.dropna()
    modifieddf.to_csv('datasetSmall.csv', index=False)


if __name__ == "__main__":
    main()
