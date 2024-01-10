import pytest
import argparse
from functions import *
import datetime
import csv

# Terminal invoer voor pytest: 
"$ python -m pytest"

#Global test_variables:
example_article = Article(name="Orange", price=2, qty=4, shelf_life=14)

def test_class():
    print(f"Name: {example_article.name}, Price: {example_article.price}, "
            f"Qty: {example_article.price}, Shelf_life: {example_article.shelf_life}, "
            f"Purchase date: {getattr(Article, "buy_date")}")
    return
#test_class()

def add_to_inventory_test():
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
#add_to_inventory_test()
