# Imports
from argparse import *
import csv
from datetime import date
from functions import *
from rich_argparse import RichHelpFormatter

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

def main():
    parser = ArgumentParser(description="Hello you're using superpy!", 
                            epilog="use -h for more information",
                            add_help=f"This is a CLI tool to check, change and report about our inventory."
                                     f"See the readme for more information about its usage.",
                                     formatter_class=RichHelpFormatter)
    subparser = parser.add_subparsers(dest="command")
      
# Commando report:
    # $ python -m main.py report inventory
    report_parser = subparser.add_parser("report", help="Various kinds of reports")
    report_parser.add_argument("report_form", type=str, help="Specify the type of report you wish to see")
    
    buy_parser = subparser.add_parser("buy", help="Add item to the store")
    buy_parser.add_argument("buy_item", type=str, help="Specify the item, price, date and the bbd")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store")
    sell_parser.add_argument("sell_item", type=str, help="Specify the item, price date and bbd")
    
    time_parser = subparser.add_parser("time", help="Set the date used by the sytem")
    time_parser.add_argument("set_date", type=str, help="Set date in format: Y-M-D / 2020-10-05")

    args = parser.parse_args()


# Oproepen commando's
    if args.command == "report":
        if args.report_form == "inventory":
            outcome = report_inventory()
    

    

    return

if __name__ == "__main__":
    main()

