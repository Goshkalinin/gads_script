# Автоматизируем табличку для Google Ads

## Ради чего мы это делаем
описать решаемые проблемы

## Как мы это делаем
Открываем data.csv ()

## Структура проекта
.
├── data.csv
├── draft
│   └── draft.csv
├── main.py
├── PROBLEMS.md
├── py
│   ├── checkers.py
│   ├── get_draft.py
│   ├── get_header.py
│   ├── get_products.py
│   ├── keys.py
│   ├── make_ads.py
│   ├── openai_generate_text.py
│   ├── start_ads_csv.py
│   └── write_campaign_footer.py
├── README.md
├── requirements.txt
└── TODO.md


## Линтер
Отпепячиваем код этим:
https://github.com/wemake-services/wemake-python-styleguide

Подробнее про опепячивалку:
https://habr.com/ru/companies/oleg-bunin/articles/433480/

запуск:
`flake8 .`
