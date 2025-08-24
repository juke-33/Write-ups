from sympy.ntheory import discrete_log

# Given parameters
p = 14912432766367177751
g = 2784687438861268863
h = 8201777436716393968
c1 = 12279519522290406516
c2 = 10734305369677133991

# Compute the private key x: solve g^x ≡ h (mod p)
x = discrete_log(p, h, g)
print(f"Private key x = {x}")

# Compute the shared secret s = c1^x mod p
s = pow(c1, x, p)

# Recover the plaintext m = c2 * s^(-1) mod p
s_inv = pow(s, -1, p)
m = (c2 * s_inv) % p
print(f"Recovered plaintext (as integer) = {m}")

# Convert the integer to bytes (assuming it represents a text string)
# First, convert to hex, then to bytes
hex_str = hex(m)[2:]
if len(hex_str) % 2 != 0:
    hex_str = '0' + hex_str
plaintext = bytes.fromhex(hex_str).decode('utf-8')
print(f"Recovered plaintext = '{plaintext}'")

# Wrap in flag format
flag = f"brunner{{{plaintext}}}"
print(f"Flag: {flag}")