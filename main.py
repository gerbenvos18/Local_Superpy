# Imports

from argparse import *
import csv
import random
from datetime import date
from functions import *

from rich_argparse import RichHelpFormatter
from rich.pretty import pprint
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.progress import track
import matplotlib.pyplot as plt

install()

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Main code:

def main():
    
    # $ python -m main -h
    parser = ArgumentParser(description=f"Hello you're using superpy.  Working date: [reverse]{superpy_date}[/]", 
                            epilog="use -h for more information",
                            add_help=f"This is a CLI tool to check, change and report about our inventory."
                                     f"See the readme for more information about its usage.",
                                     formatter_class=RichHelpFormatter)
    subparser = parser.add_subparsers(dest="command")
      
# Commando report:
    # $ python -m main report
    # $ python -m main report -h
    # $ python -m main buy Grape 1.50 14 8
    # $ python -m main sell 18 10 12
    # $ python -m main revenue -h
    # $ python -m main revenue 14-01-2024 18-01-2024
    # $ python -m main time set_date -10
    # $ python -m main set_date 20
    # $ python -m main current_date
    # $ python -m main profit 14-01-2024 18-01-2024
    # $ python -m main plot 14-01-2024 18-01-2024

    # Idee weggooien van alle artikelen die over de datum zijn 

    report_parser = subparser.add_parser("report", help="Report about current inventory", formatter_class=RichHelpFormatter)

    buy_parser = subparser.add_parser("buy", help="Add item to the inventory, specify item, price, amount and bbd", formatter_class=RichHelpFormatter)
    buy_parser.add_argument("item", type=str, help="Name of the article e.g. Yoghurts")
    buy_parser.add_argument("price", type=float, help="Purchase price of article in € e.g. €2.65")
    buy_parser.add_argument("qty", type=str, help="Amount of the article e.g. 5 apples")
    buy_parser.add_argument("bbd", type=int, help="Shelf life in days, e.g. 10 days")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store", formatter_class=RichHelpFormatter)
    sell_parser.add_argument("id_sell", type=int, help="id of the article")
    sell_parser.add_argument("price_sell", type=float, help="Retail price of the article in €")
    sell_parser.add_argument("qty_sell", type=int, help="Quantity of the article sold")
  
    revenue_parser = subparser.add_parser("revenue", help="Report revenue given period format: DD-MM-YYYY", formatter_class=RichHelpFormatter)
    revenue_parser.add_argument("start_date_revenue", type=str, help="Start date for revenue")
    revenue_parser.add_argument("end_date_revenue", type=str, help="End date for revenue")

    profit_parser = subparser.add_parser("profit", help="Report profit given period", formatter_class=RichHelpFormatter)
    profit_parser.add_argument("start_date_profit", type=str, help="Start date for profit")
    profit_parser.add_argument("end_date_profit", type=str, help="End date for profit")

    plot = subparser.add_parser("plot", help="Plot the revenue and profit in a line plot", formatter_class=RichHelpFormatter)
    plot.add_argument("start_date_plot", type=str, help="Start date for plot")
    plot.add_argument("end_date_plot", type=str, help="End date for plot")

    set_date_parser = subparser.add_parser("set_date", help="Set the date used by Superpy", formatter_class=RichHelpFormatter)
    set_date_parser.add_argument("days", type=int, help="Set date forward or revert in days")

    current_date_parser = subparser.add_parser("current_date", help="Set date to current date", formatter_class=RichHelpFormatter)

    #time_parser.add_argument("live_date", type=str, help="Set date back to realtime date")


    args = parser.parse_args()

    ## Command report about current inventory

    if args.command == "report":
        report_inventory()
        pass

    ## Command buy a article based on name

    if args.command == "buy":
        buy_article(buy_item=args.item, buy_qty=args.qty, buy_price=args.price, buy_bbd=args.bbd)
        return

    ## Command sell a article based on id.

    if args.command == "sell":
        sell_article(id_sell=args.id_sell, qty_sell=args.qty_sell, price_sell=args.price_sell)
        return

    ## Command reprot about revenue in given period
        
    if args.command == "revenue":
        report_revenue(date1=args.start_date_revenue, date2=args.end_date_revenue)
        return
    
    ## Command report about profit in given period

    if args.command == "profit":
        report_profit(date1=args.start_date_profit, date2=args.end_date_profit)
        pass

    ## Command set to specific date

    if args.command == "set_date":
        change_date(args.days)
        return
        
     ## Command set to current date   

    if args.command == "current_date":
        set_current_date()
        return

    if args.command == "plot":
        plot_revenue_profit(date1=args.start_date_plot, date2=args.end_date_plot)
        return

if __name__ == "__main__":
    main()

