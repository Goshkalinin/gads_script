"""
Модуль для подготовки csv-шки для основного скрипта.

Usage: $python3  prepare_data.py Cardstatus.csv
"""

import csv
import sys


def prepare_data_csv(products_csv):
    """
    Preraring data.csv.

    Args:
        products_csv (str): path to main file
    """
    data_list = []

    status = 4  # D
    status_appruved = ['Товар на сайте', 'На сайте только по прямой ссылке, доступен к продаже']

    category = 13  # N
    category_declined = ['ACCESSSW']

    web_allow = 27  # AB

    name = 7
    title = 8  # название конечного раздела
    description_ru = 9
    description_en = 10
    url = 11
    derection = 12
    category = 13
    product_type = 14
    vendor = 15

    with open(products_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # пропускаем хедер

        for row in reader:
            new_row = []
            if row[status] in status_appruved and row[category] not in category_declined and row[web_allow] == 'Y':
                new_row.append(row[name])
                new_row.append(row[title])  # название конечного раздела
                new_row.append(row[description_ru])
                new_row.append(row[description_en])
                new_row.append(row[url])
                new_row.append(row[derection])
                new_row.append(row[category])
                new_row.append(row[product_type])
                new_row.append(row[vendor])

                data_list.append(new_row)

    with open('data.csv', 'w', encoding='utf-8') as final_csv:
        writer = csv.writer(final_csv)
        header = [
            'Name',
            'Title',
            'Description RU',
            'Description EN',
            'URL',
            'Derection',
            'Category',
            'Product Type',
            'Vendor',
            'Headline 7',
            'Headline 8',
            'Headline 9',
            ]
        writer.writerow(header)

        counter = 0
        for row in data_list:
            counter += 1
            writer.writerow(row)
        print(counter)


if __name__ == '__main__':
    prepare_data_csv(sys.argv[1])
