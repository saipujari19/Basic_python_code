print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12 or 15 \n"))
people = int(input("how many people to split the bill? "))
tip_as_percent = tip/100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill/people
total_amount = round(bill_per_person, 2)
print(f"each person should pay: ${total_amount}")