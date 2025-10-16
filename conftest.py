import sys
import pytest


@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    old_sys, sys.argv = sys.argv, ["program.py"]
    def set_args(*args):
        sys.argv = ["program.py", *args]
    yield set_args
    sys.argv = old_sys
