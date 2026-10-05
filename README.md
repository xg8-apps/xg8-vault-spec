Step 4: Update README.md (The Public Trust Landing)
On your repository page, click on README.md in the file list.

In the top-right corner of the file preview, click the pencil icon (Edit this file).

Replace the contents completely with this:

Markdown
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
Run the decryptor:

Bash
python decrypt.py my_vault_backup.json
Verification
You can inspect SPEC.md to verify the mathematical invariants implemented across our Android client and backend API.

Website: x-gate.app

Google Play: XG8 Password Keeper on Google Play
https://play.google.com/store/apps/details?id=app.xg8.keeper
