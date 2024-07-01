# Without a Trace

Gone with the wind, can you find my flag?

ncat --ssl without-a-trace.chal.uiuc.tf 1337

## Solution

While checking the server.py, we noticed that he multiplies 2 arrays.

Also the flag is divided by 5 letters when put in the array.

When we are prompted to put 5 numbers in the terminal this array we made is multiplied with the flag array.

So we tried different inputs to notice the output.
```bash
[WAT] Welcome
[WAT] Define diag(u1, u2, u3. u4, u5)
[WAT] u1 = 1
[WAT] u2 = 1
[WAT] u3 = 1
[WAT] u4 = 1
[WAT] u5 = 1
[WAT] Have fun: 2000128101369
```

Also tried with zerosbut the system recognized it and printed a custom message.
```bash
[WAT] Welcome
[WAT] Define diag(u1, u2, u3. u4, u5)
[WAT] u1 = 0
[WAT] u2 = 0
[WAT] u3 = 0
[WAT] u4 = 0
[WAT] u5 = 0
[WAT] It's not going to be that easy...
```

We thought that if we put negative numbers maybe we can get the result we want.

```bash
[WAT] Welcome
[WAT] Define diag(u1, u2, u3. u4, u5)
[WAT] u1 = -1
[WAT] u2 = 1
[WAT] u3 = 1
[WAT] u4 = 1
[WAT] u5 = 1
[WAT] Have fun: 991567152401
```

After this result, we noticed that if you substract the last number we found from the first number, the result would be the beggining of the flag.

So we put -1 in each position and followed the same operations untill we found the whole flag.

This is a simple script that does the math and prints the flag:
```python
from Crypto.Util.number import long_to_bytes

def process_numbers(firstNumber, numbers):
    results = []
    for num in numbers:
        result = (firstNumber - num) / 2
        results.append(int(result))
        
    byte_strings = [long_to_bytes(res) for res in results]
    print(b''.join(byte_strings).decode('utf-8'))

if __name__ == "__main__":
    firstNumber = 2000128101369
    numbers = [
        991567152401, 
        1119812315025, 
        1148065938747, 
        1672423010575, 
        1068515887359
    ]
    process_numbers(firstNumber, numbers)
```


Flag: `uiuctf{tr4c1ng_&&_mult5!}`