#Saiprasad Pujari
#Printing whether water is liquid, solid or gaseous at the given temperature at sea level.
def state_of_water_at_sea_level(temperature): #function to tell the state of water at a given temperature
    if temperature <= 32: # temperature(float) temp in float
        print("solid state (ice form)") # water freezes at or below 32°F
    elif temperature >= 212:
        print("gaseous state (water vapour)") # water boils at or above 212°F
    else:
        print("liquid state") # water is liquid between freezing and boiling points
def main():
    temperature_fahrenheit = float(input("enter a temperature value in degrees Fahrenheit: "))#enter input
    state = state_of_water_at_sea_level(temperature_fahrenheit)# state of water at given temperature
    print(f"At {temperature_fahrenheit}°F, water is {state} at sea level.")#printing result
    #to get degree symbol used alt + 0176
if __name__ == "__main__":
    main()


