def caesar_cipher_decrypt(encrypted_message, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""

    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - key) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch

    return decrypted_message

# Example usage:
encrypted_message = input("Enter the encrypted message: ").strip()
key = int(input("Enter the key: "))
decrypted_message = caesar_cipher_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

# Given a string 'message' and a secret key 'key', write a Python function to encrypt the message using the Caesar cipher

message = "HELLO"
key = 3
encrypted_message = caesar_cipher_encrypt(message, key)
print(encrypted_message)  # Output: "KHOOR"
