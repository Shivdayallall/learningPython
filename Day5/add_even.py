# take input from the user and add only the even numbers


# get a number from the user
user_number = int(input("Enter a number below 200: \n"))

# get the range of every number up to and including the user number
even_nums = []
total = 0
for nums in range(1, user_number + 1):
    if nums % 2 == 0:
        even_nums.append(nums)
        total = sum(even_nums)
print(total)
print(even_nums)
