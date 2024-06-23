encoded_string = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'

# Decode from base-36 and add 10
base36_decoded = [chr(int(c, 36) + 10) for c in encoded_string.split('_')]

# Reverse transformations
# XOR with 123
xored = ''.join([chr(123 ^ ord(c)) for c in base36_decoded])

# Shift by -3
shifted = ''.join([chr(ord(c) + 3) for c in xored])

# Shift by +12
flag = ''.join([chr(ord(c) - 12) for c in shifted])

print(flag)
