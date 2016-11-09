import itertools
import hashlib
import hmac

lower_alpha_characters = (chr(x) for x in range(97, 123))
possible_keys = (''.join(x) for x in itertools.permutations(lower_alpha_characters, 5))

def crack(target, payload):
    for key in possible_keys:
        print(key)

def forge(payload, key):
    signer = hmac.new(key, payload, hashlib.sha1)
    print(payload + "--" + signer.hexdigest())
