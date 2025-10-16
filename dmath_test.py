import datetime
import sys

import pytest

from dmath import parse_args


@pytest.fixture(name="args")
def patch_args():
    """Set sys.argv to ["program.py"] and send to test function."""
    old_sys, sys.argv = sys.argv, ["program.py"]
    yield sys.argv
    sys.argv = old_sys


def test_no_args(args):
    with pytest.raises(SystemExit) as e:
        parse_args()


def test_single_integer_parsed(args):
    args.extend(["5"])
    result = parse_args()
    assert result.days_or_date == 5
    assert result.date == datetime.date.today()


def test_invalid_input(args):
    args.extend(["invalid"])
    with pytest.raises(SystemExit) as e:
        parse_args()


def test_date_only_no_second_arg(args):
    args.extend(["1999-12-31"])
    result = parse_args()
    assert result.date == datetime.date.today()
    assert result.days_or_date == datetime.date(1999, 12, 31)


def test_date_and_days(args):
    args.extend(["1999-12-31", "5"])
    result = parse_args()
    assert result.date == datetime.date(1999, 12, 31)
    assert result.days_or_date == 5


def test_two_dates(args):
    args.extend(["2000-01-01", "2000-01-10"])
    result = parse_args()
    assert result.date == datetime.date(2000, 1, 1)
    assert result.days_or_date == datetime.date(2000, 1, 10)


def test_default_date_with_days(args):
    args.extend(["30"])
    result = parse_args()
    assert result.date == datetime.date.today()
    assert result.days_or_date == 30