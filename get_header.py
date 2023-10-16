"""
Шляпа для выхватывания хедера таблицы.

Отдельным модулем лежит в связи с тем,
что используется в нескольких местах.
"""

import csv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - Line %(lineno)d - %(message)s',
)

logger = logging.getLogger(__name__)


def get_header(filename):
    """
    Штоб не дублировать простыню на 101 значение, тупо её считаем.

    Args:
        filename (str): путь до файла.

    Returns:
        fieldnames (list): хедер csv-хи.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        fieldnames = next(reader, None)
    return fieldnames
