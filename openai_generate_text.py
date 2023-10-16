"""Модуль генеряченья контента, сэр."""

import logging
import openai
import requests
import time

from KEYS import OPENAI_KEY


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def check_internet_connection():
    """
    Чекаем соединение об гугл.

    Если пропало — спим, рекурсивно вызываем проверку ещё раз.
    Returns:
        200 if ok
    """
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        logger.info('ПРОПАЖА СВЯЗИ! \n посплю 30 секунд, и попробую ещё раз.')
        time.sleep(30)
        check_internet_connection()


def generate_text(prompt):
    """
    Всё просто: суём промт, получаем ответ.

    Args:
        prompt (str): суй, чо хош

    Returns:
        чо отдали, то и получай. И не ной.
    """
    check_internet_connection()

    openai.api_key = OPENAI_KEY

    best_temp = 0.25

    completion = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'user',
             'content': prompt,
             },
        ],
        temperature=best_temp,
    )

    return completion.choices[0].message.content
