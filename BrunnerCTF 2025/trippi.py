import base64
import hashlib

s = "qjuA_QZVI_ua24NQ}fM1hX4ecdyVShKb2vJjeQJ@Jz=zws0^9Enr1fR+Em_5w2j=p4)2<#m3EZ?m3Oo@"

# Base85 decode
b85_decoded = base64.b85decode(s)   # step_four

# Reverse the reversal
reversed_again = b85_decoded[::-1]  # step_three

# Reverse the linear transformation: (x * 7) % 256 = c -> x = (c * inv(7)) % 256
inv7 = pow(7, -1, 256)   # Modular inverse of 7 mod 256 is 183
step_two = bytes([ (c * inv7) % 256 for c in reversed_again ])

# Compute the key: first 7 bytes of SHA256(b"skibidiskibidi")
key = hashlib.sha256(b"skibidiskibidi").digest()[:7]

# XOR cyclically with the key
flag_bytes = []
for i, c in enumerate(step_two):
    k = key[i % len(key)]
    flag_bytes.append(c ^ k)

flag = bytes(flag_bytes).decode()
print(flag)