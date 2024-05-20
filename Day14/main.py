from art import logo
from art import vs
from game_data import data
import random
print(logo)


def display_names():
    #Get a random name from the data array and display it
    first_person = random.choice(data)
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")

    print(vs)

    second_person = random.choice(data)
    print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")



display_names()