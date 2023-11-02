#!/bin/bash

# Включить режим автоматического завершения скрипта при первой ошибке
set -o errexit

# Если одна из частей конвейера завершится с ошибкой, весь конвейер завершится с ошибкой
set -o pipefail

# Автоматически выходить из скрипта, если используется неустановленная переменная
set -o nounset

# Если POSTGRES_USER не установлен, устанавливаем значение по умолчанию
if [ -z "${POSTGRES_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="${base_postgres_image_default_user}"
fi

# Python-скрипт для проверки доступности PostgreSQL
python << END
import sys
import time
import psycopg2

# Через 30 секунд после начала проверки предполагаем, что база данных не восстанавливается
suggest_unrecoverable_after = 30
start = time.time()

# Цикл проверки доступности PostgreSQL
while True:
  try:
    # Попытка подключиться к базе данных
    conn = psycopg2.connect(dbname='${POSTGRES_DB}', user='${POSTGRES_USER}', password='${POSTGRES_PASSWORD}', host='${POSTGRES_HOST}', port='${POSTGRES_PORT}')
    conn.close()
    break
  except psycopg2.OperationalError as error:
    # Выводим сообщение, что ждем доступности базы данных
    sys.stderr.write("Waiting for PostreSQL to become available...\n")
    # Если ожидание слишком долгое, выводим ошибку
    if time.time() - start > suggest_unrecoverable_after:
        sys.stderr.write(f"This is taking too long. Your database is unrecoverable. {error} \n")
  # Ожидаем одну секунду перед следующей попыткой подключения
  time.sleep(1)
END


>&2 echo "PostgreSQL available"

exec "$@"
