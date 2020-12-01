# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
percentage = input("What percentage tip would you like to five? 10, 12, or 15? ")
party_size = input("How many people to split the bill? ")


grand_total = float(total) * (1 + int(percentage) / 100)

individual_amount = round((grand_total / int(party_size)), 2)

print(f"Each person should pay: ${individual_amount}")