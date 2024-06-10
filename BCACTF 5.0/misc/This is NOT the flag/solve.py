import base64

encoded_str = "nZyenIuZhMiXtoygzoygyJfMoJmTnsaC"
decoded_bytes = base64.b64decode(encoded_str)

def xor_characters(s, key):
    return ''.join(chr(ord(char) ^ key) for char in s)

for key in range(256):
    xored = xor_characters(decoded_bytes.decode('latin1'), key)
    if "bcactf{" in xored:
        print(f"XOR {key}: {xored}")