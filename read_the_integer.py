# #saiprasad Pujari
# #program that reads the integers contained in the file and prints
# """The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list"""
def main():
    try:
        with open("nums.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]
# calculating the required statistics
        lowest_number = min(numbers)
        highest_number = max(numbers)
        total = sum(numbers)
        average = total / len(numbers)
# displaying the information
        print(f"The lowest number in the list is: {lowest_number}")
        print(f"The highest number in the list is: {highest_number}")
        print(f"The total of the numbers in the list is: {total}")
        print(f"The average of the numbers in the list is: {average:.2f}")
    except FileNotFoundError:
        print("Error: The file 'nums.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

