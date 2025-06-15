# Discripion:
You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!
# Solution:
Solution to Decrypt the Encrypted Flag

This script demonstrates how to decrypt a message that has been encrypted using a specific encryption method. The encryption involves shifting characters based on their position in the string, and this solution reverses that process to recover the original flag.
Key Concepts:

    ord(): This function converts a character to its corresponding ASCII value. In the context of the encryption, we subtract 0x41 (which is 65 in decimal) to map characters A-Z to numbers 0-25.

    chr(): This function converts a numeric value (ASCII value) back to a character. After reversing the shift, we convert the resulting number back to a character.

    isalpha(): This method checks if a character is an alphabet letter (A-Z). Non-alphabet characters (like _, ?, etc.) are not encrypted or decrypted.

Encryption Overview:

    The original encryption function maps each character to a number by subtracting 0x41 (so A becomes 0, B becomes 1, ..., Z becomes 25).

    It then adds the index of the character in the string to this number.

    The number is then mapped back to a character.

    Non-alphabet characters remain unchanged.

Decryption Process:

To decrypt the message, we need to reverse these steps:

    Convert each encrypted character back to a number.

    Subtract the index of the character to undo the shifting.

    Convert the result back to a character.
