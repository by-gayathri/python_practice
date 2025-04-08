import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
print(chars)

keys = chars.copy()
random.shuffle(keys)
print(keys)

plain_text = input("Enter the sentence to encrypt: ")
cipher_text = ""

#ENCRYPT
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Encrypted Text: {cipher_text}")

encrypted_text = input("Enter the sentence to decrypt: ")

plain_text = ""
#DECRYPT
for letter in encrypted_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Decrypted Text: {plain_text}")
