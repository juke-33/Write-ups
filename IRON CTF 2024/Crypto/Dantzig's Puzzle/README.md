## Challenge

Dantzig's Puzzle

Dantzig was on a trip with his friends and one day, they decided to play a game or atleast, it's easier version. He would think of a string and the others have to find it based on the clues he gives them.

1. The knapsack list contains 8 numbers, with 1 and 2 as the first two numbers and the subsequent numbers are formed by adding one to the sum of all the numbers before.

2. The value of m=257 and n is something less than 257

3. The encrypted string is - [538, 619, 944, 831, 360, 531, 468, 971, 635, 593, 655, 425, 1068, 530, 1068, 360, 706, 1068, 299, 619, 670, 1068, 891, 425, 670, 1068, 371, 670, 732, 531, 1068, 484, 372, 635, 371, 372, 237, 237, 1007]

Can you find the string Dantzig was thinking of?

Flag Format: ironCTF{this_is_fake}

## Solution

We first create the list which is knapsack = [1, 2, 4, 8, 16, 32, 64, 128] according to the description.

Then we made a script to solve the problem and we got the flag.

Since we cant find the n, we will brute force it.

```
from sympy import mod_inverse

# Given values
m = 257
encrypted_values = [
    538, 619, 944, 831, 360, 531, 468, 971, 635, 593, 655, 425, 
    1068, 530, 1068, 360, 706, 1068, 299, 619, 670, 1068, 891, 425, 
    670, 1068, 371, 670, 732, 531, 1068, 484, 372, 635, 371, 372, 
    237, 237, 1007
]

knapsack = [1, 2, 4, 8, 16, 32, 64, 128]

# Function to decrypt a single ciphertext using the knapsack
def decrypt_value(ciphertext):
    binary_repr = [0] * 8  # 8-bit binary
    remaining_value = ciphertext
    
    for i in reversed(range(8)):
        if knapsack[i] <= remaining_value:
            binary_repr[i] = 1
            remaining_value -= knapsack[i]
    
    return binary_repr

# Function to decrypt using a given n and its inverse mod m
def try_decrypt_with_new_n(ciphertext, inv_mod):
    decrypted_vals = []
    for value in ciphertext:
        decrypted_vals.append((value * inv_mod) % m)
    return decrypted_vals

# Try all possible values of n < m
def brute_force_decrypt():
    for n_test in range(1, 257):
        try:
            n_inverse = mod_inverse(n_test, m)
            decrypted_vals = try_decrypt_with_new_n(encrypted_values, n_inverse)
            decoded_bits = [decrypt_value(val) for val in decrypted_vals]
            decoded_chars = ''.join(bits_to_char(bits) for bits in decoded_bits)
            
            if "ironCTF" in decoded_chars:
                return decoded_chars
        except:
            continue

# Convert binary sequence to ASCII character
def bits_to_char(bits):
    return chr(int(''.join(map(str, bits)), 2))

# Print flag
flag = brute_force_decrypt()
print(flag)

```


Flag: `ironCTF{M4th_&_C5_ar3_7h3_b3sT_c0Mb0!!}`