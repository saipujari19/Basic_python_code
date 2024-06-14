#Saiprasad Pujari
# program that calculates the total amount of a meal purchased at a restaurant
food_charge = float(input("Enter the charge for the food: $"))
tip_amount = 0.20 * food_charge
meal_tax_amount = 0.05 * food_charge
total_amount = food_charge + tip_amount + meal_tax_amount
print("charge for the food at restaurant: %.2f" % food_charge)
print("The tip amount: %.2f" % tip_amount)
print("The meal tax amount: %.2f" % meal_tax_amount)
print("The total amount: %.2f" % total_amount)
