# Imports
from argparse import *
import csv
from datetime import date
from functions import *
from rich_argparse import RichHelpFormatter

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Global variables:

# Main code:

def main():
    # $ python -m main -h
    parser = ArgumentParser(description="Hello you're using superpy!", 
                            epilog="use -h for more information",
                            add_help=f"This is a CLI tool to check, change and report about our inventory."
                                     f"See the readme for more information about its usage.",
                                     formatter_class=RichHelpFormatter)
    subparser = parser.add_subparsers(dest="command")
      
# Commando report:
    # $ python -m main report inventory
    # $ python -m main report -h
    # $ python -m main buy orange 1.50 20

    report_parser = subparser.add_parser("report", help="Report about current inventory", formatter_class=RichHelpFormatter)
    #report_parser.add_argument("format", type=str, help="")

    buy_parser = subparser.add_parser("buy", help="Add item to the store, specify item, price, amount and bbd")
    buy_parser.add_argument("item", type=str, help="Name of the article")
    buy_parser.add_argument("price", type=float, help="Price of the article in €")
    buy_parser.add_argument("qty", type=str, help="Amount of the article")
    buy_parser.add_argument("bbd", type=int, help="Best by date in days")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store")
    sell_parser.add_argument("sell_item", type=str, help="Specify the item, price date and bbd")
    
    time_parser = subparser.add_parser("time", help="Set the date used by the sytem")
    time_parser.add_argument("set_date", type=str, help="Set date in format: Y-M-D / 2020-10-05")

    revenue_parser = subparser.add_parser("revenue", help="Report revenue given period")

    profit_parser = subparser.add_parser("profit", help="Report profit given period")

    args = parser.parse_args()


# Oproepen commando's
    if args.command == "report":
        report_inventory()
        return
#        if args.format == "inventory":
    

    if args.command == "buy":
        with open('inventory.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            article_id = sum(1 for row in reader)

        with open('inventory.csv', 'a', newline='') as file:
            fieldnames = ["id", "product_name", "quantity", "buy_date", "buy_price", "expiration_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writerow({
                "id": article_id,
                "product_name": args.item,
                "quantity": args.qty,
                "buy_date": today_formatted,
                "buy_price": args.price,
                "expiration_date": expire_date(args.bbd)
            })
            return 
    

if __name__ == "__main__":
    main()

