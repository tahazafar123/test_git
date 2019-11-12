
from hashlib import blake2s
from base64 import b64decode, b64encode


orig_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
print(orig_key)
enc_key = blake2s(key=orig_key, person=b'kEncrypt').digest()
mac_key = blake2s(key=orig_key, person=b'kMAC').digest()
print(b64encode(enc_key).decode('utf-8'))
print(b64encode(mac_key).decode('utf-8'))

hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)