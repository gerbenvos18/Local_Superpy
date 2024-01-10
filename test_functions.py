import pytest
import argparse
import functions
from functions import *
import datetime
import csv


# Terminal invoer voor pytest: 
"$ python -m pytest"

#Global test_variables:
#example_article2 = Article(name="Orange", price=2, qty=4, shelf_life=14)

def test_class():
    print(f"Name: {example_article.name}, Price: {example_article.price}, "
            f"Qty: {example_article.price}, Shelf_life: {example_article.shelf_life}, "
            f"Purchase date: {getattr(Article, "buy_date")}")
    return
#test_class()
