#saiprasad pujari
"""Write a program that asks a person their age. Accept an int.
Use an exception to return a message if a non number is entered.
 Return another custom message if the age entered is less than 1 or greater than 120."""
def main():
    try:
        age = int(input("Please enter your age: "))# asking the input from the user
        if age < 1 or age > 120:#checking if the age is between the valid range or not
            print("Error: The age entered must be between 1 and 120.")
        else:
            print(f"Your age is: {age}")
    except ValueError:
        print("error: Please enter a valid integer for age.")
if __name__ == "__main__":
    main()
