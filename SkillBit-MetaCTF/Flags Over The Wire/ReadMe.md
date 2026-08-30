# Flags Over The Wire
 
**Platform:** Skill Bit (previously MetaCTF)
 
**Description:** When two computers communicate over a network, they exchange tens, hundreds, or perhaps thousands of packets. These connections send data over protocols such as SSH, HTTP, or FTP. Here we've managed to record a packet capture between two computers talking over FTP. One of them downloaded a file from the other. Can you recover the file they downloaded in this packet capture?
 
## Approach
 
The description tells us data was sent over a protocol, so the goal is to find a file that was transferred inside this capture and pull it back out.
 
## Step 1: See what is in the capture
 
Open the pcap in Wireshark and go to **Statistics > Protocol Hierarchy**. This gives a breakdown of every protocol in the capture and how much of the traffic each one accounts for. Here we see FTP for the commands and FTP-DATA for the actual file transfer, so that is where the file will be.
 
## Step 2: Read the FTP conversation
 
Type `ftp` in the display filter bar at the top to show only the FTP control packets. Right click any of them and choose **Follow > TCP Stream**.
 
FTP sends everything in cleartext, so the whole conversation is readable:
 
- The user logged in as `hack0r` with the password `Chiapet2`
- Further down the stream there is a `RETR` command showing the file being downloaded
Credentials showing up in plaintext like this is the whole reason FTP has been replaced by SFTP and FTPS on real networks.
 
## Step 3: Export the file
 
Go to **File > Export Objects > FTP-DATA**. Wireshark lists every file that was transferred over the data channel. Select the file and save it somewhere on your machine.
 
The recovered file is `flags.png`.
 
## Step 4: Get the flag out of the image
 
Opening the PNG shows the flag, but since it is an image you cannot copy and paste it into the submission box. You can retype it by hand, or if you are lazy like me you can run OCR on it.
 
Install tesseract:
 
```bash
sudo apt install tesseract-ocr tesseract-ocr-eng
```
 
Then print the text from the image straight to the terminal:
 
```bash
tesseract flags.png stdout
```
 
Now you have the flag as text. Enjoy.
 
## Takeaway
 
FTP has no encryption, so anyone capturing the traffic gets the username, the password, and a full copy of every file transferred. Wireshark's Export Objects feature rebuilds those files from the raw packets for you, which makes this kind of recovery a two click job.
