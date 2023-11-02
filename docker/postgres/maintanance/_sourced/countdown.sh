#!/usr/bin/env bash

countdown() {

  declare desc="A simple countdown."

  # Локальная переменная seconds принимает значение аргумента, переданного функции
  local seconds="${1}"

  # Вычисляем время окончания отсчета, добавляя seconds к текущему времени
  local d=$(($(date +%s) + "${seconds}"))

  # Пока текущее время меньше времени окончания отсчета, продолжаем цикл
  while [ "$d" -ge `date +%s` ]; do

    # Выводим оставшееся время обратного отсчета в формате ЧЧ:ММ:СС, используя \r для возврата каретки, чтобы обновить текущую строку
    echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r";

    sleep 0.1
  done

}