from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import hashlib

# Encrypted message (enc) from the given example.
enc = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'

# Known parts of the key and IV.
key_base = b'the_enc_key_is_'
iv_base = b'my_great_iv_is_'

# The correct flag hash for verification.
correct_flag_hash = '6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e'

# Iterate over all possible combinations of appended random bytes for key and IV.
for key_suffix in range(256):
    for iv_suffix in range(256):
        # Construct the key and IV with the current suffix.
        key = key_base + bytes([key_suffix])
        iv = iv_base + bytes([iv_suffix])

        try:
            # Create a new AES cipher object with the current key, mode, and IV.
            cipher = AES.new(key, AES.MODE_CBC, iv)
            
            # Decrypt the message.
            decrypted_msg = cipher.decrypt(enc)

            # Unpad the decrypted message to get the original plaintext.
            original_msg = unpad(decrypted_msg, 16)

            # Check if the decrypted message hash matches the correct flag hash.
            if hashlib.sha256(original_msg).hexdigest() == correct_flag_hash:
                print(f'Success! The decrypted message is: {original_msg.decode()}')
                print(f'Key: {key}')
                print(f'IV: {iv}')
                break
        except (ValueError, KeyError):
            # If unpad or decrypt throws an error, skip to the next combination.
            continue
    else:
        # Continue only if the inner loop wasn't broken.
        continue
    # Break the outer loop if the inner loop was broken.
    break
