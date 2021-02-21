import base64
import hashlib
from Crypto import Random #pip install pycrypto
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]

def iv():
    return chr(0) * 16

class AESCipher(object):

    def __init__(self, key):
        self.key = key
        #self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


key = 'abcdefghijklmnopqrstuvwxyz123456'

_enc = 'gOXlygE+qxS+69zN5qC6eKJvMiEoDQtdoJb3zjT8f/E='
message = 'Test English...'
answer = 'rvs4H8x4Q8sblGG1jkOHFQ=='

enc = AESCipher(key).encrypt(message)
dec = AESCipher(key).decrypt(_enc)

print(_enc == enc)
print(message == dec)