print("The love calculator is calculating...")
your_name = input("what is your name? ")
their_name = input("what is their name? ")
combined_name = (your_name + their_name).lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

first_digit = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"you go together like coke and mentos, your score is {score}")
elif (score >= 40) and (score <= 50):
    print(f"your score is {score}, you go together like egg and cheese")