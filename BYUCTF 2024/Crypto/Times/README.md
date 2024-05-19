# Times

## It's just multiplication... right?

I wrote a script with the help of ChatGPT that finds the flag:
```
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def point(self, x, y=None):
        if y is not None:
            return Point(self, x, y)
        else:
            # For simplicity, assume x is provided and y needs to be calculated
            # This is not complete as it doesn't handle cases where y^2 = x^3 + ax + b has no solution
            return Point(self, x, self._calculate_y(x))

    def _calculate_y(self, x):
        # We need to find a y such that (y^2) % p = (x^3 + ax + b) % p
        rhs = (x**3 + self.a * x + self.b) % self.p
        for y in range(self.p):
            if (y * y) % self.p == rhs:
                return y
        raise ValueError("No valid y found")

class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y

    def __add__(self, other):
        if self.x == other.x and self.y != other.y:
            return Point(self.curve, 0, 0)  # Point at infinity
        if self == other:
            s = (3 * self.x**2 + self.curve.a) * pow(2 * self.y, -1, self.curve.p)
        else:
            s = (other.y - self.y) * pow(other.x - self.x, -1, self.curve.p)
        s = s % self.curve.p
        x_r = (s**2 - self.x - other.x) % self.curve.p
        y_r = (s * (self.x - x_r) - self.y) % self.curve.p
        return Point(self.curve, x_r, y_r)

    def __mul__(self, n):
        result = self
        for _ in range(n - 1):
            result += self
        return result

# Provided encryption parameters and results
curve_a = 13
curve_b = 245
curve_p = 335135809459196851603485825030548860907
point_x = 14592775108451646097
point_y = 237729200841118959448447480561827799984
multiplication_factor = 1337

ciphertext_b64 = 'SllGMo5gxalFG9g8j4KO0cIbXeub0CM2VAWzXo3nbIxMqy1Hl4f+dGwhM9sm793NikYA0EjxvFyRMcU2tKj54Q=='
iv_b64 = 'MWkMvRmhFy2vAO9Be9Depw=='

# Step 1: Reconstruct the elliptic curve
curve = EllipticCurve(curve_a, curve_b, curve_p)

# Step 2: Reconstruct the point
start_point = Point(curve, point_x, point_y)

# Step 3: Compute the new point by multiplying the starting point by 1337
new_point = start_point * multiplication_factor

# Step 4: Derive the shared secret (x-coordinate of the new point)
shared_secret = new_point.x

# Step 5: Derive the AES key from the shared secret
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16]

# Step 6: Decrypt the ciphertext
ciphertext = b64decode(ciphertext_b64)
iv = b64decode(iv_b64)

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext_padded = cipher.decrypt(ciphertext)
plaintext = unpad(plaintext_padded, AES.block_size).decode('ascii')

print("Decrypted flag:", plaintext)
```

Flag: `byuctf{mult1pl1c4t10n_just_g0t_s0_much_m0r3_c0mpl1c4t3d}`