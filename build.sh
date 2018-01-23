#!/usr/bin/env bash

cd "$(dirname "$0")"
if [ ! -d 'venv' ]; then
    echo 'Please run ./setup.sh'
    exit 1
fi

if [ ! -f 'venv/bin/pyinstaller' ]; then
    venv/bin/pip install pyinstaller
fi

venv/bin/pyinstaller -y surro.spec
