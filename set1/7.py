from Cryptodome.Cipher import AES
import base64
key = "YELLOW SUBMARINE".encode('utf-8')
aes = AES.new(key, AES.MODE_ECB)
et = open('7.txt', 'r').read()
print(et)
dt = aes.decrypt(base64.b64decode(et))
print(dt)
