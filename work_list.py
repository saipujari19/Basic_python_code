#Saiprasad Pujari
"""Program that contains list of 6 integers,using a list method to add one integer and
list method to sort the list and using while loop to print the entries"""
def main ():
    number_list = [1, 3, 5, 6, 99, 0]  # creating list of 6 integers
    number_list.append(19)  # using append command to add one more integer
    print(number_list)  # printing the appended list
    number_list.sort()  # using sorting command to sort the list
    print(number_list)  # printing the sorted list
    i = 0
    while i < len(number_list):  # using while loop to print the entries
        print(number_list[i])
        i = i + 1

if __name__ == "__main__":
    main()

