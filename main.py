"""Автоматизируем csv-табличку для Google Ads."""

import argparse
import logging

from py.get_draft import get_draft
from py.get_products import get_products
from py.make_ads import make_ads
from py.start_ads_csv import start_ads_csv
from py.write_campaign_footer import write_campaign_footer

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - Line %(lineno)d - \n %(message)s \n',
)


def main():
    """
    Хорошо бы дописать приём аргументов.

    Логика:
    собираем коллекцию продуктов из  CMS-выгрузки;
    подбираем значение полей шаблонной выгрузки из Google Ads;

    создаём макет будущей csv-хи;
    записываем тудой коллекцию продуктов;
    записываем тудой футер компании.
    """
    parser = argparse.ArgumentParser(
        description='Process product and draft data.',
        )
    parser.add_argument(
        '-p',
        '--products',
        help='Path to the products file (e.g., data.csv)',
        )
    parser.add_argument(
        '-d',
        '--draft',
        help='Path to the draft file (e.g., draft/draft.csv)',
        )

    args = parser.parse_args()

    products_file = args.products

    if args.draft:
        draft_file = args.draft
    else:
        draft_file = 'draft/draft.csv'

    if args.products:
        products_file = args.products
    else:
        products_file = 'data.csv'

    products = get_products(products_file)
    draft = get_draft(draft_file)

    start_ads_csv(draft)
    make_ads(products, draft)
    write_campaign_footer(draft)


if __name__ == '__main__':
    main()
