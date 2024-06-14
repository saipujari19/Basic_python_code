#Saiprasad Pujari
"""program that prompts the user for a distance in meters and then displays that distance converted to miles, feet and inches
the value to be converted to feet in this problem is the decimal portion of the number of miles,
and the value to be converted to inches is the decimal portion of the number of feet."""
def main ():
    distance_meters = float(input("enter the distance in meters: "))#user to enter the distance in meter
    miles = distance_meters * 0.000621371 #convert meter to miles
    miles_int = int(miles) #extracting the integer part for miles
    feet = (miles - miles_int) * 5280 #convert miles to feet
    feet_int = int(feet) ##extracting the integer part for feet
    inches = (feet - feet_int) * 12 # convert feet to inches
    inches_round = round(inches) # rounding inches to nearest integer
    print("distance converted into miles, feet and inches: ") #displaying result
    print(miles_int, "miles,", feet_int, "feet,", inches_round, "inches")

if __name__ == "__main__":
    main()