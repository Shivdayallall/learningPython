# primitive data types

#string
"Hello"

#int
23

#float
12.3

#boolean
True
False

# take an two digit number input from the user and add the digits together
num_input = input("enter a two digit number \n")
first_digit = num_input[0]
second_digit = num_input[1]
result = int(first_digit) + int(second_digit)
print(result)
# print(type(first_digit))