import base64

giftcard = "HZvbp1XQ7JpKXeCWLGT/ndoInD6H7S1j2uaW74WCv7tLAqM="
cardbytes = bytearray(base64.standard_b64decode(giftcard))
print(map(hex, cardbytes))

print(base64.standard_b64encode(cardbytes))
