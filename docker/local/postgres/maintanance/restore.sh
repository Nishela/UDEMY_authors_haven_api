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

# Проверяем, был ли предоставлен аргумент с именем файла резервной копии
if [[ -z ${1+x} ]]; then
  message_error "Backup filename is not specified yet it is a required parameter. Make sure you provide one and try again."
  exit 1
fi

# Формируем полный путь к файлу резервной копии
backup_filename="${BACKUP_DIR_PATH}/${1}"

# Проверяем, существует ли указанный файл резервной копии
if [[ ! -f "${backup_filename}" ]]; then
  message_error "No backup with the specified backup filename was found. Check out the 'backups' maintenance script output to see if there in one and try again"
  exit 1
fi

# Выводим приветственное сообщение о начале восстановления
message_welcome "Restoring the '${POSTGRES_DB}' database from the '${backup_filename}' backup..."

# Проверяем, не используется ли пользователь postgres для восстановления, так как это небезопасно
if [[ "${POSTGRES_USER}" == "postgres" ]]; then
  message_error "Restoring as 'postgres' user is not allowed. Assign 'POSTGRES_USER' env with another one and try again."
  exit 1
fi

# Устанавливаем переменные окружения для утилит PostgreSQL
export PGHOST="${POSTGRES_HOST}"
export PGPORT="${POSTGRES_PORT}"
export PGUSER="${POSTGRES_USER}"
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGDATABASE="${POSTGRES_DB}"

# Сообщаем о том, что сейчас будет удалена текущая база данных
message_info "Dropping the database..."

# Удаляем текущую базу данных
dropdb "${PGDATABASE}"

# Сообщаем о том, что будет создана новая база данных
message_info "Creating a new database..."

# Создаем новую базу данных
createdb --owner="${POSTGRES_USER}"

# Сообщаем о том, что будет применена резервная копия к новой базе данных
message_info "Applying the backup to the new database..."

# Восстанавливаем базу данных из файла резервной копии
gunzip -c "${backup_filename}" | psql "${POSTGRES_DB}"

# Выводим сообщение об успешном восстановлении
message_success "The '${POSTGRES_DB}' database has been restored successfully from the '${backup_filename}' backup"
