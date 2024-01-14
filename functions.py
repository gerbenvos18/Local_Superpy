# Functies gebruikt in main

import csv
import datetime

from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel

#Variables and article class

today_datetime = datetime.datetime.today()
time_notation = "%d-%m-%Y"
today_formatted = today_datetime.strftime(time_notation)

## Various time functions:

def change_date(days):                      #Used to set the date
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

class Article():
    buy_date = today_formatted
    def __init__(self, name, price, qty, shelf_life):
        self.name = name                #Name of the article
        self.price = price              #Total price for products 
        self.qty = qty                  #Amount bought
        self.shelf_life = shelf_life    #Shelf life of article in days
        self.bbd_date = expire_date(shelf_life) #Bbd 

#example_article = Article(name="Orange", price=2, qty=4, shelf_life=14)

## Random Id generator to give every item its own Id.
        
def id_generator():
    import random
    existing_ids = set()
    with open('inventory.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_ids.add(int(row["id"]))
    random_id = random.choice([x for x in range(50) if x not in existing_ids])
    return random_id

## Functions to change the inventory and report about it

   
def report_profit():
    pass

def sell_article():
    pass

