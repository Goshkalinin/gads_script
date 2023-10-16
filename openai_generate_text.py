"""Модуль генеряченья контента, сэр."""


import logging
import time

import openai
import requests

from keys import OPENAI_KEY

logger = logging.getLogger(__name__)


def check_internet_connection():
    """
    Чекаем соединение об гугл.

    Если пропало — спим, рекурсивно вызываем проверку ещё раз.

    Returns:
        200 if ok
    """
    try:
        response = requests.get('http://www.google.com', timeout=5)
        correct_status_code = 200
        return response.status_code == correct_status_code
    except requests.ConnectionError:
        logger.info('ПРОПАЖА СВЯЗИ! \n посплю 30 секунд, и попробую ещё раз.')
        seconds_to_sleep = 30
        time.sleep(seconds_to_sleep)
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
