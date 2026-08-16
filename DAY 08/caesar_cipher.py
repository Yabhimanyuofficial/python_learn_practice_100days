alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            original_text += alphabet[new_position]
        else:
            original_text += letter
    print(f"The decoded text is {original_text}")   

decrypt(cipher_text=text, shift_amount=shift)