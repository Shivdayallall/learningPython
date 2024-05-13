# print the highest number from the array
nums = [23, 5667, 234234, 4566, 56765, 7890]
highest_number = 0

for num in nums:
    if num > highest_number:
        highest_number = num
print(f"The highest number is: {highest_number} ")