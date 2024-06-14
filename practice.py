# # # # # # # # # # # # name = "spp"
# # # # # # # # # # # # city_born = "Bengaluru"
# # # # # # # # # # # # favourite_sport = "cricket"
# # # # # # # # # # # # undergraduate_major = "ece"
# # # # # # # # # # # # print("your name:", name)
# # # # # # # # # # # # print("the city you were born:", city_born)
# # # # # # # # # # # # print("your favourite sport:", favourite_sport)
# # # # # # # # # # # # print("your undergraduate major:", undergraduate_major)
# # # # # # # # # # # #
# # # # # # # # # # # # a = "hello king" #assigning a string to a variable
# # # # # # # # # # # # print(a)
# # # # # # # # # # # #
# # # # # # # # # # # # b = """hi i am python,
# # # # # # # # # # # # welcome to the world of coding,
# # # # # # # # # # # # we shall learn lot many things
# # # # # # # # # # # # """ # multi line string
# # # # # # # # # # # # print(b[1]) #character at a position using array concept
# # # # # # # # # # # #
# # # # # # # # # # # # x = 12
# # # # # # # # # # # # y = 19
# # # # # # # # # # # # if x==y:
# # # # # # # # # # # #     print("x is equal to y") #if statement
# # # # # # # # # # # # elif x>y:
# # # # # # # # # # # #     print("x is greater than y") #elif statement
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("x is less tha y") # else statement when both the conditions are false.
# # # # # # # # # # # #     print(15 % 4) #quotient part
# # # # # # # # # # # # print(5//2)
# # # # # # # # # # # # result = 2 + 3
# # # # # # # # # # # # print(type(result))
# # # # # # # # # # # #
# # # # # # # # # # # # result = str(3) + "spp"
# # # # # # # # # # # # top_speed = 120
# # # # # # # # # # # # acceleration = 10
# # # # # # # # # # # # print(top_speed > 100 and acceleration > 20) #Returns True if both statements are true
# # # # # # # # # # # # print(top_speed > 100 or acceleration > 20) #Returns True if one of the statements is true
# # # # # # # # # # # # age = 60
# # # # # # # # # # # # if age < 60:
# # # # # # # # # # # #     pass #if we do not want to  write anything we can use pass
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("senior")
# # # # # # # # # # # # #print("bye")
# # # # # # # # # # # # state = "NH"
# # # # # # # # # # # # price = 30.5
# # # # # # # # # # # # product_catogery = "E"
# # # # # # # # # # # # if state == "NH":
# # # # # # # # # # # #     if product_catogery == "E":
# # # # # # # # # # # #         print(price * 0.08)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print(price * 0.06)
# # # # # # # # # # # #  if state == "CT":
# # # # # # # # # # # #     if product_catogery == "E":
# # # # # # # # # # # #         print(price * 0.04)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print(price * 0.12)
# # # # # # # # # # # #  else:
# # # # # # # # # # # #      if product_catogery == "E":
# # # # # # # # # # # #          print(price * 0.15)
# # # # # # # # # # # #      else:
# # # # # # # # # # # #          print(price * 0.16)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #def state_of_water_at_sea_level(temperature): #function to tell the state of water at a given temperature
# # # # # # # # # # #     # if temperature <= 32: # temperature(float) temp in float
# # # # # # # # # # #     #     print("solid state (ice form)") # water freezes at or below 32°F
# # # # # # # # # # #     # elif temperature >= 212:
# # # # # # # # # # #     #     print("gaseous state (water vapour)") # water boils at or above 212°F
# # # # # # # # # # #     # else:
# # # # # # # # # # #     #     print("liquid state") # water is liquid between freezing and boiling points
# # # # # # # # # # #
# # # # # # # # # # #     temperature = float(input("enter a temperature value in degrees Fahrenheit: "))#enter input
# # # # # # # # # # #     # state of water at given temperature
# # # # # # # # # # #     print(f"At {temperature}°F, water is at sea level.")level
# # # # # # # # # # # if temperature <= 32:  # temperature(float) temp in float
# # # # # # # # # # #     print("solid state (ice form)")  # water freezes at or below 32°F
# # # # # # # # # # # elif temperature >= 212:
# # # # # # # # # # #     print("gaseous state (water vapour)")  # water boils at or above 212°F
# # # # # # # # # # # else:
# # # # # # # # # # #     print("liquid state")  # water is liquid between freezing and boiling points
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # pocket_number: int = int(input("enter a pocket number: "))
# # # # # # # # # # if pocket_number == 0:
# # # # # # # # # #     print("it is green")
# # # # # # # # # # elif pocket_number (1, 10):
# # # # # # # # # #     print("it is red")
# # # # # # # # # # elif pocket_number (11, 28):
# # # # # # # # # #     print("it is black")
# # # # # # # # # # else:
# # # # # # # # # #     print("error")
# # # # # # # # # #
# # # # # # # # # def main():
# # # # # # # # #     # Define a tuple to store the days of the week
# # # # # # # # #     days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# # # # # # # # #
# # # # # # # # #     # Initialize an empty tuple to store sales
# # # # # # # # #     sales = ()
# # # # # # # # #
# # # # # # # # #     # Ask the user to enter sales for each day of the week
# # # # # # # # #     for day in days_of_week:
# # # # # # # # #         sales_amount = float(input(f"Enter sales for {day}: "))
# # # # # # # # #         sales += (sales_amount,)
# # # # # # # # #
# # # # # # # # #     # Display the entered sales
# # # # # # # # #     print("\nSales for each day of the week:")
# # # # # # # # #     for i in range(len(days_of_week)):
# # # # # # # # #         print(f"{days_of_week[i]}: ${sales[i]:.2f}")
# # # # # # # # #
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     main()
# # # # # # # # def main():
# # # # # # # #     # Create a dictionary of movie names and leading actors
# # # # # # # #     movies = {
# # # # # # # #         "The Shawshank Redemption": {"actor": "Tim Robbins", "director": "Frank Darabont"},
# # # # # # # #         "The Godfather": {"actor": "Marlon Brando", "director": "Francis Ford Coppola"},
# # # # # # # #         "The Dark Knight": {"actor": "Christian Bale", "director": "Christopher Nolan"},
# # # # # # # #         "Pulp Fiction": {"actor": "John Travolta", "director": "Quentin Tarantino"},
# # # # # # # #         "Inception": {"actor": "Leonardo DiCaprio", "director": "Christopher Nolan"}
# # # # # # # #     }
# # # # # # # #
# # # # # # # #     # Print the dictionary
# # # # # # # #     print("Original Dictionary:")
# # # # # # # #     print_dict(movies)
# # # # # # # #
# # # # # # # #     # Loop through printing key/value pairs
# # # # # # # #     print("\nLoop through the dictionary:")
# # # # # # # #     for movie, details in movies.items():
# # # # # # # #         print(f"Movie: {movie}, Actor: {details['actor']}, Director: {details['director']}")
# # # # # # # #
# # # # # # # #     # Add a new entry
# # # # # # # #     movies["The Matrix"] = {"actor": "Keanu Reeves", "director": "Lana Wachowski"}
# # # # # # # #
# # # # # # # #     # Reprint the dictionary
# # # # # # # #     print("\nDictionary after adding a new entry:")
# # # # # # # #     print_dict(movies)
# # # # # # # #
# # # # # # # #     # Find a star by selecting the movie
# # # # # # # #     movie_name = "The Dark Knight"
# # # # # # # #     if movie_name in movies:
# # # # # # # #         print(f"\nThe star of '{movie_name}' is {movies[movie_name]['actor']}.")
# # # # # # # #
# # # # # # # # def print_dict(dictionary):
# # # # # # # #     for key, value in dictionary.items():
# # # # # # # #         print(f"Movie: {key}, Actor: {value['actor']}, Director: {value['director']}")
# # # # # # # #
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     main()
# # # # # # #
# # # # # # #
# # # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # movies = {
# # # # # # #     "The Matrix": ("Keanu Reeves", "The Wachowskis"),
# # # # # # #     "John Wick": ("Keanu Reeves", "Chad Stahelski"),
# # # # # # #     "Titanic": ("Leonardo DiCaprio", "James Cameron"),
# # # # # # #     "Inception": ("Leonardo DiCaprio", "Christopher Nolan"),
# # # # # # #     "Interstellar": ("Matthew McConaughey", "Christopher Nolan"),
# # # # # # # }
# # # # # # # # Print the dictionary
# # # # # # # print("Original Dictionary:")
# # # # # # # print(movies)
# # # # # # # # Loop through printing key/value pairs
# # # # # # # print("\nMovies and their lead actors and directors:")
# # # # # # # for movie, details in movies.items():
# # # # # # #     print(f"{movie}: Actor - {details[0]}, Director - {details[1]}")
# # # # # # # # Add a new entry
# # # # # # # movies["Gladiator"] = ("Russell Crowe", "Ridley Scott")
# # # # # # # # Reprint
# # # # # # # print("\nUpdated Dictionary:")
# # # # # # # print(movies)
# # # # # # # # Find a star by selecting the movie
# # # # # # # movie_search = input("\nEnter a movie name to find its star: ")
# # # # # # # if movie_search in movies:
# # # # # # #     print(f"The star of {movie_search} is {movies[movie_search][0]}.")
# # # # # # # else:
# # # # # # #     print("Movie not found.")
# # # # # # # numbers =[1,5,6.7,85,66]
# # # # # # # sorted_list = sorted(numbers)
# # # # # #
# # # # # # # print(numbers)
# # # # # # # print(sorted_list)
# # # # # # # numbers.sort()
# # # # # # import math
# # # # # # help(math.factorial())
# # # # # # def capitalize_vowels(string):
# # # # # #     vowels = 'aeiouAEIOU'
# # # # # #     modified_string = ''
# # # # # #     for char in string:
# # # # # #         if char in vowels:
# # # # # #             modified_string += char.upper()
# # # # # #         else:
# # # # # #             modified_string += char
# # # # # #     return modified_string
# # # # # #
# # # # # #
# # # # # # def main():
# # # # # #     user_input = input("Enter a string: ")
# # # # # #
# # # # # #     # Display length of the string
# # # # # #     print("Length of the string:", len(user_input))
# # # # # #
# # # # # #     # Capitalize vowels and display modified string
# # # # # #     modified_string = capitalize_vowels(user_input)
# # # # # #     print("Modified string with capitalized vowels:", modified_string)
# # # # # #
# # # # # #     # Convert string into list of words
# # # # # #     words_list = user_input.split()
# # # # # #
# # # # # #     # Display length of the list
# # # # # #     print("Length of the list of words:", len(words_list))
# # # # #
# # # # #
# # # # # # if __name__ == "__main__": #Enter a string: king
# # # # # # Length of the string: 4
# # # # # # Modified string with capitalized vowels: kIng
# # # # # # Length of the list of words: 1
# # # # # #     main()
# # # # #
# # # # # # Ask user to enter a string
# # # # # input_string = input("Enter a string: ")
# # # # # # Display the length of the string
# # # # # print("Length of the string:", len(input_string))
# # # # # # Capitalize all vowels and display the modified string
# # # # # vowels = 'aeiou'
# # # # # modified_string = ''.join([char.upper() if char.lower() in vowels else char for char in input_string])
# # # # # print("Modified string with capitalized vowels:", modified_string)
# # # # # # Convert the string into a list of words
# # # # # words_list = input_string.split()
# # # # # # Display the length of the list
# # # # # print("Number of words in the string:", len(words_list))
# # # #
# # # # distance_meters = float(input("Enter distance in meters: "))
# # # # # Convert meters to miles, feet, and inches
# # # # miles = distance_meters * 0.000621371
# # # # feet = (miles - int(miles)) * 5280
# # # # inches = (feet - int(feet)) * 12
# # # # # Display the converted distance
# # # # print("Distance converted to miles, feet, and inches:")
# # # # print(int(miles), "miles,", int(feet), "feet,", round(inches, 2), "inches")
# # # def meters_to_miles_feet_inches(meters):
# # #     # Convert meters to miles
# # #     miles = meters / 1609.34
# # #
# # #     # Extract the integer part for miles
# # #     miles_int = int(miles)
# # #
# # #     # Convert remaining decimal part of miles to feet
# # #     feet_decimal = (miles - miles_int) * 5280
# # #
# # #     # Extract the integer part for feet
# # #     feet_int = int(feet_decimal)
# # #
# # #     # Convert remaining decimal part of feet to inches
# # #     inches_decimal = (feet_decimal - feet_int) * 12
# # #
# # #     # Round the inches to the nearest integer
# # #     inches = round(inches_decimal)
# # #
# # #     return miles_int, feet_int, inches
# # #
# # #
# # # def main():
# # #     # Prompt the user for distance in meters
# # #     distance_meters = float(input("Enter distance in meters: "))
# # #
# # #     # Convert meters to miles, feet, and inches
# # #     miles, feet, inches = meters_to_miles_feet_inches(distance_meters)
# # #
# # #     # Display the result
# # #     print(f"{distance_meters} meters is approximately {miles} miles, {feet} feet, and {inches} inches.")
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # range(5)
# # print(range)
# def is_even(int):
#     if int % 2 == 0:
#         return True
#     else:
#         return False
# def
def is_even(num):
    return num % 2 == 0

def main():
    num = int(input("Enter an integer: ")) # taking input from the user
    if is_even(num): # displaying even or odd
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()
#
#
#
#
#
#
#
#
