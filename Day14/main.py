from art import logo
from art import vs
from game_data import data
import random
print(logo)

# Get a random name from the data array and display it
first_person = random.choice(data)
second_person = random.choice(data)
# print(first_person["follower_count"])
# print(second_person["follower_count"])

user_score = 0


def display_names():

    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")

    print(vs)

    print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")



display_names()
user_input = input("Who has more followers? Type A or B: ").lower()


def check_answer(user_answer, person1, person2):
    if user_answer == "a":
        person1 = first_person
    elif user_answer == "b":
        person2 = second_person
    else:
        print("invalid choice")

    if person1["follower_count"] > person2["follower_count"]:
        print(f"{person1['name']} have more follower")
    elif person1["follower_count"] < person2["follower_count"]:
        print(f"{person2['name']} have more follower")
    else:
        print("Both are the same")





check_answer(user_input, first_person, second_person)
