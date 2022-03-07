from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            if new_position < 0:
                new_position += 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d text: {end_text}")


print(logo)

continue_cipher = "yes"

while continue_cipher == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    continue_cipher = input("Do you want to continue? Type yes or no ")
    if continue_cipher == "no":
        print("Goodbye")