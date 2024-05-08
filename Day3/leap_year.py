print("Leap year calculator!")
year = int(input("Enter a year(000): "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}: You have a leap year")
else:
    print(f"{year}: it's not a leap year")
