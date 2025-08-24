import base64

# The input string
input_str = "89|89.21|55.13.5.1|34.13.2|89.8.1|89.13.5.2|34.13.5.1|89.13.5.1|89.8.2|89.21|89.21.5|34.13.3.1|89.8|55.13|55.21.2|89.13|89.1|89.21.8.3.1|55.8.2|89.21.8.2|89.1|55.13|55.21.2|89.21.5.2|55.21.8.3.1|34.13.3.1|55.8.3|89.21.1|55.21.1|55.21.8.2|55.1|89.21.8.1|89.1|89.13.5.1|55.2|34.13.5.2|89.1|55.21.8.3|55.21.2|89.21.3.1|89.1|55.21.8.3|34.13.5.1|89.13.5|89.8.1|34.13.3.1|55.13.5.1|89.13.5.2|89.13|55.21.5|55.5.1|55.5.1"

# Split the input into groups
groups = input_str.split('|')

# List to store the summed values for each group
sums = []

# Process each group
for group in groups:
    # Split the group by '.' to get individual Fibonacci numbers
    numbers = group.split('.')
    # Convert each to integer and sum
    total = sum(int(num) for num in numbers)
    sums.append(total)

# Convert the sums to ASCII characters
ascii_chars = [chr(s) for s in sums]

# Combine into a string
base64_str = ''.join(ascii_chars)

# Decode the base64 string
decoded_bytes = base64.b64decode(base64_str)
flag = decoded_bytes.decode('utf-8')

print("Sums (ASCII codes):", sums)
print("Base64 string:", base64_str)
print("Decoded flag:", flag)