#!/usr/bin/env bash

set -eE

is_command() {
    command -v $1 &>/dev/null
}

if ! is_command python3 || ! is_command curl || ! is_command hg; then
    echo 'Please install python3, curl, and mercurial to continue.'
    echo 'Note: openal-dev is also a dependency'
    exit 1
fi

cd "$(dirname "$0")"
if [ ! -x 'venv/bin/pip' ]; then
    rm -rf venv/
    python3 -m venv venv/ --without-pip
    source venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python
    deactivate
fi

venv/bin/pip install -r requirements.txt

