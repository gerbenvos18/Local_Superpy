Welcome to the readme file of this Superpy project!
This readme file gives a basic user guide for the program.
It also shows how the program is structered and how to use it properly.
This program represents the inventory management of a supermarket.
The program is built as a CLI tool which uses csv and text files to store and retrieve data from.
To start the program make sure you're having the Superpy files in the cwd.
The program is accessed by running the main.py and asking for its help section:

$ python -m main -h 

This should give the welcoming message and then a overview of all the functions it has.
As shown in the help section the program has a multitude of functions:
        {report,buy,sell,revenue,profit,old stock,set_date,current_date}
Each function has a built in help section to guide the user along. 

The code itself is structured as follows:
 - A main file with the command parser: "main.py"
 - A functions file to store all logic: "functions.py". 
 - Two csv files to keep track of the inventory and sales: "inventory.csv" and "sales.csv"
 - The date the program perceives is stored in a text file: "time.txt"

The program makes use of the rich and rich argparse module to give it a more userfriendly experience.
The latter part of this readme will show the features of the tool with examples


Positional Arguments:
  {report,buy,sell,revenue,profit,old stock,set_date,current_date}
    
    
    sell                Sell item from the store
    revenue             Report revenue given period format: DD-MM-YYYY
    profit              Report profit given period
    old stock           Check for items that are past due
    set_date            Set the date used by Superpy
    current_date        Set date to current date

1. report              Report about current inventory

$ python -m main report

╭─────────────────────────────────────────────────────────╮
│                 Inventory - 21-01-2024                  │
╰─────────────────────────────────────────────────────────╯
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━┓
┃   Product    ┃ Purchase_€ ┃ Qty  ┃ Expiration_date ┃ Id ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━┩
│    Apples    │ 0.5        │ 25   │    05-1-2024    │ 12 │
└──────────────┴────────────┴──────┴─────────────────┴────┘
 
2. buy                 Add item to the inventory, specify item, price, amount and bbd

