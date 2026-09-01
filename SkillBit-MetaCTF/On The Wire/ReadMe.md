# On The Wire

**Platform:** Skill Bit (previously MetaCTF)

**Description:** When we're investigating potentially malicious activity on the network, we like to take a packet capture (pcap) of the network traffic. Since you're new to the team, here's a basic pcap to get you warmed up to network analysis. There seems to be a plaintext authentication in there. Can you find out what password was used?

## Approach

The description gives away a lot here. The key phrase is "plaintext authentication," which tells us to look for protocols in this pcap that do not encrypt their traffic. If the login was encrypted we would only see ciphertext, so whatever protocol carried it has to be one that sends everything in the clear.

The common cleartext protocols worth checking are:

- HTTP
- FTP
- Telnet
- POP3, IMAP, and SMTP
- SNMP v1 and v2c

HTTP and FTP are the two most likely in a warmup challenge, so start there.

## Step 1: Filter for the cleartext protocols

In the display filter bar at the top of Wireshark, enter:

```
http or ftp
```

This hides everything except packets using those protocols. Wireshark display filters are lowercase, so `HTTP or FTP` will not work.

In this capture there are only two HTTP packets and no FTP packets at all, which narrows things down immediately.

You can confirm the same thing from **Statistics > Protocol Hierarchy**, which lists every protocol present in the capture and what percentage of the traffic each one makes up. That is a good habit for larger captures where guessing a filter is slower.

## Step 2: Follow the stream

Right click either HTTP packet and choose **Follow > HTTP Stream**. This reassembles the request and response into one readable conversation instead of making you click through packets one at a time.

## Step 3: Read the credentials

The credentials are sitting in the GET request at the top of the stream. Since the challenge only asks for the password, that is the flag.

## Takeaway

Any authentication sent over HTTP is readable by anyone who can capture the traffic. HTTP Basic authentication in particular is not encrypted at all, it is only base64 encoded, which is an encoding and not a protection. This is the entire reason logins belong over HTTPS.
