#Greet the user
print(
    "Welcome to python pizza! \nWhere large pizza are only $25, Our medium size pizza are only $20, and Small are $15")

#Ask what size pizza the user wants. L = 25, M = 20, S = 15
pizza_size = input("What size pizza would you like? (s,m,l): ")

#Ask do they want pepperoni. s = +2, l,m = +3
add_pepperoni = input("Would you like pepperoni? (y or n) \nSmall will be +$2 \nLarge and Medium is be +$3: ")

#Ask if they want extra cheese. +1
extra_cheese = input("Extra cheese? (y or n) $+1 ")

#calculate bill
bill = 0
if pizza_size == "l":
    bill += 25
elif pizza_size == "m":
    bill += 20
else:
    bill += 15

if add_pepperoni == "y":
    if pizza_size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

#Display total bill
print("Thank you for choosing python pizza")
print(f"your bill is: ${bill}")
