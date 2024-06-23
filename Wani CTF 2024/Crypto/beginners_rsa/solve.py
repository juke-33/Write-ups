from sympy import mod_inverse, Mul
from Crypto.Util.number import *

# Given values
primes = [
    13079524394617385153, 
    12109985960354612149, 
    9953162929836910171, 
    11771834931016130837, 
    17129880600534041513
]

N = 317903423385943473062528814030345176720578295695512495346444822768171649361480819163749494400347
e = 65537
enc = 127075137729897107295787718796341877071536678034322988535029776806418266591167534816788125330265

# Reconstruct N from given primes and verify
N_reconstructed = Mul(*primes)

# Compute phi(N)
phi_N = Mul(*(p - 1 for p in primes))

# Calculate the private exponent d
d = mod_inverse(e, phi_N)

# Decrypt the ciphertext
M = pow(enc, d, N)

N_reconstructed, phi_N, d, M

print(long_to_bytes(M))