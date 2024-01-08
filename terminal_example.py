from argparse import *
import csv
from datetime import date
from functions import *
from rich_argparse import RichHelpFormatter

# $python -m terminal_example -h
# How to do a recursive sub-folder search and return files in a list? Stack Overflow

RichHelpFormatter.styles["argparse.text"] = "green"

parser = ArgumentParser(description="Hello you're using superpy!", 
                        epilog="use -h for more information",
                        add_help= f"This is a CLI tool to check, change and report about our inventory."
                                  f"See the readme for more information about its usage.",
                        formatter_class=RichHelpFormatter)
subparser = parser.add_subparsers(dest="command")
      
report_parser = subparser.add_parser("report", help="Various kinds of reports")
report_parser.add_argument("report form", type=str, help="Specify the type of report you wish to see")

args = parser.parse_args()


if args.command == "report":
        outcome = None
        pass