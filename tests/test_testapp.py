import logging
import os
from sappgen.templates import Template1
from sappgen.util import cleanup

# ==================================================================================================

logging.getLogger().setLevel("DEBUG")

# ==================================================================================================


""" Template - 1
proj1
├── Makefile
├── app1
│   ├── cfg
│   │   ├── config.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
├── README.md
├── requirements-dev.txt
4 directories, 10 files
│   └── util
│       ├── __init__.py
│       └── log_util.py
└── tests
    └── test_app1.py

4 directories, 10 files
"""
def test_template1_struct():
    logging.debug("testing main")

    tmpl = Template1("proj1", "app1")
    tmpl.process()

    assert os.path.isfile("./proj1/Makefile") == True
    assert os.path.isfile("./proj1/README.md") == True
    assert os.path.isfile("./proj1/requirements-dev.txt") == True

    assert os.path.isfile("./proj1/app1/__init__.py") == True
    assert os.path.isfile("./proj1/app1/main.py") == True

    assert os.path.isfile("./proj1/app1/cfg/__init__.py") == True
    assert os.path.isfile("./proj1/app1/cfg/config.py") == True

    assert os.path.isfile("./proj1/app1/util/__init__.py") == True
    assert os.path.isfile("./proj1/app1/util/log_util.py") == True

    assert os.path.isfile("./proj1/tests/test_app1.py") == True

    cleanup(project_name="proj1")

    assert os.path.isdir("./proj1") == False
