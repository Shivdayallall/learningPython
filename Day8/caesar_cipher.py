from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
#BUG- index out of range error is thrown when a word that starts with the letter z is being encoded, to fix the bug copy and paste the value in the alphabet again

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, OR  type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    #TODO-1: Create a function called 'encrypt' that takes the text and shift as inputs.

    def encrypt(plain_text, shift_amount):
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                get_position_of_each_letter = alphabet.index(letter)
                get_new_positionn_of_each_letter = get_position_of_each_letter + shift_amount
                new_letter_position = alphabet[get_new_positionn_of_each_letter]
                cipher_text += new_letter_position
            else:
                cipher_text += letter
        print(f"Encoded text is: {cipher_text}")


    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

    #encrypt(text, shift)

    #Decode
    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
    def decrypt(cipher_text, shift_amount):
        #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
        decoded_text = ""
        for letter in cipher_text:
            if letter in alphabet:
                get_position_of_each_letter = alphabet.index(letter)
                get_new_positionn_of_each_letter = get_position_of_each_letter - shift_amount
                new_letter_position = alphabet[get_new_positionn_of_each_letter]
                decoded_text += new_letter_position
            else:
                decoded_text += letter

        print(f"Decoded text: {decoded_text}")


    #decrypt(text, shift)

    #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    results = input("Do you want to continue? yes or no?:  \n")
    if results == "no":
        should_continue = False
        print("Goodbye")
