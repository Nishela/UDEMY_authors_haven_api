#!/usr/bin/env bash

# Устанавливаем флаги для bash, чтобы:
# - прекратить выполнение скрипта при первой ошибке (errexit)
# - прекратить выполнение скрипта, если используется неопределенная переменная (nounset)
# - возвращать код ошибки последней команды в конвейере, которая завершилась неудачно (pipefail)
set -o errexit
set -o nounset
set -o pipefail

# Определяем рабочую директорию скрипта
working_dir="$(dirname ${0})"

# Подключаем внешние файлы скрипта
source "${working_dir}/_sourced/constants.sh"
source "${working_dir}/_sourced/messages.sh"

# Выводим приветственное сообщение
message_welcome "Backing up the '${POSTGRES_DB}' database..."

# Проверяем, не используется ли пользователь postgres для резервного копирования, так как это небезопасно
if [[ "${POSTGRES_USER}" == "postgres" ]]; then
  message_error "Backing up as 'postgres' user is not allowed. Assign 'POSTGRES_USER' env with another one and try again."
  exit 1
fi

# Устанавливаем переменные окружения для утилиты pg_dump
export PGHOST="${POSTGRES_HOST}"
export PGPORT="${POSTGRES_PORT}"
export PGUSER="${POSTGRES_USER}"
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGDATABASE="${POSTGRES_DB}"

# Формируем имя файла для резервной копии
backup_filename="${BACKUP_FILE_PREFIX}_$(date +'%Y_%m_%dT%H_%M_%S').sql.gz"

# Создаем резервную копию базы данных с помощью утилиты pg_dump и архивируем ее с помощью gzip
pg_dump | gzip > "${BACKUP_DIR_PATH}/${backup_filename}"

# Выводим сообщение об успешном создании резервной копии
message_success "'${POSTGRES_DB}' database backup '${backup_filename}' has been created successfully and placed in '${BACKUP_DIR_PATH}'"
