[![HitCount](http://hits.dwyl.io/aayushuppal/sappgen.svg)](https://github.com/aayushuppal/sappgen)
[![GitHub contributors](https://img.shields.io/github/contributors/aayushuppal/sappgen.svg)](https://github.com/aayushuppal/sappgen/graphs/contributors)
[![Version](https://img.shields.io/pypi/v/sappgen.svg)](https://pypi.python.org/pypi/sappgen)
[![License](https://img.shields.io/pypi/l/sappgen.svg)](https://pypi.python.org/pypi/sappgen)
[![Build Status](https://travis-ci.org/aayushuppal/sappgen.svg?branch=master)](https://travis-ci.org/aayushuppal/sappgen)
[![Downloads](https://img.shields.io/pypi/dm/sappgen.svg)](https://pypi.python.org/pypi/sappgen)

# SAPPGEN

Simple App / WSGI Server App - Generator for Python - Command line utility

Well structured code skeleton for python code and applications with pytest

Template 1

> Standardizing general scripting, bots, applications etc. for maintainability and testing

Template 2

> WSGI REST backend server application with flask - gunicorn

Python `3.7`

## Installation

- Install from [PyPi](https://pypi.org/project/sappgen)

`pip install sappgen`

## Usage:

    $ sappgen [options] <project_name> <app_name>
    $ sappgen proj app
    $ sappgen -t1 proj app
    $ sappgen -t2 proj app

## Available options are:

    -h, --help         Show help
    -v, --version      Show package version
    -t1, --template1   Generate application - template 1
    -t2, --template2   Generate wsgi application - template 2

## Default App Template: Template 1 - App structure

    proj1
    ├── app1
    │   └── util
    │   │   ├── __init__.py
    │   │   └── log_util.py
    │   │── __init__.py
    │   └── app.py
    ├── config.ini
    ├── main.py
    │
    ├── tests
    |   └── test_app1.py
    │
    ├── Makefile
    ├── README.md
    └── requirements-dev.txt

## WSGI Server App Template: Template 2 - App structure

    project
    │
    ├── testapp
    │   ├── routes
    │   │   ├── __init__.py
    │   │   └── test_routes.py
    │   │
    │   └── util
    │   │   ├── __init__.py
    │   │   └── log_util.py
    │   │
    │   ├── __init__.py
    │   └── main.py
    │
    ├── config.ini
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    │
    └── tests
        └── test_main.py

## Contact

- https://aayushuppal.github.io

## Links

- https://pypi.org/project/sappgen
- https://github.com/aayushuppal/sappgen
