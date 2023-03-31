def monoalphabetic_encrypt(plaintext, key):
    """
    Encrypts plaintext using a Monoalphabetic Cipher with a given key.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Find the index of the character in the alphabet and substitute it with the key character
            index = ord(char.upper()) - 65
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def monoalphabetic_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using a Monoalphabetic Cipher with a given key.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Find the index of the character in the key and substitute it with the corresponding alphabet character
            index = key.index(char.upper())
            plaintext += chr(index + 65)
        else:
            plaintext += char
    return plaintext
plaintext = "A SOFTWARE ENGINEER"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

ciphertext = monoalphabetic_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = monoalphabetic_decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted)
