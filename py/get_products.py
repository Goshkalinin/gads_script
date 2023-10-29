"""
Собираем коллекцию объектов из продуктовой csv-хи.

Здесь же делаем запросы в GPT.
"""

import csv
import logging
import multiprocessing
from dataclasses import dataclass

from .openai_generate_text import generate_text

logger = logging.getLogger(__name__)


@dataclass
class Product(object):
    """
    Класс для хранения продуктов — по строке на ячейку.

    Логика именования: а штоб оно было похоже на заголовок csv-хи!
    """

    name: str  # cell A; Имя продукта
    title: str  # cell B; Название конечного раздела
    description2: str  # cell C; на русском, подлежит переводу об GPT
    description1: str  # cell D; на английском, подлежит чеку на (!, ...)
    url: str  # cell E, внутренняя ссылка на продукт
    direction: str  # cell F,
    category: str  # cell G, категория продукта
    product_type: str  # cell H, тип продукта
    vendor: str  # cell I,

    headline7: str  # cell J,
    headline8: str  # cell K,
    headline9: str  # cell L,

    description3: str  # to generate!
    description4: str  # to generate!
    headline6: str  # to generate!


def count_total_rows(products_csv):
    """
    Посчитаем, сколько строк в файле.

    Args:
        products_csv (str): path

    Returns:
        total lines
    """
    with open(products_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        line_count = sum(1 for row in reader) - 1

    return line_count


def print_status(total, ctr):
    """
    Выведем, сколько обработано.

    Args:
        total (int): сколько строк в файле
        ctr (int): counter
    """
    message = ' '.join(['Got', str(ctr), 'GPTs', 'of total', str(total)])
    logger.info(message)


def make_description3_prompt(
    manufacturer,
    product_name,
    description1,
    product_type,
    product_category,
):
    """
    Готовим промт для дескрипшна 3.

    Args:
        manufacturer (str): from csv (vendor)
        product_name (str): from csv
        description1 (str): from csv
        product_type (str): from csv
        product_category (str): from csv

    Returns:
        ready prompt!
    """
    to_do = """
    Act like you are an experienced Google ads professional,
    working for a distributor of industrial computers.
    Tone of voice: considerate and simple.
    Write minimum 85 and maximum 90 characters description for product:"""

    return ' '.join([
        to_do,
        product_name,
        'by',
        manufacturer,
        '-',
        description1,
        'in category',
        product_category,
        ])


def make_description4_prompt(
    manufacturer,
    product_name,
    description1,
    product_type,
    product_category,
):
    """
    Готовим промт для дескрипшна 4.

    Args:
        manufacturer (str): from csv (vendor)
        product_name (str): from csv
        description1 (str): from csv
        product_type (str): from csv
        product_category (str): from csv

    Returns:
        ready prompt!
    """
    to_do = """
        Act like you are an experienced Google ads professional,
        working for a distributor of industrial computers.
        Write minimum 75 and maximum 85 characters description for product:"""

    return ' '.join([
        to_do,
        product_name,
        'by',
        manufacturer,
        '-',
        description1,
        'in category',
        product_category,
        ])


def make_headline6_prompt(product_type):
    """
    Готовим промт для хедлайна 6.

    Args:
        product_type (str): from csv

    Returns:
        ready prompt!
    """
    to_do = """
        Act like you are an experienced Google ads professional,
        working for a distributor of industrial computers.
        Write maximum 30 characters headline for product:"""

    return ' '.join([to_do, product_type])


def get_products(products_csv):
    """
    Открвыем csv-ху с продуктами, и построчно её обрабатываем.

    Args:
        products_csv (str): путь к CSV-файлу с продуктами.

    Returns:
        products (list): Список продуктов (объектов их!).
    """
    products = []

    total = count_total_rows(products_csv)
    ctr = 1

    with open(products_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # пропускаем хедер

        for row in reader:
            
            promt_3 = make_description3_prompt(
                    row[8],
                    row[0],
                    row[3],
                    row[7],
                    row[6],
                )
            
            promt_4 = make_description4_prompt(
                    row[8],
                    row[0],
                    row[3],
                    row[7],
                    row[6],
                )

            promt_6 = make_headline6_prompt(
                    row[7],
                )
            
            """
            description2 = multiprocessing.Process(target=generate_text, args=(' '.join(['translate on English:', row[2]]),))  # description_ru
            """
            description2 = ''
            
            
            description3 = multiprocessing.Process(target=generate_text, args=(promt_3,))
                    
            description4 = multiprocessing.Process(target=generate_text, args=(promt_4,))                
                    
            headline6 = multiprocessing.Process(target=generate_text, args=(promt_6,))
                


            # description2.start()
            description3.start()
            description4.start()
            headline6.start()

            
            # description2.join()
            description3.join()
            description4.join()
            headline6.join()
            
            product = Product(
                name=row[0],
                title=row[1],

                description2=description2,

                description1=row[3],  # description_en
                url=row[4],
                direction=row[5],
                category=row[6],
                product_type=row[7],
                vendor=row[8],

                headline7=row[9],
                headline8=row[10],
                headline9=row[11],

                description3=description3,

                description4=description4,

                headline6=headline6,
                )

            print_status(total, ctr)
            ctr += 1
            products.append(product)

    return products


if __name__ == '__main__':
    import time
    start_t = time.time()
    products_csv = 'data_1.csv'
    products_list = get_products(products_csv)
    
    end_t = time.time()
    t = end_t - start_t
    print(t)
