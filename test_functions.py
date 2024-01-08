import pytest
import argparse
from functions import *

# Terminal invoer voor pytest: 
"$ python -m pytest"

def test_addition():
    assert addition(5, 5) == 10
