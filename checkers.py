def repair_ellipsis(string):
    '''
    Меняет многоточие на скучный дефис
    '''
    string = string.replace('...', '-')
    return string


def check_headline_length(ad, not_writed_products):
    if len(ad.Headline_1) > 30:
        not_writed_products.append(ad)
        return True
    if len(ad.Headline_2) > 30:
        not_writed_products.append(ad)
        return True
    if len(ad.Headline_3) > 30:
        not_writed_products.append(ad)
        return True
    if len(ad.Headline_4) > 30:
        not_writed_products.append(ad)
        return True
    if len(ad.Headline_5) > 30:
        not_writed_products.append(ad)
        return True
    if len(ad.Headline_6) > 30:
        not_writed_products.append(ad)
        return True
    return False


def is_in_fourth_keywords(keywords, fourth_keywords):
    '''
    если в списке есть четвёртый ключ, выпиливаем объявку
    '''
    if keywords[3] not in fourth_keywords:
        fourth_keywords.append(keywords[3])
    else:
        print(keywords)
        keywords.remove(keywords[3])


def check_description(description):
    '''
    Чекает длину дескрипшна:
    если больше 90 символов режет по последнюю запятую, рекурсивно повторить
    правит многоточия при их наличии
    '''
    description = repair_ellipsis(description)
    if len(description) > 90:
        parts = description.split(',')
        description = ','.join(parts[:-1])
        description = check_description(description)
    return description
