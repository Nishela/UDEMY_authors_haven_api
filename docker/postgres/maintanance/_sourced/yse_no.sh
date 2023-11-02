#!/usr/bin/env bash

yse_no() {
  declare desc="Promt for confirmation. \$\"\{1\}\": confirmation message"
  local arg1="${1}"
  local response=read -r -p "${arg1} (y/[n]) " response

  if [[ "${response}" =~ ^[yY]$ ]]
  then
    exit 0
  else
    exit 1
  fi
}