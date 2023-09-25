def repair_ellipsis(string):
    '''
    Меняет многоточие на скучный дефис
    '''
    string = string.replace('...', '-')
    return string


def check_headline(headline):
    '''
    Чекает длину хедлайна:
    не больше 30 символов
    '''
    if len(headline) > 30:
        print(headline)
    return headline


def check_description(description):
    '''
    Чекает длину дескрипшна:
    не больше 30 символов,
    правит многоточия при их наличии
    '''
    description = repair_ellipsis(description)
    if len(description) > 90:
        print(description)
    return description
