#Saiprasad Pujari
"""program that determine whether the month times the day equals the year.If so,it should display the date is magic.
Otherwise,it should display the date is not magic."""
def main ():
    month = int(input("enter the month (1-12): "))  # input from the user
    day = int(input("enter the day: "))  # input from the user
    year = int(input("enter the two-digit year: "))  # input from the user
    if month * day == year:  # checking if the date is magic or not using if and else statement
        print("the date is magic")
    else:
        print("the date is not magic")

if __name__ == "__main__":
    main()

