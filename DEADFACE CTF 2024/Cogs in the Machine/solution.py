def decode_flag(encoded_str):
    decoded_flag = ""
    shift = 4
    
    for char in encoded_str:
        if char.isalpha():
            if char.islower():
                decoded_flag += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                decoded_flag += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            decoded_flag += char
        shift -= 1

    return decoded_flag

encoded_flag = "biyf{7j3_Kr4u3_Y3i3g_Ua3m}"
decoded_flag = decode_flag(encoded_flag)
print(decoded_flag)
