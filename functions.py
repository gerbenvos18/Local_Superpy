# Functies gebruikt in main

import csv, argparse
import datetime
import test_functions
import main
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel

#Variables and article class

today_datetime = datetime.datetime.today()
time_notation = "%d-%m-%Y"
today_formatted = today_datetime.strftime(time_notation)

class Article():
    buy_date = today_formatted
    def __init__(self, name, price, qty, shelf_life):
        self.name = name                #Name of the article
        self.price = price              #Total price for products 
        self.qty = qty                  #Amount bought
        self.shelf_life = shelf_life    #Shelf life of article in days

example_article = Article(name="Orange", price=2, qty=4, shelf_life=14)

## Various time functions:

def change_date(days):                      #Used to forward or backward time
    with open('time.txt', 'r') as file:
        current_date = file.readline()

    to_datetime = datetime.datetime.strptime(current_date, time_notation)
    timedelta2 = datetime.timedelta(days=days)
    new_date = to_datetime + timedelta2

    with open('time.txt', 'w') as file:
        file.write(new_date.strftime(time_notation))
        return    
#change_date(2)
        
def expire_date(days):                      #Used to calculate the shelf_life
    with open('time.txt', 'r') as file:
        current_date = file.readline()

    to_datetime = datetime.datetime.strptime(current_date, time_notation)
    timedelta2 = datetime.timedelta(days=days)
    new_date = to_datetime + timedelta2

    return new_date.strftime(time_notation)
#print(expire_date(14))

def set_current_date():                     #Used to set date back to current date
    with open('time.txt', 'w') as file:
        file.write(today_formatted)
    return
#set_current_date()

## Functions to change the inventory and report about it

def report_inventory():

    table = Table(title=Panel("[blue bold]Current Inventory",), show_header=True)
    table.add_column("Product", header_style="yellow", justify="center")
    table.add_column("Purchase_€", header_style="yellow")
    table.add_column("Qty", header_style="yellow")
    table.add_column("Expiration_date", header_style="yellow", justify="center")
    table.add_column("Id", header_style="yellow",justify="right")

    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            table.add_row(row['product_name'], 
                          row['buy_price'],
                          row['quantity'], 
                          row['expiration_date'],
                          row['id'])

        console = Console()
        console.print(table)
    return

def report_revenue():
    table = Table(title=Panel("[blue bold]Revenue of today",), show_header=True)
    table.add_column("Mare Lore Ipsum", header_style="yellow")
    console = Console()
    console.print(table)
    pass

def buy_article():
    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        article_id = sum(1 for row in reader)

    with open('inventory.csv', 'a', newline='') as file:
        fieldnames = ["id", "product_name", "quantity", "buy_date", "buy_price", "expiration_date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writerow({
            "id": article_id,
            "product_name": example_article.name,
            "quantity": example_article.qty,
            "buy_date": example_article.buy_date,
            "buy_price": example_article.price,
            "expiration_date": expire_date(example_article.shelf_life)
        })
        return
    
def report_profit():
    pass

def sell_article():
    pass

