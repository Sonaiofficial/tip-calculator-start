#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the Tip calculator\n---------------------------------------------")
bill = input("What was the total bill? Rs.")
new_bill = float(bill)
tip = input("What percentage tip would you like to give? 10, 12 or 20: ")
new_tip = float(tip) / 100
people_count = input("How many people to split the bill? ")
new_people_count = int(people_count)
pay = new_bill * new_tip
payment = pay / new_people_count
new_payment = round(payment, 2)
print(f"Each person should pay: Rs.{new_payment}  .. Thank you")

