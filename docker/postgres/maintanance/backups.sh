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
message_welcome "These are the backups you have got:"

# Выводим список файлов резервных копий в заданной директории, отсортированных по дате изменения
ls -lht "${BACKUP_DIR_PATH}"
