import pytest
import argparse
from functions import *

# Terminal invoer voor pytest: 
"$ python -m pytest"

def test_addition():
    assert addition(5, 5) == 10

    pass

def split_list():
    line_1 = "1;Orange;25;7-1-2024;0.8;28-1-2024"
    line_split = line_1.split(";")
    return print(line_split)

split_list()