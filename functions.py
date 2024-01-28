# Functions used in main. 

import csv
import datetime
import random
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.traceback import install

#Variables and article class

today_datetime = datetime.datetime.today()
time_notation = "%d-%m-%Y"
today_formatted = today_datetime.strftime(time_notation)
install()   #Console log from rich module for easier debugging

class Article():
    buy_date = today_formatted
    def __init__(self, name, price, qty, shelf_life):
        self.name = name                            #Name of the article
        self.price = price                          #Total price for products 
        self.qty = qty                              #Amount bought
        self.shelf_life = shelf_life                #Shelf life of article in days
        self.bbd_date = expire_date(shelf_life)     #Bbd 

# Read current date from txt file:
        
def read_date():
    with open("time.txt", "r") as file:
        current_date = file.readline()
    return current_date

superpy_date = read_date()

## Random Id generator to give every item its own Id.
def id_generator():
    existing_ids = set()
    with open('inventory.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_ids.add(int(row["id"]))
    random_id = random.choice([x for x in range(0,101) if x not in existing_ids])
    return random_id

## Random Id generator used in the sales.csv 
def id_generator_sales():
    existing_ids_sales = set()
    with open('sales.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_ids_sales.add(int(row["sales_id"]))
    random_id_sales = random.choice([x for x in range(101,201) if x not in existing_ids_sales])
    return random_id_sales

## Calculting the shelf_life calculated by giving days 
def expire_date(days):                      
    with open('time.txt', 'r') as file:
        current_date = file.readline()

    to_datetime = datetime.datetime.strptime(current_date, time_notation)
    timedelta2 = datetime.timedelta(days=days)
    new_date = to_datetime + timedelta2

    return new_date.strftime(time_notation)


#Report Inventory - Report about current state of inventory
def report_inventory():
    table_inventory = Table(title=Panel(f"[blue bold]Inventory - {today_formatted}",), show_header=True)
    table_inventory.add_column("Product", header_style="yellow", justify="center")
    table_inventory.add_column("Purchase_€", header_style="yellow")
    table_inventory.add_column("Qty", header_style="yellow")
    table_inventory.add_column("Expiration_date", header_style="yellow", justify="center")
    table_inventory.add_column("Id", header_style="yellow",justify="right")

    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            table_inventory.add_row(row['product_name'], 
                            row['buy_price'],
                            row['quantity'], 
                            row['expiration_date'],
                            row['id'])

        console = Console()
        console.print(table_inventory)
    return

#Report revenue - Print the revenue between 2 given dates  
def report_revenue(date1, date2):
    revenue_sorted = 0.00 #Empty value to store revenue in
    console = Console()
    start_date = datetime.datetime.strptime(date1, time_notation)
    end_date = datetime.datetime.strptime(date2, time_notation)
    with open("sales.csv", "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)
        for row in rows:
            sale_date = datetime.datetime.strptime(row["sale_date"], time_notation)
            if start_date <= sale_date <= end_date:
                console.print((f"ID: {row["sales_id"]} ({row["product_name"]}) € {row["sales_price"]}"))
                revenue_sorted += float((row["sales_price"]))
        print(Panel(f"[bold]Time Period:[/] [yellow]{date1}[/] - [red]{date2}[/]\n"
                    f"[bold]Total Revenue:[/] [green bold]€{revenue_sorted}"))
    return revenue_sorted


#Report profit - print the profit between 2 given dates
def report_profit(date1, date2):
    profit_sorted = 0.00 #Empty value to store proft in
    console = Console()
    start_date = datetime.datetime.strptime(date1, time_notation)
    end_date = datetime.datetime.strptime(date2, time_notation)
    with open("sales.csv", "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)
        for row in rows:
            sale_date = datetime.datetime.strptime(row["sale_date"], time_notation)
            if start_date <= sale_date <= end_date:
                profit = float(row["sales_price"]) - float(row["buy_price"])
                console.print(f"ID: {row["sales_id"]} ({row["product_name"]}):  € {profit}")
                profit_sorted += profit
        print(Panel(f"[bold]Time Period:[/] [yellow]{date1}[/] - [red]{date2}[/]\n"
                    f"[bold]Total Profit:[/] [green bold]€{profit_sorted}"))
    return profit_sorted

##Plot revenue and profit in pie charts:
def plot_revenue_profit(date1, date2):
    fieldnames_sales = ["sales_id","product_name",
                       "quantity","buy_price","sales_price",
                        "sale_date","expiration_date"]
    x_names = []
    y_profit = []
    y_revenue = []
    start_date = datetime.datetime.strptime(date1, time_notation)
    end_date = datetime.datetime.strptime(date2, time_notation)
    filtered_rows = [] #Empty list to store records in
    with open("sales.csv", "r", newline="") as file: 
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)
        for row in rows:
            sale_date = datetime.datetime.strptime(row["sale_date"], time_notation)
            if start_date <= sale_date <= end_date:
                filtered_rows.append(row) #Add all corresponding records to temporary list

    with open("plot.csv", "w", newline="") as new_file:
        writer = csv.DictWriter(new_file, fieldnames = fieldnames_sales, delimiter=",")
        writer.writeheader()
        writer.writerows(filtered_rows)
        for row in filtered_rows:
            x_names.append(f"{row["product_name"]} - €{row["sales_price"]}")
            y_profit.append(float(row["sales_price"]) - float(row["buy_price"]))
            y_revenue.append(float(row["sales_price"])) #Add all items of temporary list to plot.csv

    fig, axs = plt.subplots(1, 2, figsize=(8, 4)) #Number of rows in subplot
    
    axs[0].pie(y_profit, labels=x_names, autopct='%1.1f%%', textprops={"fontsize" :8})
    axs[0].set_title("Profit Plot", fontweight="bold")

    axs[1].pie(y_revenue, labels=x_names, autopct='%1.1f%%', textprops={"fontsize" :8})
    axs[1].set_title("Revenue Plot", fontweight="bold")

    fig.suptitle(f'Revenue plot {date1} - {date2}', fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()      #Plot with two subplots showing revenue and profit 
    return

#Buy Article - Buying an article using the item, qty, price and shelf life
def buy_article(buy_item, buy_qty, buy_price, buy_bbd):
    with open('inventory.csv', 'r', newline="") as file:
        reader = csv.DictReader(file, delimiter=",")
        article_id = id_generator()

    with open('inventory.csv', 'a', newline='') as file:
        fieldnames = ["id", "product_name", "quantity", "buy_date", "buy_price", "expiration_date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",")
        writer.writerow({
            "id": article_id,
            "product_name": buy_item,
            "quantity": buy_qty,
            "buy_date": today_formatted,
            "buy_price": buy_price,
            "expiration_date": expire_date(buy_bbd)
        })

        print(Panel(f"You bought a: [cyan bold]{buy_item}[/] \n" #Confirmation stating all given input
        f"Total Price: € [yellow bold]{buy_price}[/] \n"
        f"Qty: [cyan bold]{buy_qty}[/] \n"
        f"Shelf_life: [green bold]{buy_bbd}[/] days \n"
        f"Purchase date: [green bold]{today_formatted}[/] \n"
        f"Best by date: [red bold]{expire_date(buy_bbd)}[/]"))   
    return 

# Sell article - Selling an article using its id, quantity and price

def sell_article(id_sell, qty_sell, price_sell):
    sales_append = {}
    # Reading the inventory CSV
    with open('inventory.csv', mode='r+', newline='') as file:
        reader = csv.DictReader(file, delimiter=",")
        rows = list(reader)

    # Generate new rows to add in sales CSV
        for row in rows:    
            if row["id"] == str(id_sell):

                if datetime.datetime.strptime(row["expiration_date"], time_notation) < datetime.datetime.strptime(superpy_date, time_notation):
                    print(f"The [red]{row["product_name"]}[/] you've tried to sell are past bbd!")
                    break

                if int(row["quantity"]) > qty_sell:
                    row["quantity"] = int(row['quantity']) - qty_sell
                    print(f"You've sold {qty_sell} {row["product_name"]}")
                    sales_append = {"sales_id": id_generator_sales(),
                                    "product_name": row["product_name"],
                                    "quantity": qty_sell,
                                    "buy_price": row["buy_price"],
                                    "sales_price": price_sell,
                                    "sale_date": today_formatted,
                                    "expiration_date": row["expiration_date"]}
                    break

                if qty_sell >= int(row['quantity']):
                    print(f"You've sold the last amount of {row['product_name']}: {row['quantity']}")
                    sales_append = {"sales_id": id_generator_sales(),
                                "product_name": row["product_name"],
                                "quantity": row['quantity'],
                                "buy_price": row["buy_price"],
                                "sales_price": price_sell,
                                "sale_date": today_formatted,
                                "expiration_date": row["expiration_date"]}
                    rows.remove(row)
                    break

        file.seek(0)    #Move pointer back to the top of the file 
        file.truncate() 

        writer = csv.DictWriter(file, fieldnames= reader.fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(rows)

    # Adding sales to new CSV list:
        if sales_append != {}:
            with open("sales.csv", mode="a", newline="") as output:
                writer = csv.DictWriter(output, fieldnames = ["sales_id","product_name",
                                                          "quantity","buy_price",
                                                          "sales_price","sale_date",
                                                          "expiration_date"], delimiter=",")
                writer.writerow(sales_append)
    
    return 

#Change date - Change the date of the system to the future or the past
def change_date(days):                      
    with open('time.txt', 'r') as file:
        current_date = file.readline()

    to_datetime = datetime.datetime.strptime(current_date, time_notation)
    timedelta2 = datetime.timedelta(days=days)
    new_date = to_datetime + timedelta2

    with open('time.txt', 'w') as file:
        file.write(new_date.strftime(time_notation))
        print(f"Superpy's working date is set to: {new_date.strftime(time_notation)}")
        return    

#Set current date - Set the date back to current date in realtime 
def set_current_date():                     
    with open('time.txt', 'w') as file:
        file.write(today_formatted)
        print(f"Superpy's working date is set to: {today_formatted}")
        return

