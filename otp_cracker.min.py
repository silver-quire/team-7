import base64
from itertools import cycle

def xor(a1, a2):
    return map(
            lambda (x,y): x ^ y,
            zip(a1, a2)
        )

def decrypt_cc(key, encrypted):
    return "".join(map(chr, xor(cycle(key), encrypted)))

cc1 = "krSKla6Hk7aGjLWKmbGflbCFkA=="
cc2 = "l7uLl66AmLWFjLCHkrKfl7KCmQ=="

cc1b = bytearray(base64.standard_b64decode(cc1))
cc2b = bytearray(base64.standard_b64decode(cc2))

xored = xor(cc1b, cc2b)

print(map(hex, cc1b))
print(map(hex, cc2b))
print(map(hex, xored))

