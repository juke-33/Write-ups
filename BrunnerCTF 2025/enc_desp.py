import os
from pathlib import Path
from itertools import cycle

TARGET_DIR = Path("./recipes/")

# Known PNG header (first 16 bytes)
KNOWN_PNG_HEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52'

def recover_key(enc_file: Path, known_plaintext: bytes) -> bytes:
    with open(enc_file, "rb") as f:
        ciphertext = f.read(16)  # Read first 16 bytes
    if len(ciphertext) < 16:
        raise ValueError(f"File {enc_file} is too small to recover key.")
    key = bytes(a ^ b for a, b in zip(ciphertext, known_plaintext))
    return key

def decrypt(file: Path, key: bytes) -> None:
    with open(file, "rb") as f:
        ciphertext = f.read()
    plaintext = bytes(a ^ b for a, b in zip(ciphertext, cycle(key)))
    original_file = file.with_suffix('')  # Remove .enc extension
    with open(original_file, "wb") as f:
        f.write(plaintext)
    print(f"Decrypted {file.name} to {original_file.name}")
    # Optionally: file.unlink()  # Delete encrypted file

if __name__ == "__main__":
    # Assume you have a photo file that is a PNG, replace 'photo.png.enc' with actual file name
    enc_photo = TARGET_DIR / "1f.png.enc"  # Change this to your actual encrypted photo file name
    
    try:
        key = recover_key(enc_photo, KNOWN_PNG_HEADER)
        print(f"Recovered key: {key.hex(' ')}")
    except Exception as e:
        print(f"Error recovering key: {e}")
        print("Make sure the file is an encrypted PNG and adjust the file name.")
        exit(1)
    
    print("Decrypting files...")
    for file in TARGET_DIR.rglob("*.enc"):
        if file.is_file():
            decrypt(file, key)