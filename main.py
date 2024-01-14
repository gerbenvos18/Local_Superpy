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

    # Idee weggooien van alle artikelen die over de datum zijn 

    report_parser = subparser.add_parser("report", help="Report about current inventory", formatter_class=RichHelpFormatter)

    buy_parser = subparser.add_parser("buy", help="Add item to the store, specify item, price, amount and bbd")
    buy_parser.add_argument("item", type=str, help="Name of the article")
    buy_parser.add_argument("price", type=float, help="Price of the article in €")
    buy_parser.add_argument("qty", type=str, help="Amount of the article")
    buy_parser.add_argument("bbd", type=int, help="Best by date in days")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store")
    sell_parser.add_argument("sell_item", type=str, help="Specify the item, price date and bbd")
    
    revenue_parser = subparser.add_parser("revenue", help="Report revenue given period")
    profit_parser = subparser.add_parser("profit", help="Report profit given period")

    time_parser = subparser.add_parser("time", help="Set the date used by the sytem")
    time_parser.add_argument("set_date", type=str, help="Set date in format: Y-M-D / 2020-10-05")

    args = parser.parse_args()


    ## Command Report 

    if args.command == "report":

        table_inventory = Table(title=Panel(f"[blue bold]Inventory - {today_formatted}",), show_header=True)
        table_inventory.add_column("Product", header_style="yellow", justify="center")
        table_inventory.add_column("Purchase_€", header_style="yellow")
        table_inventory.add_column("Qty", header_style="yellow")
        table_inventory.add_column("Expiration_date", header_style="yellow", justify="center")
        table_inventory.add_column("Id", header_style="yellow",justify="right")

        with open('inventory.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                table_inventory.add_row(row['product_name'], 
                            row['buy_price'],
                            row['quantity'], 
                            row['expiration_date'],
                            row['id'])

            console = Console()
            console.print(table_inventory)
        return


    ## Command Buy 

    if args.command == "buy":
        with open('inventory.csv', 'r') as file:
            reader = csv.reader(file, delimiter=",")
            article_id = id_generator()

        with open('inventory.csv', 'a', newline='') as file:
            fieldnames = ["id", "product_name", "quantity", "buy_date", "buy_price", "expiration_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",")
            writer.writerow({
                "id": article_id,
                "product_name": args.item,
                "quantity": args.qty,
                "buy_date": today_formatted,
                "buy_price": args.price,
                "expiration_date": expire_date(args.bbd)
            })

            print(Panel(f"You bought a: [cyan bold]{args.item}[/] \n"
            f"Total Price: € [yellow bold]{args.price}[/] \n"
            f"Qty: [cyan bold]{args.qty}[/] \n"
            f"Shelf_life: [green bold]{args.bbd}[/] days \n"
            f"Purchase date: [green bold]{today_formatted}[/] \n"
            f"Best by date: [red bold]{expire_date(args.bbd)}[/]"))
            return 
    
    ## Command Revenue
        
    if args.command == "revenue":
        table = Table(title=Panel("[blue bold]Revenue of today",), show_header=True)
        table.add_column("Mare Lore Ipsum", header_style="yellow")
        console = Console()
        console.print(table)
        return

if __name__ == "__main__":
    main()

