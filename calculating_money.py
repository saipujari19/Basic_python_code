# #saiprasad pujari
# """calculates the amount of money a person could earn over a period of time.
# Write a try/except block that ensures the user inputs a valid integer when entering data"""
def main():
    while True:# using while loop
        try:
# asking user for the number of days
            days = int(input("enter the number of days: "))
# validating that the days are positive
            if days < 1:
                print("please enter a number greater than 0")
                continue
            break
        except ValueError:
            print("invalid input. please enter a valid integer.")
    total_pennies = 0
    current_pennies = 1  # starts with one penny
    print("Day\tSalary (pennies)\tTotal Salary ($)")
# looping through each day
    for day in range(1, days + 1):
        total_pennies += current_pennies
        print(f"{day}\t{current_pennies}\t\t\t${total_pennies / 100:.2f}")
        current_pennies *= 2  # doubling the salary each day
if __name__ == "__main__":
    main()
