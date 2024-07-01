from itertools import cycle

# Given ciphertext file
ciphertext_file = "ct"

# Read the ciphertext
with open(ciphertext_file, "rb") as f:
    ct = f.read()

# We know the flag starts with "uiuctf{"
known_plaintext = b"uiuctf{"

# XOR the first 7 bytes of ciphertext with the known plaintext to get the key
partial_key = bytes(ct_byte ^ pt_byte for ct_byte, pt_byte in zip(ct[:7], known_plaintext))

# The key is 8 bytes long, we can deduce the 8th byte by XORing the 8th byte of the ciphertext with the 8th character of the flag
# Here we assume the 8th character of the flag is the first character after '{' which could be any valid character, we will brute-force it
for i in range(256):
    potential_key = partial_key + bytes([i])
    decrypted_flag = bytes(ct_byte ^ key_byte for ct_byte, key_byte in zip(ct, cycle(potential_key)))
    if decrypted_flag.startswith(b"uiuctf{") and decrypted_flag.endswith(b"}"):
        print(decrypted_flag.decode())
        break