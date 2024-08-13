# below is the old way to read data from csv file w/o using the csv library

# with open("./weather_data.csv") as weather_data:
#     weather_data_list = weather_data.readlines()
#     print(weather_data_list)


# import csv
# print the data using the built-in csv library
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#
#     # iterate and print out the data in the csv file
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

