import csv
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    title: str  # Название конечного раздела
    description_ru: str
    description_en: str
    url: str
    direction: str
    category: str
    product_type: str
    vendor: str

def get_products(products_csv):
    products = []

    with open(products_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # пропускаем хедер

        for row in reader:
            name = row[0]
            title = row[1] #B
            description_ru = row[2]
            description_en = row[3]
            url = row[4]
            direction = row[5]
            category = row[6] #G
            product_type = row[7] #H
            vendor = row[8]

            products.append(Product(
                name=name,
                title=title,
                description_ru=description_ru,
                description_en=description_en,
                url=url,
                direction=direction,
                category=category,
                product_type=product_type,
                vendor=vendor
            ))

    return products


