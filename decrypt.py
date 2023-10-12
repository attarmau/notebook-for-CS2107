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
def caesar_cipher_encrypt(message, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""

    for ch in message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position + key) % 26
            new_char = letters[new_pos]
            encrypted_message += new_char
        else:
            encrypted_message += ch

    return encrypted_message

# Example usage:
message = input("Enter the message to encrypt: ").strip()
key = int(input("Enter the key: "))
encrypted_message = caesar_cipher_encrypt(message, key)
print("Encrypted message:", encrypted_message)
