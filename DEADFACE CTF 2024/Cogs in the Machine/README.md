## Challenge

Cogs in the Machine [250]

We intercepted this internal communcation between DEADFACE members, but all of our attempts to decipher the message have failed. Use your skills in cryptanalysis to decipher the hidden message.

```
Fsqp: rbkrkqqe
Ie: zb0oq404

Vygplkc: Fus Tfgkm Woc Oqgq

mo0bd,
Gvt mwbf ep shjpqmsm njceqe ixrf C aundcugg. Cl'eo sbh q obhykt, bvv my'z wkcdbk. Kzx jpecqs cuis'a bopuau yk ryo, ztt vki ypowkw vg scwtl kk ly gqh. Mwuvzi hwu mlovh nzti, fzz bjup n auwl uo qfd dtrwxxvim etvg jzex.
Pec gbvhojkwmac ibb'j fhndyb shf vanzjp... lsi.

Mbz cjzmf kex imnx xvh, rfw nkll tig wmgkwfc ivza dgoy. Yss sgpirhlz, etvg yjf'n frqs bprxmky yvlk. Iydaga ep dvftbxmouo.
Oaa'i cwm odbk sokij evc yff.

Vcsz: biyf{7j3_Kr4u3_Y3i3g_Ua3m}
```

## Solution

In the last line of the file we are given,there is a flag{} format string

We noticed that if we increase the first letter by 4, we get letter f

In the second letter, if we increase by 3, we get letter l

So there is a pattern

After that notice we made a script to solve it automatically and do not affect numbers, brackets and underscores.

```
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
```

It gave us the flag


Flag: `flag{7h3_Fl4m3_N3v3r_Di3s}`