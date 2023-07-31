# clean up the CSV data for the format you want!
import csv


def scrub_the_csv():
    cleaned_data = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '[', ']']

    def clean_data(element, colnum, rownum):
        index = 0
        name = ''
        number = ''
        symbol = ''
        weight = ''

        while index < len(element) and element[index] not in numbers:
            if element[index] == 'Â':
                index += 2
            else:
                name += element[index]
                index += 1

        while index < len(element) and element[index] in numbers:
            number += element[index]
            index += 1

        while index < len(element) and element[index] not in numbers:
            if element[index] == 'â':
                index += 3
            else:
                symbol += element[index]
                index += 1

        while index < len(element):
            if element[index] in numbers:
                weight += element[index]
            index += 1

        return [name, number, symbol, weight, colnum, rownum]

    with open('Periodic Data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        # skip row 1 and 2 since those are headers
        for row in reader:
            # print(row)
            if count > 1:
                for i in range(len(row)):
                    if len(row[i]) > 1 and row[i] != 'Period 1':
                        cleaned_data.append(clean_data(row[i], i, count))
            count += 1

    # print(cleaned_data)
    return cleaned_data


scrub_the_csv()
