#!/usr/bin/env bash

cd "$(dirname "$0")"
if [ ! -d 'venv' ]; then
    echo 'Please run ./setup.sh'
    exit 1
fi

venv/bin/python surro/__main__.py
