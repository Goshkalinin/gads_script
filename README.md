# Автоматизируем табличку для Google Ads

## Ради чего мы это делаем
описать решаемые проблемы

## Как мы это делаем

## Структура проекта
**main.py** — get_draft → get_products → start_ads_csv → make_ads → write_campaign_footer
┃
┣━ **get_draft** — подбирает шаблонные значения из draft.csv
┣━ **get_products** — подбирает инфу о продуктах из csv-файла, дописывает нужные поля
┣━ **start_ads_csv** — создаёт финальную табличку с хедером компании
┣━ **make_ads** — записывает группы объявлений в финальную табличку
┗━ **write_campaign_footer** — записывает футер компании

## Линтер
Отпепячиваем код этим:
https://github.com/wemake-services/wemake-python-styleguide

Подробнее про опепячивалку:
https://habr.com/ru/companies/oleg-bunin/articles/433480/
