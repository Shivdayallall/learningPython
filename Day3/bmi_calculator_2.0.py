# formula for bmi calculator BMI = weight(kg)/height(m)^2. PEMDAS
# example BMI = 55kg/1.6256^2

# get user input for weight
weight = input("Please enter your weight? \n")

# convert weight from pounds to kg. 1 pound = 0.453592 kg.
convert_weight_to_kg = int(weight) * 0.453592

# get user input for height
height_ft = input("Please enter your height(ft)? \n")
height_in = input("Please enter your height(in)? \n")

# convert height from ft, inch to meters. 1 foot = 0.3048 meters. 1 inch = 0.0254 meters.
convert_height_ft_to_meter = int(height_ft) * 0.3048
convert_height_in_to_meter = int(height_in) * 0.0254
total_height_in_meters = convert_height_ft_to_meter + convert_height_in_to_meter

# perform calculation, get bmi
BMI = round(convert_weight_to_kg / (total_height_in_meters ** 2), 2)

if BMI >= 30:
    print(f"your BMI is : {BMI}, Please join a gym fattie")
elif BMI >= 25 and BMI < 29.9:
    print(f"your BMI is : {BMI}, Do some jumping jax slightly less fattie")
elif BMI >= 18.5 and BMI <= 24.9:
    print(f"your BMI is : {BMI}, you good bro, Treat your self with some ice-cream")
elif BMI < 18.5:
    print(f"your BMI is : {BMI}, Eat a steak twig")

