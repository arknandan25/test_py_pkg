import argparse
from src.get_show_info import show_information





def main() -> None:
    parser = argparse.ArgumentParser(description='Show Tracker')
    subparser = parser.add_subparsers(dest="sub_parser")

    # define get subparser
    get = subparser.add_parser('get', help="Get show info")

    # Define argument name
    get.add_argument('name',  type=str, help='Name of show/movie')

    # set the function to be called after parsing this argument
    get.set_defaults(func=show_information)

    # parse the arguments and call the function specified
    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
