import logging
from sappgen import process
from sappgen.templates import Template1

# ==================================================================================================

logging.getLogger().setLevel("DEBUG")

# ==================================================================================================


def test_main():
    logging.debug("testing main")
    # capture 'tree' output in a string and compare it for testing the structure
    assert 1 == 1
