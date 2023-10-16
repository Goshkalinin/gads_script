"""Записали объявки? Пора записать футер компании."""

import csv

from get_header import get_header


def write_footer1(draft, writer):
    """
    First footer row.

    Args:
        draft (obj): draft object
        writer (obj): scv writer object
    """
    footer = {
        'Campaign': draft.campaign,
        'ID': draft.id,
        'Location': draft.location,
        'Reach': draft.reach,
    }

    writer.writerow(footer)


def write_footer2(draft, writer):
    """
    Second footer row.

    Args:
        draft (obj): draft object
        writer (obj): scv writer object
    """
    footer = {
        'Campaign': draft.campaign,
        'Image Size': draft.image_size,
        'Link source': draft.link_source,
    }

    writer.writerow(footer)


def write_footer3(draft, writer):
    """
    Third footer row.

    Args:
        draft (obj): draft object
        writer (obj): scv writer object
    """
    footer = {
        'Campaign': draft.campaign,
        'Link source': draft.link_source,
        'Business name': draft.business_name,
    }

    writer.writerow(footer)


def write_campaign_footer(draft):
    """
    Записываем футер, на трёх строчках.

    Args:
        draft (obj): объект-шаблон.

    """
    with open('final.csv', 'a', encoding='utf-8') as csv_file:

        fieldnames = get_header('final.csv')

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        write_footer1(draft, writer)
        write_footer2(draft, writer)
        write_footer3(draft, writer)
