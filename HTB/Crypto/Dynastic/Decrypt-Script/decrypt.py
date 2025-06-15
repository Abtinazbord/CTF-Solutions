def decrypt(m):
    c = ''  # Empty string for decrypted message
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():  # If character is not alphabetic, don't change it
            ech = ch
        else:
            # Reverse the 'i' shift added during encryption
            chi = ord(ch) - 0x41  # Convert char to a number (0 for 'A', 25 for 'Z')
            chi = (chi - i) % 26  # Subtract the index to reverse the offset
            ech = chr(chi + 0x41)  # Convert back to character

        c += ech
    return c

# Test the decryption
encrypted_message = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
decrypted_message = decrypt(encrypted_message)
print(decrypted_message)
