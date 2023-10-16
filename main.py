"""Автоматизируем csv-табличку для Google Ads."""

import logging

from get_draft import get_draft
from get_products import get_products
from make_ads import make_ads
from start_ads_csv import start_ads_csv
from write_campaign_footer import write_campaign_footer

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
    products = get_products('data.csv')
    draft = get_draft('draft.csv')

    start_ads_csv(draft)
    make_ads(products, draft)
    write_campaign_footer(draft)


if __name__ == '__main__':
    main()
