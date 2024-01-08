# Functies gebruikt in main

import csv, argparse
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel

# Voorbeeld functie om op juiste manier te testen:

def superpy_parser():
    pass

def addition(number_1 =4, number_2 =6):
    return number_1 + number_2

def report_inventory():

    table = Table(title=Panel("[blue bold]Current Inventory",), show_header=True)
    table.add_column("Id", header_style="yellow")
    table.add_column("Product", header_style="yellow")
    table.add_column("Qty", header_style="yellow")
    table.add_column("Buy_date", header_style="yellow")    
    table.add_column("Price", header_style="yellow")
    table.add_column("Expiration_date", header_style="yellow")


    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            table.add_row(row['id'], 
                          row['product_name'], 
                          row['quantity'], 
                          row['buy_date'], 
                          row['buy_price'],
                          row['expiration_date'])

        console = Console()
        console.print(table)

    return

def report_revenue():
    pass

def report_profit():
    pass

def sell_article():
    pass

def buy_article():
    pass

def set_time():
    pass

report_inventory()
"""
    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for line in reader:
            print(line['id'], line["product_name"])
        
        
        console = Console()
        console.print(table)"""