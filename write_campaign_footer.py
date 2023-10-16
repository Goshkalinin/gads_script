"""Записали объявки? Пора записать футер компании."""

import csv

from get_header import get_header


def write_campaign_footer(draft):
    """
    Записываем футер, на трёх строчках.

    Args:
        draft (obj): объект-шаблон.

    """
    with open('final.csv', 'a', encoding='utf-8') as csv_file:

        fieldnames = get_header('final.csv')

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        footer1 = {
            'Campaign': draft.campaign,
            'ID': draft.id,
            'Location': draft.location,
            'Reach': draft.reach,
        }

        footer2 = {
            'Campaign': draft.campaign,
            'Image Size': draft.image_size,
            'Link source': draft.link_source,
        }

        footer3 = {
            'Campaign': draft.campaign,
            'Link source': draft.link_source,
            'Business name': draft.business_name,
        }

        writer.writerow(footer1)
        writer.writerow(footer2)
        writer.writerow(footer3)
