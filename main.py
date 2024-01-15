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

    buy_parser = subparser.add_parser("buy", help="Add item to the inventory, specify item, price, amount and bbd")
    buy_parser.add_argument("item", type=str, help="Name of the article e.g. Yoghurts")
    buy_parser.add_argument("price", type=float, help="Purchase price of article in € e.g. €2.65")
    buy_parser.add_argument("qty", type=str, help="Amount of the article e.g. 5 apples")
    buy_parser.add_argument("bbd", type=int, help="Shelf life in days, e.g. 10 days")

    sell_parser = subparser.add_parser("sell", help="Sell item from the store")
    sell_parser.add_argument("id", type=int, help="id of the article")
    sell_parser.add_argument("price", type=float, help="Retail price of the article in €")
    sell_parser.add_argument("qty", type=int, help="Quantity of the article sold")

    revenue_parser = subparser.add_parser("revenue", help="Report revenue given period")
    profit_parser = subparser.add_parser("profit", help="Report profit given period")
    old_stock = subparser.add_parser("old stock", help="Check for items that are past due")

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
    

    ## Command Sell

    if args.command == "sell":
    
        sales_append = {}
            # Lezen van de CSV
        with open('inventory.csv', mode='r+', newline='') as file:
            reader = csv.DictReader(file, delimiter=",")
            rows = list(reader)

            # Aanpassen id,product_name,quantity,buy_price,sales_price,expiration_date
            for row in rows:
                print(type(row["id"]))
                print(type(row["quantity"]))
                print(type(row["buy_price"]))

                print(row["id"])
                print(args.id)

                if row["id"] == args.id:
                    if int(row["quantity"]) > args.qty:
                        print("Test 1")
                        row["quantity"] = int(row['quantity']) - args.qty
                        print(f"You've sold {args.qty} {row["product_name"]}")
                        sales_append = {"id": row["id"],
                                            "product_name": row["product_name"],
                                            "quantity": args.qty,
                                            "buy_price": row["buy_price"],
                                            "sales_price": args.price,
                                            "sale_date": today_formatted,
                                            "expiration_date": row["expiration_date"]}
                    break

                elif int(args.qty) >= int(row['quantity']):
                    print("Test 2")
                    print(f"You've sold the last amount of {row['product_name']}: {row['quantity']}")
                    sales_append = {"id": row["id"],
                                        "product_name": row["product_name"],
                                        "quantity": row['quantity'],
                                        "buy_price": row["buy_price"],
                                        "sales_price": args.price,
                                        "sale_date": today_formatted,
                                        "expiration_date": row["expiration_date"]}
                    rows.remove(row)
                    break

                else:
                    print("Test 3")
                    print(f"The item you want to sell is not in stock!")
                    break  

            file.seek(0)
            file.truncate()

            writer = csv.DictWriter(file, fieldnames= reader.fieldnames, delimiter=",")
            writer.writeheader()
            writer.writerows(rows)

            if sales_append != {}:
                with open("sales.csv", mode="a", newline="") as output:
                    writer = csv.DictWriter(output, fieldnames = ["id","product_name",
                                                                "quantity","buy_price",
                                                                "sales_price","sale_date",
                                                                "expiration_date"], delimiter=",")
                    writer.writerow(sales_append)

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

