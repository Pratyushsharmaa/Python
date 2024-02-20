alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#defined twice to avoid list out of bound error.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. It should then shift the letters in the text by the shift amount and print the encrypted text.
def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    encrypted_text += new_letter
  print(f"The encoded text is {encrypted_text}")

#TODO-2: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs. It should then shift the letters in the text by the shift amount and print the decrypted text.

def decrypt(text, shift):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
    
  
        