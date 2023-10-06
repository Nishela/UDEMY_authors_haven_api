#!/bin/bash

# Включить режим автоматического завершения скрипта при первой ошибке
set -o errexit

# Если одна из частей конвейера завершится с ошибкой, весь конвейер завершится с ошибкой
set -o pipefail

# Автоматически выходить из скрипта, если используется неустановленная переменная
set -o nounset

python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec python manage.py runserver 0.0.0.0:8000