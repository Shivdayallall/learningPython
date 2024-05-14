alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, OR  type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the text and shift as inputs.


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        get_position_of_each_letter = alphabet.index(letter)
        get_new_positionn_of_each_letter = get_position_of_each_letter + shift_amount
        new_letter_position = alphabet[get_new_positionn_of_each_letter]
        cipher_text += new_letter_position
    print(f"Encoded text is: {cipher_text}")


encrypt(text, shift)




#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.