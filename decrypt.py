cdef decrypt():
    
    #enter your encrypted message(string) below
    encrypted_message = input("Gurer_V5_n_YbG_Bs_Uby3f_Va_Gu1f_Ba3 ").strip()
    
    letters="abcdefghijklmnopqrstuvwxyz"
    
    #enter the key value to decrypt
    k = int(input("Gurer_V5_n_YbG_Bs_Uby3f_Va_Gu1f_Ba3"))
    decrypted_message = ""
    for ch in encrypted_message:
        
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]

# Given a string 'message' and a secret key 'key', write a Python function to encrypt the message using the Caesar cipher
