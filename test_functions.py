import pytest
import datetime
import csv
from functions import *

# Terminal invoer voor pytest: 
"$ python -m pytest"

#Global test_variables:

def test_class():
    example_article2 = Article(name="Orange", price=2, qty=4, shelf_life=14)
    print(f"Name: {example_article2.name}, Price: {example_article2.price}, "
            f"Qty: {example_article2.price}, Shelf_life: {example_article2.shelf_life}, "
           f"Purchase date: {getattr(Article, "buy_date")}")
    return

#test_class()

#print(today_formatted)