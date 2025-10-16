import argparse
import datetime


def date(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d").date()


def date_or_int(string):
    try:
        return date(string)
    except ValueError:
        try:
            return int(string)
        except ValueError:
            raise argparse.ArgumentTypeError("Number or date required")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "date",
        nargs="?",
        type=date,
        default=datetime.date.today(),
    )
    parser.add_argument("days_or_date", type=date_or_int)
    return parser.parse_args()


def main():
    args = parse_args()
    if isinstance(args.days_or_date, int):
        print(args.date + datetime.timedelta(args.days_or_date))
    else:
        print((args.days_or_date - args.date).days)


if __name__ == "__main__":
    main()