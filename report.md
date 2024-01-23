# Superpy Assignment - Gerben 

Highlight 3 technical elements of the script
Explain what problem they solve and why you chose to implement them in this way

### Small introduction 

From the middle of december 2023 until mid/end january I've made the Superpy assignment. Took a lot of time making notes of the practical examples in the csv, and time video's to use them in the assignment. I structered the program in seperate .py files for the main body, functions and testing these functions. 

#### Element 1 - item ID's for the inventory and sales data:

As hinted in the assignment I gave the items two unique ID's. One in the inventory.csv and one in the sales.csv. They are 2 seperate ID's and the sales ID is given at the moment you sell something. This way you can keep track of selling the stock off in various sales. This is done by doing some list comprehension to get a list of all the existing ID's and then generating a random number which is not in it. 

    def id_generator():
        existing_ids = set()
        with open('inventory.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_ids.add(int(row["id"]))
        random_id = random.choice([x for x in range(0,51) if x not in existing_ids])
        return random_id


#### Element 2 - Specifying profit and revenue given between 2 dates:

This way it is possible for the user to specify revenue and profit given between any 2 dates. Which has a wider use than only today, yesterday etc. It is done by iterating through the csv's and summing the profit/revenue's when they fall between the two dates:

    