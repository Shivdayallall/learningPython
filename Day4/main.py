import random

#generate a random number from 1 to 20. Including 20. randomInt includes the number
randomNum = random.randint(1, 20)

#generate a random float from 00000-0.9999. not including 1. to get a whole number you have to multiple by that number.
random_float = random.random() * 5
print(random_float)

#flip a coin
randon_number = random.randint(0, 1)
if randon_number == 0:
    print("Heads")
else:
    print("Tails")