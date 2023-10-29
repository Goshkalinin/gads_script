"""Модуль генеряченья контента, сэр."""


import logging
import time

import openai
import requests

from .keys import OPENAI_KEY

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
    except requests.ConnectionError:
        logger.info('ПРОПАЖА СВЯЗИ! \n посплю 30 секунд, и попробую ещё раз.')
        seconds_to_sleep = 30
        time.sleep(seconds_to_sleep)
        check_internet_connection()

    correct_status_code = 200
    return response.status_code == correct_status_code


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

    response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      prompt="Write a tagline for an ice cream shop.",
      temperature=0.25
    )

    print(response.choices[0].text)

    return response.choices[0].text
