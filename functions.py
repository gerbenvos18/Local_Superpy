# Functies gebruikt in main

import csv
import datetime

from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from main import ArgumentParser

#Variables and article class

today_datetime = datetime.datetime.today()
time_notation = "%d-%m-%Y"
today_formatted = today_datetime.strftime(time_notation)

## Various time functions:
a_id_sell = 18 #id_sell 
a_price_sell = 12.00 #price_sell
a_qty_sell = 10 #qty_sell

def sell_article():
    sales_append = {}
    # Lezen van de CSV
    with open('inventory.csv', mode='r+', newline='') as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)

    # Aanpassen id,product_name,quantity,buy_price,sales_price,expiration_date
        for row in rows:
            if row["id"] == str(a_id_sell):
                if int(row["quantity"]) > a_qty_sell:
                    row["quantity"] = int(row['quantity']) - a_qty_sell
                    print(f"You've sold {a_qty_sell} {row["product_name"]}")
                    sales_append = {"id": row["id"],
                                    "product_name": row["product_name"],
                                    "quantity": a_qty_sell,
                                    "buy_price": row["buy_price"],
                                    "sales_price": a_price_sell,
                                    "sale_date": today_formatted,
                                    "expiration_date": row["expiration_date"]}
                    break

                if a_qty_sell >= int(row['quantity']):
                    print(f"You've sold the last amount of {row['product_name']}: {row['quantity']}")
                    sales_append = {"id": row["id"],
                                "product_name": row["product_name"],
                                "quantity": row['quantity'],
                                "buy_price": row["buy_price"],
                                "sales_price": a_price_sell,
                                "sale_date": today_formatted,
                                "expiration_date": row["expiration_date"]}
                    rows.remove(row)
                    break

                else:
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

sell_article() 

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

