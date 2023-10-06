# Определение переменной для версии Python
ARG PYTHON_VERSION=3.11.2-bullseye

# Используем официальный образ Python с указанной версией
FROM python:${PYTHON_VERSION} AS python

# Стадия сборки зависимостей
FROM python AS python-build-stage
# Определяем переменную для окружения сборки (по умолчанию — local)
ARG BUILD_ENVIRONMENT=local

# Обновляем пакеты и устанавливаем необходимые для сборки библиотеки
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

# Копируем файл с зависимостями в контейнер
COPY ./requirements .

# Собираем зависимости в wheels (бинарные пакеты)
RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt

# Стадия подготовки к выполнению
FROM python AS python-run-stage
# Определяем переменную для окружения (по умолчанию — local)
ARG BUILD_ENVIRONMENT=local

# Определение рабочего каталога
ARG APP_HOME=/app

# Установка переменных окружения Python для улучшения производительности
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Переменная для определения окружения сборки
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

# Установка рабочей директории
WORKDIR ${APP_HOME}

# Обновляем пакеты и устанавливаем необходимые библиотеки для выполнения
# После установки некоторые пакеты удаляются для экономии места
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Копируем собранные wheels из стадии сборки
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Устанавливаем зависимости из wheels и очищаем папку wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# Копируем файл entrypoint из локального каталога в корень файловой системы контейнера
COPY ./docker/local/django/entrypoint.sh /entrypoint.sh

# Удаляем символы возврата каретки (\r), что может быть полезно,
# если файл был создан или редактировался в Windows, чтобы избежать проблем с запуском файла в Linux
RUN sed -i 's/\r$//g' /entrypoint.sh

# Даем файлу entrypoint права на выполнение
RUN chmod +x /entrypoint.sh

# Копируем файл start из локального каталога в корень файловой системы контейнера
COPY ./docker/local/django/start.sh /start.sh

# Удаляем символы возврата каретки (\r) из файла start (по той же причине, что и выше)
RUN sed -i 's/\r$//g' /start.sh

# Даем файлу start права на выполнение
RUN chmod +x /start.sh

# Копируем содержимое текущей локальной директории в рабочую директорию контейнера (APP_HOME)
COPY . ${APP_HOME}

# Устанавливаем файл entrypoint в качестве основного исполняемого файла контейнера
ENTRYPOINT [ "/entrypoint.sh" ]
