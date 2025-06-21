
# Silicon Data Sleuthing – CTF Walkthrough

## Challenge Description

> In the dust and sand surrounding the vault, you unearth a rusty PCB... You try to read the etched print, it says Open..W...RT, a router!  
> You hand it over to the hardware gurus and to their surprise the ROM chip is intact!  
> They manage to read the data off the tarnished silicon and give you back a firmware image.  
> It's now your job to examine the firmware and maybe recover some useful information that will be important for unlocking and bypassing some of the vault's countermeasures!

---

## Tools Used

- `binwalk`
- `jefferson`
- `tar`, `gzip`
- `cat`, `grep`
- Basic Linux commands

---

## Step 1: Extract the Firmware

```bash
binwalk -e router_dump.bin
```

This extracts the embedded file systems into:

```
./_router_dump.bin.extracted/squashfs-root/
```

---

## 📦 Step 2: Identify OpenWRT Version

```bash
cd squashfs-root/etc
cat openwrt_release
```

**Answer:** `23.05.0`

---

##  Step 3: Find the Linux Kernel Version

```bash
cat usr/lib/opkg/status | grep -A5 "Package: kernel"
```

Look for:

```
Version: 5.15.134-...
```

**Answer:** `5.15.134`

---

## Step 4: Extract Root Password Hash

### Install `jefferson`:

```bash
pip install jefferson
```

### Extract the JFFS2 layer:

```bash
jefferson -d jffs2_output jffs2-rootfs.img
cd jffs2_output/upper
gzip -d sysupgrade.tgz
tar -xf sysupgrade.tar
cd etc
cat shadow
```

**Answer:**  
`root:$1$YfuRJudo$cXCiIJXn9fWLIt8WY2Okp1:19804:0:99999:7:::`

---

## Step 5: Find PPPoE Username & Password

```bash
cat config/network
```

**Answers:**

- **Username:** `yohZ5ah`
- **Password:** `ae-h+i$i^Ngohroorie!bieng6kee7oh`

---

## Step 6: Find Wi-Fi SSID and Password

```bash
cat config/wireless
```

**Answers:**

- **SSID:** `VLT-AP01`
- **WiFi Password:** `french-halves-vehicular-favorable`

---

## Step 7: Identify WAN Port Forwards

```bash
cat config
```

Look for port forwarding rules like:

```
option src_port '1778'
option src_port '2289'
option src_port '8088'
```

**Answer:** `1778,2289,8088`

---

## Final Flag

```
HTB{Y0u'v3_m4st3r3d_0p3nWRT_d4t4_3xtr4ct10n!!_31568569a249b437b55acda862f16d27}
```

---

## Summary of Answers

| Question                           | Answer                                                  |
|------------------------------------|----------------------------------------------------------|
| **OpenWRT Version**                | `23.05.0`                                               |
| **Kernel Version**                 | `5.15.134`                                              |
| **Root Password Hash**            | `root:$1$YfuRJudo$cXCiIJXn9fWLIt8WY2Okp1:19804:0:99999:7:::` |
| **PPPoE Username**                | `yohZ5ah`                                               |
| **PPPoE Password**                | `ae-h+i$i^Ngohroorie!bieng6kee7oh`                      |
| **WiFi SSID**                      | `VLT-AP01`                                              |
| **WiFi Password**                  | `french-halves-vehicular-favorable`                    |
| **WAN → LAN Ports**                | `1778,2289,8088`                                        |
| **Final Flag**                     | `HTB{Y0u'v3_m4st3r3d_0p3nWRT_d4t4_3xtr4ct10n!!_...}`     |

---

Feel free to share this repo if you found it helpful!
