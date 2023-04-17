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
