## Discription:

Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!
## Challenge: Flag Extraction from a Server

### Problem Overview
This challenge involved connecting to a remote server at a specific IP address and port using the `Netcat (nc)` command. The server prompts for a number, and for each number, it responds with a character at that position in a flag. The objective was to loop through the sequence, collect the characters, and form the complete flag.

### Approach

1. **Initial Discovery:**
   - I connected to the server using `nc` and discovered that it requests a number from 0 upwards.
   - For each number I sent, the server would respond with the character at that index of the flag.

2. **Script Writing:**
   - I wrote a **bash script** to automate the process of sending numbers from `0` to `15` (or more depending on the number of characters).
   - The script loops through the numbers and collects each corresponding character from the server’s response.

3. **Flag Construction:**
   - The server gives a response like: "Character at Index 0: H".
   - The script extracts each character and appends it to a growing string representing the flag.
   - The process continues until the flag ends with a `}` character, which typically marks the end of the flag.

4. **Completion:**
   - The script finishes when the full flag is constructed, and the challenge is solved.

### Tools Used:
- **Netcat (nc)**: To communicate with the server.
- **Bash scripting**: To automate the process and loop through the indices.
- **`sed` and `awk`**: To extract the relevant part of the server’s response.

### Full Solution Script:
The complete solution is in the `flag_extraction.sh` file. To run the script:

```bash
chmod +x flag_extraction.sh
./flag_extraction.sh
