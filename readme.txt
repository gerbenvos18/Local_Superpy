Welcome to the readme file of this Superpy project!
This readme file gives a basic user guide for the program.
It also shows how the program is structered and how to use it properly.
This program represents the inventory management system of a supermarket.
The program is built as a CLI tool which uses csv and text files to store and retrieve data from.
To start the program make sure you're having the Superpy files in the cwd.
The program is accessed by running the main.py. 

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
The latter part of this readme will show the features of the tool with examples:


All Positional Arguments:
  {report, buy, sell, revenue, profit, set_date, current_date}

    

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
 
2. buy                 Add item to the inventory, specify item, price, amount and bbd (days).

$ python -m main buy [string] [float] [interger] [integer]
$ python -m main buy Grape 1.50 14 8

╭───────────────────────────────────╮
│ You bought a: Grape               │
│ Total Price: € 1.5                │
│ Qty: 14                           │
│ Shelf_life: 8 days                │
│ Purchase date: 22-01-2024         │
│ Best by date: 29-01-2024          │
╰───────────────────────────────────╯

3. sell                Sell item from the store, specify item_id, amount, price 
$ python -m main sell [integer] [integer] [float]
$ python -m main sell 18 10 12

You've sold the last amount of Pancakes: 12

Or if youve tried to sell items that are past best by date:

The Pancakes you've tried to sell are past bbd!

4. revenue             Report revenue between two time periods, in given format: DD-MM-YYYY
$ python -m main revenue [DD-MM-YYYY] [DD-MM-YYYY]
$ python -m main revenue 14-01-2024 18-01-2024

ID: 110 (Grapes) € 4.0
ID: 183 (Hamburgers) € 12.0
ID: 162 (Pork_ribs) € 12.0
ID: 176 (Apples) € 20.0
ID: 125 (Pears) € 20.0
ID: 199 (Grapes) € 20.0

╭──────────────────────────────────────────────╮
│ Time Period: 14-01-2024 - 18-01-2024         │
│ Total Revenue: €88.0                         │   
╰──────────────────────────────────────────────╯

5. profit              Report profit between two time periods, in given format: DD-MM-YYYY
$ python -m main profit [DD-MM-YYYY] [DD-MM-YYYY]
$ python -m main profit 16-01-2024 17-01-2024

Id: 148 (Pears):  € 11.25
Id: 176 (Apples):  € 19.55
Id: 125 (Pears):  € 19.25
Id: 143 (Grapes):  € 8.5
Id: 145 (Apples):  € 9.5
Id: 134 (Grape):  € 8.5
╭──────────────────────────────────────────╮
│ Time Period: 16-01-2024 - 17-01-2024     │
│ Total Profit: €76.55                     │
╰──────────────────────────────────────────╯

6. set_date            Set the date used by Superpy, in days forward or backwards
$ python -m main set_date [integer]
$ python -m main set_date -5

Superpy's working date is set to: 10-02-2024

$ python -m main set_date 5

Superpy's working date is set to: 10-02-2024

7. current_date        Set date to current date

$ python -m main current_date

Superpy's working date is set to: 22-01-2024