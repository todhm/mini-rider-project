#!/bin/bash

REPO_NAME="${1}"
if [[ -z "${REPO_NAME}" ]]
then 
  echo "Please enter your repo name ${REPO_NAME}" >&2
  exit 1
fi

skaffold run --default-repo="${REPO_NAME}"