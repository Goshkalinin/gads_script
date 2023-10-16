"""Этот модуль записывает группы объявлений в финальную csv."""

import csv

import checkers
from get_header import get_header


def make_keywords(vendor, name):
    """
    Запилим ключевые слова.

    Args:
        vendor (str): product.vendor
        name (str): products.name

    Returns:
        keywords (list)

    """
    keywords = []

    # keyword 1: poduct.name
    keyword = name
    keywords.append(keyword)

    # keyword 2: poduct.vendor
    keyword = name.replace('-', '')
    keywords.append(keyword)

    # keyword 3: poduct.vendor + poduct.name
    keyword = ' '.join([vendor, name])
    keywords.append(keyword)

    # keyword 4: poduct.vendor + poduct.name, last '-$part' replaced with ''
    keyword = ' '.join([vendor, name])
    parts = keyword.split('-')
    keyword = '-'.join(parts[:-1])
    keywords.append(keyword)

    return keywords


def make_ads(products, draft):
    """
    Запишем в подготовленную csv группы объявок.

    Args:
        products (list): лист с продуктами, переработанными в obj
        draft (obj): объект с шаблонными значениями
    """
    with open('final.csv', 'a', encoding='utf-8') as csv_file:

        fieldnames = get_header('final.csv')

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        fourth_keywords = []
        not_writed_products = []

        for product in products:

            # есть ли у нас моральное право объявление пилить?
            if checkers.check_headline_length(product, not_writed_products):
                continue

            # пилим хедер группы объявлений:
            header = {
                'Campaign':
                    draft.campaign,
                'Audience targeting':
                    draft.audience_targeting,
                'Flexible Reach':
                    draft.flexible_reach,
                'Ad Group':
                    product.name,
                'Max CPC':
                    draft.max_cpc,
                'Max CPM':
                    draft.max_cpm,
                'Target CPM':
                    draft.target_cpm,
                'Display Network Custom Bid Type':
                    draft.display_network_custom_bid_type,
                'Optimized targeting':
                    draft.optimized_targeting,
                'Ad Group Type':
                    draft.ad_group_type,
            }

            writer.writerow(header)

            # генерячим ключи:
            keywords = make_keywords(product.vendor, product.name)
            checkers.is_in_fourth_keywords(keywords, fourth_keywords)

            for keyword in keywords:
                writer.writerow({
                    'Campaign': draft.campaign,
                    'Ad Group': product.name,
                    'Keyword': keyword,
                    'Criterion Type': 'Broad',
                    })

            # пилим футер группы объявлений
            writer.writerow({
                'Campaign': draft.campaign,
                'Ad Group': product.name,
                'Final URL':
                    ''.join(['https://ipc2u.com/catalog/', product.url, '/']),
                'Ad type': draft.ad_type,

                'Headline 1': product.vendor,
                'Headline 1 position': '1',
                'Headline 2': product.name,
                'Headline 2 position': '2',
                'Headline 3': product.product_type,
                'Headline 3 position': '3',
                'Headline 4': ' '.join(['buy', product.vendor]),
                'Headline 4 position': '1',
                'Headline 5': product.name,
                'Headline 5 position': '2',
                'Headline 6': 'product.product_type GPT',
                'Headline 6 position': '-',
                'Headline 7': product.headline7,
                'Headline 7 position': '3',
                'Headline 8': product.headline8,
                'Headline 8 position': '3',
                'Headline 9': product.headline9,
                'Headline 9 position': '3',
                'Headline 10': '',
                'Headline 10 position': '',
                'Headline 11': '',
                'Headline 11 position': '',
                'Headline 12': '',
                'Headline 12 position': '',
                'Headline 13': '',
                'Headline 13 position': '',
                'Headline 14': '',
                'Headline 14 position': '',
                'Headline 15': '',
                'Headline 15 position': '',

                'Description 1':
                    checkers.check_description(product.description2),
                'Description 1 position': '',
                'Description 2':
                    checkers.check_description(product.description1),
                'Description 2 position': '',
                'Description 3':
                    checkers.check_description(product.description3),
                'Description 3 position': '',
                'Description 4':
                    checkers.check_description(product.description4),
                'Description 4 position': '',
                'Path 1': draft.path1,
                'Path 2': product.url,
                })

    if not not_writed_products:
        with open(
            'NOT_WRITED_COZE_HEADLINES.csv',
            'w',
            encoding='utf-8',
        ) as csv_bad_products:

            writer = csv.writer(csv_bad_products)
            for bad_product in not_writed_products:
                writer.writerow([bad_product])
