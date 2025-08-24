table = bytes.fromhex(
    "3d0334282b71162337712814232b3271262674360b2336700a23742471360a2324773715233570193f362532323536267e7e07010f057e7e"
)

# 1) XOR with 0x42
s = bytearray(b ^ 0x42 for b in table)

# 2) decrement all bytes by 1
s = bytearray((b - 1) & 0xff for b in s)

# 3) reverse the whole thing
s = s[::-1]

raw = s.decode("latin-1")

# 4) final Caesar −1 on letters/digits (and prettify separators)
def caesar_minus1_letters_digits(txt):
    out = []
    for ch in txt:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - 97 - 1) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - 65 - 1) % 26 + 65))
        elif '0' <= ch <= '9':
            out.append(chr((ord(ch) - 48 - 1) % 10 + 48))
        else:
            out.append(ch)
    return "".join(out)

msg = caesar_minus1_letters_digits(raw).replace('`',' ').replace('|',' ')

print("raw :", raw)
print("text:", msg)
