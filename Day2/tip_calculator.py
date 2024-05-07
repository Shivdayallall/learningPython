# Greet the user.
print("Welcome to the tip calculator!")

# Get the total bill from the user. turn the input to a float, bc bills are not whole numbers.
current_bill = float(input("Enter bill amount? "))

# get the percentage of tip the user would like to leave. convert input to a percent.
tip_amount = input("How much tip would you like to leave? ")
tip_percent = int(tip_amount) / 100

# calculate tip amount
tip_amount = current_bill * tip_percent

# total bill with tips
TOTAL_BILL = round(tip_amount + current_bill,2)

# get amount of people to split the bill.
amount_of_people = input("How many people are spliting the bill? ")

# calculate how much each person have to pay
amount_per_person = round(TOTAL_BILL / int(amount_of_people),2)

print(f"Each person will pay: {amount_per_person}")
print(f"Total bill: {TOTAL_BILL}")
