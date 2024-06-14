#saiprsad pujari
"""A function named is_even that accepts an integer as an argument and returns True if that integer is even
and False otherwise. Use the function in a program that prompts the user to enter an integer.
The program should display Even if the value entered is evenly divisible by 2, and Odd otherwise."""
def is_even(number):
    if number % 2 == 0: # checking if the number is divisible by 2 or not and returning it
        return True
    else:
        return False
def main ():
    number = int(input("enter an integer: ")) # taking input from the user
    # displaying even or odd
    if is_even(number):
        print("even")
    else:
        print("odd")
if __name__ == "__main__":
    main()