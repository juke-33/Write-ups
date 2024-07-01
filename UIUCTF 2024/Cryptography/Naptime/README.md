# Naptime

I'm pretty tired. Don't leak my flag while I'm asleep.

## Solution

The pub.txt contained some numbers.

We noticed that the ct numbers are forming the "uiu" in the beggining so we tried to make a script to find the rest of the characters.

This is the script we made that gave us the flag.
```python
flag = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}_!@#$%^&*()"

# values from given pub.txt
a = [66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]

# values from given pub.txt
temp = [273896, 179019, 273896, 247527, 208558, 227481,
        328334, 179019, 336714, 292819, 102108, 208558,
        336714, 312723, 158973, 208700, 208700, 163266,
        244215, 336714, 312723, 102108, 336714, 142107,
        336714, 167446, 251565, 227481, 296857, 336714,
        208558, 113681, 251565, 336714, 227481, 158973,
        147400, 292819, 289507]

bitstrings = []
for c in flag:
    bitstrings.append(bin(ord(c))[2:].zfill(8))

ct = []

for bits in bitstrings:
    curr = 0
    for i, b in enumerate(bits):
        if b == "1":
            curr += a[i]
    ct.append(curr)

for i in range(len(flag)):
    print(flag[i], ct[i])

final = ""

for t in temp:
    ind = ct.index(t)
    final += flag[ind]

print(final)
```


Flag: `uiuctf{i_g0t_sleepy_s0_I_13f7_th3_fl4g}`