# Functies gebruikt in main

import csv, argparse
from datetime import datetime
from rich.console import Console
from rich.table import Table

# Voorbeeld functie om op juiste manier te testen:

def superpy_parser():
    pass

def addition(number_1 =4, number_2 =6):
    return number_1 + number_2

def report_inventory():

    table = Table(title="Current Inventory", show_header=True, title_style="green bold italic")
    table.add_column("Id", header_style="yellow")
    table.add_column("Product", header_style="yellow")
    table.add_column("Qty", header_style="yellow")
    table.add_column("Buy_date", header_style="yellow")    
    table.add_column("Price", header_style="yellow")

    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for line in reader:
            print(line['id'])
        
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

