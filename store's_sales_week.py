#Saiprasad Pujari
"""program that asks the user to enter a store's sales for each day of the week.
And the amounts should be stored in a tuple,
Using a loop to calculate the total sales for the week and displaying the result."""
def main ():
    store_daily_sales = []# an empty list to store the store's daily sales
    #asking the user to enter the sale amount for each day of the week
    for day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" ]:
        sales = float(input(f"enter the sale amount on {day}: $"))
        store_daily_sales.append(sales)
    sales_tuple = tuple(store_daily_sales)# converting the list to a tuple
    total_sales = sum(sales_tuple)# calculating the total sales amount
    #displaying the total sales for the week
    print(f"total sales amount for the week: ${total_sales:.2f}")


if __name__ == "__main__":


    main()