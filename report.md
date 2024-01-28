## Superpy Assignment - Gerben 

This short report highlights 3 technical elements of the script.
It explains what problem they solve and what choices were made to implement them in this way.

### Small introduction 

From the middle of december 2023 until mid/end january 2024 I've made the Superpy assignment.
I took a lot of time making notes of the practical examples in the csv, 
argparse and time video's to use them directly in the assignment. 
I structered the program in seperate .py files for the main body and its functions. 

#### Element 1 - item ID's for the inventory and sales data:

There are two unique ID's. One in the inventory.csv and one in the sales.csv. 
The sales ID is given at the moment you sell something. To keep track of seperate sales.
This way you have a greater insight in your sales. This is done by doing some list comprehension to get a list of all the existing ID's, 
and then generating a random number with the random module. For reference see the following functions in the functions.py:

    id_generator(), buy_article() and sell_article()


#### Element 2 - Specifying profit and revenue given between 2 dates:

This way it is possible for the user to specify revenue and profit given between any 2 dates. 
Which has a wider use than only today, yesterday etc. It is done by using the datetime module to use date objects, 
and then using the csv module to get the specific sales from those dates. 
For reference see the following functions in the functions.py:

    report_profit() and report_revenue()

#### Element 3 - Plotting revenue and profit in pie charts:

To visualize the data in a nice way its possible plot the revenue and profit in a pie chart. It is done so by using the matplotlib module. 
The information is written to a seperate "plot.csv". For reference see the following functions in the functions.py:

    plot_revenue_profit()

![Picture](https://raw.githubusercontent.com/gerbenvos18/Superpy/main/Revenue_profit_plot.png?token=GHSAT0AAAAAACMPWMK6QMLBHGN6XBUKHNXGZNWXETA)


