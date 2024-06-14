#Saiprasad Pujari
"""calculating and displaying BMI (Body Mass Index) using the formula bmi = w  /  h 2"""
def calculate_bmi(weight, height):
    return weight / (height ** 2)
def main():
    # Prompt the user for weight in kilograms and height in meters
    weight = float(input("enter your weight in kilograms: "))
    height = float(input("enter your height in meters: "))
# calculating BMI
    bmi = calculate_bmi(weight, height)
 # displaying the result
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
if __name__ == "__main__":
    main()