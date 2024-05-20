from art import logo
from art import vs
from game_data import data
import random
print(logo)



user_score = 0



def check_answer(user_answer, person1, person2):
    if person1 > person2:
        return user_answer == "a"
    else:
        return user_answer == "b"



should_continue = True

while should_continue:
    # Get a random name from the data array and display it
    first_person = random.choice(data)
    second_person = random.choice(data)
    if first_person == second_person:
        second_person = random.choice(data)
    first_person_count = first_person["follower_count"]
    second_person_count = second_person["follower_count"]


    def display_names():

        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")

        print(vs)

        print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")


    display_names()
    user_input = input("Who has more followers? Type A or B: ").lower()

    is_correct = check_answer(user_input, first_person_count, second_person_count)

    if is_correct:
        user_score += 1
        print(f"Your correct!!. Current score {user_score}")
    else:
        should_continue = False
        print(f"Sorry, that's incorrect. Final score {user_score}")

