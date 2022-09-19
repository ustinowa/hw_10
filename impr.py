def read_file_1(path='phone1.csv'):
    import csv
    data = []
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            data.append(row)

    return data


def read_file_2(path='phone2.csv'):
    import csv
    data = []
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            print(row)

    return data


