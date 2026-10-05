# XG8 Password Keeper — Cryptographic Spec & Recovery Tool

> **Your keys. Your data. Absolute zero-knowledge.**

Welcome to the open-source transparency repository for **XG8 Password Keeper**.

---

## What Happens If XG8 Disappears Tomorrow?

Most cloud password managers hold your data hostage: if their servers crash, their company goes bankrupt, or your internet drops, you are locked out of your digital life.

**With XG8, you are always in complete control.**

Because XG8 is **local-first** and **zero-knowledge**:
1. Your passwords are encrypted on your phone *before* anything is saved.
2. We never hold your Master Password or your decryption keys.
3. You can export an encrypted copy of your entire vault at any time.
4. **Even if XG8's servers are wiped off the internet, you can recover every single username and password yourself using your Master Password.**

---

## How to Back Up Your Passwords (In 3 Taps)

You don't need any technical skills to back up your data:

1. Open the **XG8 Password Keeper** app on your Android device.
2. Tap **Settings** (⚙️) $\rightarrow$ **Export Vault**.
3. Choose **Save to Device** or send it to your private cloud storage (Google Drive, Nextcloud, or email to yourself).

This gives you a secure backup file ending in `.json`. Even if someone steals this file, **it is completely unreadable without your Master Password**.

---

## Emergency Offline Recovery (If You Can't Access the App)

If you ever lose your phone, uninstall the app, or need your passwords on a desktop computer without contacting our servers:

### Option A: Restore to Another Android Phone
Simply install XG8 Password Keeper on any Android device, tap **Settings $\rightarrow$ Import Vault**, choose your backup file, and type your Master Password.

### Option B: Decrypt Offline on Any Computer (Using Python)
You can view your passwords directly on your computer with no internet connection:

1. Download [`decrypt.py`](./decrypt.py) from this repository.
2. Place your exported vault file in the same folder.
3. Open your computer's terminal or command prompt and run:
   ```bash
   pip install cryptography
   python decrypt.py my_vault_backup.json   
4. Enter your Master Password when prompted. Your credentials will decrypt and display instantly on your screen.

---

## For Developers & Security Auditors

Want to inspect the cryptographic mathematics powering our zero-knowledge engine?

* Read the mathematical proofs, round iterations, and memory lifetimes in **[`SPEC.md`](https://www.google.com/search?q=./SPEC.md)**.
* **Algorithm Standard:** PBKDF2-HMAC-SHA256 (600,000 rounds) + RFC 5869 HKDF-Expand + AES-256-GCM.

---

* 🌐 **Official Website:** [xg8.app](https://xg8.app)
* 📱 **Google Play:** [Download XG8 on Google Play](https://play.google.com/store/apps/details?id=app.xg8.passkeeper)
