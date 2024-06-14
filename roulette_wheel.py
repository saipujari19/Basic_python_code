#Saiprasad Pujari
"""program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black.
And should display an error message if the user enters a number that is outside the range of 0 to 36."""
# pocket_number = int(input("enter a pocket number (0 to 36): "))
def main ():
    pocket_number = int(input("enter a pocket number: "))# user should enter a pocket number
    if pocket_number < 0 or pocket_number > 36: # checking entered pocket number is in the range or not
        print("error message: pocket number must be between 0 to 36")# outside the range print error message
    elif pocket_number == 0: # it is green when it is equal to zero
        print("the pocket", pocket_number, "is green")
    elif pocket_number <= 10:#For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
        if pocket_number % 2 == 0: #(pocket_number = x) x%2 = 0 is even or it is odd it gives remainder
            print("the pocket", pocket_number, "is black")
        else:
            print("the pocket", pocket_number, "is red")
    elif pocket_number <= 18:#For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
        if pocket_number % 2 == 0:
            print("the pocket", pocket_number,"is red")
        else:
            print("the pocket", pocket_number,"is black")
    elif pocket_number <= 28:#For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
        if pocket_number % 2 == 0:
            print("the pocket",pocket_number,"is black")
        else:
            print("the pocket",pocket_number,"is red")
    else:#For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.
        if pocket_number % 2 == 0:
            print("the pocket",pocket_number,"is red")
        else:
            print("the pocket",pocket_number,"is black")

if __name__ == "__main__":
    main()



