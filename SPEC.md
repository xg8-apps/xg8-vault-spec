# Cryptographic Architecture & Invariants

XG8 Password Keeper enforces an uncompromising zero-knowledge boundary. 
The backend server never receives, stores, or handles the user's Master Password, derived master key, or raw vault payload.

## Key Derivation (Local-First)
1. **PBKDF2-HMAC-SHA256**:
   - Iterations: 600,000
   - Salt: User email (normalized lowercase, trimmed)
   - Output: 256-bit Master Key (MK)

2. **HKDF-Expand (Key Segregation)**:
   - To prevent cross-protocol key reuse, the Master Key is segregated using RFC 5869 HKDF-Expand into dedicated domain keys:
     - `AuthKey` = HKDF-Expand(MK, "xg8-auth-verification-key", 32)
     - `VaultKey` = HKDF-Expand(MK, "xg8-vault-encryption-key", 32)

## Data Encryption
- **Algorithm**: AES-256-GCM (Authenticated Encryption with Associated Data).
- **Nonce/IV**: Cryptographically secure random 96-bit (12-byte) initialization vector per record.
- **Integrity**: 128-bit authentication tag appended to every ciphertext to detect tampering.

## Memory Lifetime & Process Isolation
- The `VaultKey` resides strictly in volatile Android process memory.
- Locked-state credential capture routes through a private `PendingSaveManager` buffer enforcing an automatic 180-second TTL self-destruct and explicit memory zeroing (`Arrays.fill('\u0000')`).
