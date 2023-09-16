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

