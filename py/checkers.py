"""
Набор проверялок.

Надо бы переписать, потому что эти проверялки
часто выполняют лишние (не проверяющие) функции.

Что вводит в заблуждение.
"""


def repair_symbols(string):
    """
    Фиксим стилистику дескрипшна.

    Сейчас в бане: '...', '!', '"'

    Args:
        string (str): любая строка

    Returns:
        string (str)
    """
    return string.replace('...', '-').replace('!', '').replace('"', '')


def check_headline_length(ad, not_writed_products):
    """
    Проверяем длину хедлайна.

    Если слишком длинно, отправляем в список незаписанных.

    Args:
        ad (str): объект с хедлайнами
        not_writed_products (list): список для продуктов не под запись.

    Returns:
        bool: если False — всё ок.
    """
    max_headline_length = 30
    attributes_to_check = [
        ad.vendor,
        ad.name,
        ad.product_type,
        ' '.join(['buy', ad.vendor]),
    ]

    for attribute in attributes_to_check:
        if len(attribute) > max_headline_length:
            not_writed_products.append(ad)
            return True

    return False


def is_in_fourth_keywords(keywords, fourth_keywords):
    """
    Eсли в списке fourth_keywords есть четвёртый ключ, выпиливаем объявку.

    Args:
        keywords (list): массив с ключами
        fourth_keywords (list): массив с четвертыми ключами.

    """
    if keywords[3] not in fourth_keywords:
        fourth_keywords.append(keywords[3])
    else:
        keywords.remove(keywords[3])


def check_description(description):
    """
    Чекает длину дескрипшна.

    Если больше 90 символов — режет по последнюю запятую,
    рекурсивно повторить!
    Правит многоточия и прочее при их наличии.

    Args:
        description (str): сбсна, дескрипшн объявки.

    Returns:
        description (str): поправленный дескрипшн.
    """
    description = repair_symbols(description)
    description_max_length = 90
    if len(description) > description_max_length and ',' in description:
        parts = description.split(',')
        description = ','.join(parts[:-1])
        description = check_description(description)

    return description
