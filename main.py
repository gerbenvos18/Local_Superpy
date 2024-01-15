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

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Global variables:

# Main code:

def main():
    set_current_date()
    # $ python -m main -h
    parser = ArgumentParser(description=f"Hello you're using superpy.  Date: [reverse]{today_formatted}[/]", 
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

    # Idee weggooien van alle artikelen die over de datum zijn 

    report_parser = subparser.add_parser("report", help="Report about current inventory", formatter_class=RichHelpFormatter)

    buy_parser = subparser.add_parser("buy", help="Add item to the inventory, specify item, price, amount and bbd")
    buy_parser.add_argument("item", type=str, help="Name of the article e.g. Yoghurts")
    buy_parser.add_argument("price", type=float, help="Purchase price of article in € e.g. €2.65")
    buy_parser.add_argument("qty", type=str, help="Amount of the article e.g. 5 apples")
    buy_parser.add_argument("bbd", type=int, help="Shelf life in days, e.g. 10 days")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store")
    sell_parser.add_argument("id_sell", type=int, help="id of the article")
    sell_parser.add_argument("price_sell", type=float, help="Retail price of the article in €")
    sell_parser.add_argument("qty_sell", type=int, help="Quantity of the article sold")
  
    revenue_parser = subparser.add_parser("revenue", help="Report revenue given period")
    profit_parser = subparser.add_parser("profit", help="Report profit given period")
    old_stock = subparser.add_parser("old stock", help="Check for items that are past due")

    time_parser = subparser.add_parser("time", help="Set the date used by Superpy")
    time_parser.add_argument("set_date", type=str, help="Set a date in format: Y-M-D / 2020-10-05")
    time_parser.add_argument("live_date", type=str, help="Set the date to realtime")

    args = parser.parse_args()


    ## Command Report 

    if args.command == "report":
        report_inventory()
        pass

    ## Command Buy 

    if args.command == "buy":
        buy_article(buy_item=args.item, buy_qty=args.qty, buy_price=args.price, buy_bbd=args.bbd)
        return

    ## Command Sell

    if args.command == "sell":
        sell_article(id_sell=args.id_sell, qty_sell=args.qty_sell, price_sell=args.price_sell)
        return

    ## Command Revenue
        
    if args.command == "revenue":
        table = Table(title=Panel("[blue bold]Revenue of today",), show_header=True)
        table.add_column("Mare Lore Ipsum", header_style="yellow")
        console = Console()
        console.print(table)
        return
    
    ## Command Profit

    if args.command == "profit":
        pass

    ## Command Time

    if args.command == "time":
        pass

if __name__ == "__main__":
    main()

