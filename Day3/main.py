# Conditional statement
print("Welcome to the rollercoaster ride of doom!!")
HEIGHT = int(input("How tall are you? "))
bill = 0

if HEIGHT >= 120:
    print("HAVE A BLAST!!!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("you pay 5$")
    elif age <= 18:
        bill = 7
        print("you pay 7$")
    else:
        bill = 12
        print("you pay 12$")
    take_photo = input("Would you like a photo? It will cost an extra $3 (y or n) ")
    if take_photo == "y":
        print("click!!")
    bill += 3
    print(f"Your bill is ${bill}")
else:
    print("SORRY SHORT STUFF. MAYBE NEXT TIME! AH HA HA HA!")

# Modulas operator
# check if the number user enter is odd or even
'''
number = int(input("What number would you like to check? "))
even = number % 2 == 0
if even:
    print("number is even")
else:
    print("number is odd")
'''
