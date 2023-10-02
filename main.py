import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

def caesar(input_text, shift_amount):
  output_string = ""
  for char in input_text:
    if char in alphabet:
      position = alphabet.index(char)
      if direction == "encode": 
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        output_string += new_letter
      else:
        new_position = position - shift_amount 
        new_letter = alphabet[new_position]
        output_string += new_letter
    else:
      output_string += char
  if direction == "encode":
    print(f"\nThe encrypted string is: {output_string}")
  else:
    print(f"\nThe decrypted string is: {output_string}")

while should_continue:
  if direction == "encode" or direction == "decode":
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))
    shift = shift % 26
    caesar(text, shift)
    result = input("\nDo you wish to continue? Y for yes, N for no.: ")
    if result == "Y":
      should_continue = True
      direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    else:
      print("\nGoodbye!")
      should_continue = False
  else:
    print("invalid input!")
