# HTB Challenge: An Unusual Sighting
 
**Files Provided:** `sshd.log`, `bash_history.txt`  
**Flag:** `<details> <summary>Click to reveal the flag </summary> HTB{4n_unusual_s1ght1ng_1n_SSH_l0gs!} </details>

## 🧩 Challenge Description

> As The Fray draws near, our team begins working on refactoring the new CMS app.  
> However, work mysteriously disappears! We've extracted SSH logs and bash history from the dev server.  
> Can you uncover the attacker’s actions?

Operating hours: **0900–1900**  
All timestamps use local time from the logs.

---

## 🧪 Goal

We are tasked with answering the following questions:

1. What is the IP and Port of the SSH connection?  
2. When was the first successful login?  
3. When was the unusual login?  
4. What is the attacker’s public key fingerprint?  
5. What was the first command they ran?  
6. What was the last command before logging out?

---

## 🔍 Investigation Steps

### 1. IP Address and Port of SSH Server

Looking through `sshd.log`, we find:
