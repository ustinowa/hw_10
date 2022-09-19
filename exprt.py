def write_file_1(path='phone1.csv'):
    import csv

    phone = [
        ['Ivanov', 'Ivan', '(777)777-77-77', 'Desc'],
        ['Smirnov', 'Pavel', '(999)999-99-99', 'Desc']
    ]

    with open(path, 'w', newline='') as file:
        for record in phone:
            file.write(f'{record[0]}\n{record[1]}\n{record[2]}\n{record[3]}\n\n')

    return path


def write_file_2(path='phone2.csv'):
    import csv

    phone = [
        ['Ivanov', 'Ivan', '(777)777-77-77', 'Desc'],
        ['Smirnov', 'Pavel', '(999)999-99-99', 'Desc']
    ]

    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(phone)

    return path