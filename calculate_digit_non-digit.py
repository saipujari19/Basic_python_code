#Saiprasad Pujari
"""program that contains a function that accepts a string and
calculates the number of digits and non-digits in that string
Same String as input. Write and return the digits found in the string to a list and print list
Same String. Write and return the non-digits found in the string to a tuple and print tuple"""
def count_digits_and_non_digits(input_string): # string input to count the digits
    digits = 0
    non_digits = 0
    digits_list = []
    non_digits_list = []
    for char in input_string: #iterating through each character
        if char.isdigit():
            digits += 1
            digits_list.append(char)
        else:
            non_digits += 1
            non_digits_list.append(char)
    return digits, non_digits, digits_list, tuple(non_digits_list)
def main():
    input_string = input("enter a string: ") # entering the input
    digits, non_digits, digits_list, non_digits_tuple = count_digits_and_non_digits(input_string)
    print(f"The number of digits is: {digits}")# printing the number of digits
    print(f"The number of non-digits is: {non_digits}")# the number of non digits
    print(f"The list of digits are: {digits_list}") # printing the list of digits
    print(f"The tuple of non-digits are: {non_digits_tuple}") # printing the tuple of non digits
if __name__ == "__main__":
    main()