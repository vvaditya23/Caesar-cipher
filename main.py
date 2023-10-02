alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(plain_text, shift_amount):
  encrypted_string = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    encrypted_letter = alphabet[new_position]
    encrypted_string += encrypted_letter
  print(encrypted_string) 

def decrypt(encrypted_text, shift_amount):
  decrypted_string = ""
  for letter in encrypted_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    decrypted_letter = alphabet[new_position]
    decrypted_string += decrypted_letter
  print(decrypted_string)

if direction == "encode":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encrypt(text, shift)
elif direction == "decode":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  decrypt(text, shift)
else:
  print("Inavlid input!")
