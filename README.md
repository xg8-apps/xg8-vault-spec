# XG8 Cryptographic Specification & Offline Decryptor

> **Your keys. Your data. Absolute zero-knowledge.**

This repository contains the official cryptographic specification and offline extraction tooling for **XG8 Password Keeper**.

### Why This Repo Exists
We believe you should never trust a password manager that holds your data hostage. 
Even if our servers go offline, our company disappears, or Google Play is unreachable, **you can always recover every single credential you own.**

### Offline Recovery
To inspect or decrypt your encrypted vault export locally without contacting any server:

1. Clone this repository or download `decrypt.py`.
2. Install the standard Python cryptography library:
   ```bash
   pip install cryptography
