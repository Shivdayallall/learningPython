import math

#Given the height and width of a wall, calculate how many cans of paint you will need to paint the wall.


def paint_calculator(height, width, price):
    number_of_cans = (height * width) / price
    print(math.ceil(number_of_cans))


paint_calculator(3, 4, 5)