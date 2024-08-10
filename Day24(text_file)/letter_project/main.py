PLACEHOLDER = "[name]"


with open("./letters/letter_names.txt") as name_files:
    names = name_files.readlines()
    #print(nammes)

with open("./letters/starting_letter.txt") as letter_files:
    letter_content = letter_files.read()
    for name in names:

        # remove the backslash/whitespace from the names
        formatted_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, formatted_name)

        with open(f"./letters/completed_letters_for_{formatted_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)