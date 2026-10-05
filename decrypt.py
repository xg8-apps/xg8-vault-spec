#!/usr/bin/env python3
"""
XG8 Password Keeper - Offline Recovery & Decryption Tool
Zero-knowledge proof-of-work: Decrypts an exported XG8 vault completely offline.
Dependencies: pip install cryptography
"""

import sys
import json
import base64
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ITERATIONS = 600_000
KEY_LENGTH = 32  # 256 bits

def derive_keys(master_password: str, email: str):
    # 1. PBKDF2-HMAC-SHA256 (600,000 rounds)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=email.lower().strip().encode('utf-8'),
        iterations=ITERATIONS,
    )
    master_key = kdf.derive(master_password.encode('utf-8'))

    # 2. HKDF-Expand for Vault Encryption Key
    hkdf_vault = HKDFExpand(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        info=b"xg8-vault-encryption-key"
    )
    vault_key = hkdf_vault.derive(master_key)
    return vault_key

def decrypt_payload(vault_key: bytes, nonce_b64: str, ciphertext_b64: str) -> str:
    nonce = base64.b64decode(nonce_b64)
    ciphertext = base64.b64decode(ciphertext_b64)
    
    aesgcm = AESGCM(vault_key)
    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted_bytes.decode('utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <exported_vault.json>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        vault_data = json.load(f)

    email = vault_data.get("email") or input("Account Email: ")
    password = getpass.getpass("Master Password: ")

    print("\n[+] Deriving keys using PBKDF2 (600,000 iterations)...")
    vault_key = derive_keys(password, email)

    print(f"[+] Decrypting {len(vault_data.get('items', []))} vault items...\n")
    print("-" * 60)

    for item in vault_data.get("items", []):
        try:
            decrypted_user = decrypt_payload(vault_key, item['nonce'], item['encrypted_username'])
            decrypted_pass = decrypt_payload(vault_key, item['nonce'], item['encrypted_password'])
            title = item.get('title', 'Unknown')
            print(f"Title:    {title}")
            print(f"Username: {decrypted_user}")
            print(f"Password: {decrypted_pass}")
            print("-" * 60)
        except Exception:
            print(f"[!] Failed to decrypt item {item.get('title')}: Authentication verification failed.")

if __name__ == "__main__":
    main()
