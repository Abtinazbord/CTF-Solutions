# HTB Challenge: An Unusual Sighting
 
**Files Provided:** `sshd.log`, `bash_history.txt`  
**Flag:** `<details> <summary>Click to reveal the flag </summary> HTB{4n_unusual_s1ght1ng_1n_SSH_l0gs!} </details>

## Challenge Description

> As The Fray draws near, our team begins working on refactoring the new CMS app.  
> However, work mysteriously disappears! We've extracted SSH logs and bash history from the dev server.  
> Can you uncover the attacker’s actions?


## Goal

We are tasked with answering the following questions:

1. What is the IP and Port of the SSH connection?  
2. When was the first successful login?  
3. When was the unusual login?  
4. What is the attacker’s public key fingerprint?  
5. What was the first command they ran?  
6. What was the last command before logging out?


## Investigation Steps

### 1. IP Address and Port of SSH Server

Looking through `sshd.log`, we find:
Accepted publickey for devuser from 100.107.36.130 port 2221 ssh2


**Answer:** `100.107.36.130:2221`


### 2. First Successful Login

In the same log:

2024-02-13 11:29:50 Accepted publickey for softdev from ...


 **Answer:** `2024-02-13 11:29:50`


### 3. Unusual Login Time

Clue: operating hours are **09:00–19:00**.

In `bash_history.txt`, we see an early morning activity:
[2024-02-19 04:00:18] whoami


**Answer:** `2024-02-19 04:00:14`

---

### 4. Attacker’s Public Key Fingerprint

From `sshd.log`:
Accepted publickey for devuser from 100.107.36.130 port 2221 ssh2: RSA OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4

**Answer:** `OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4`

### 5. First Command Executed by Attacker

From `bash_history.txt`, the attacker logs in at `04:00:14`, and we see:
[2024-02-19 04:00:18] whoami

**Answer:** `whoami`

### 6. Final Command Before Logout

Continuing in the same session:
[2024-02-19 04:14:02] ./setup

**Answer:** `./setup`


## Final Flag
**Flag:** <details> <summary>Click to reveal the flag </summary> HTB{4n_unusual_s1ght1ng_1n_SSH_l0gs!} </details>
