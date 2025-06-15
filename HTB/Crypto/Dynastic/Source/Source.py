from secret import FLAG       # Imports the flag here!
from random import randint

def to_identity_map(a): #--> subtracts the hex value of "A" for each char
    return ord(a) - 0x41 # same as - ord("A")

def from_identity_map(a):
    return chr(a % 26 + 0x41) # takes a numeric input and puts it back to a character

def encrypt(m):
    c = ''  #empty string as a place holder for the encrypted flag
    for i in range(len(m)):
        print(i)
        ch = m[i]
        print(ch)
        if not ch.isalpha(): #if character is not in alphabet dont change it
            ech = ch
        else:
            chi = to_identity_map(ch)  # chi is a number
            ech = from_identity_map(chi + i)
        c += ech
    return c

with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))
