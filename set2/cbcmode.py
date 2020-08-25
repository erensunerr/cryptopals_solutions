from Cryptodome.Cipher import AES
from pkcs7pad import padpkcs7
def repgen(n, A):
        c = 0
        while True:
            try:
                yield A[c*n:(c+1)*n]
            except IndexError:
                raise StopIteration
            c += 1

def CBCE(pt: bytes, iv: bytes, key: bytes):
    message = []
    if len(pt) % 16 != 0:
        raise Exception("pad it properly to 16 bytes")

    g = repgen(16, bytearray(pt))
    ptblock = next(g)
    # print(len(pt), pt)
    aes = AES.new(key, AES.MODE_ECB)
    encoded = aes.encrypt(ptblock).hex()
    q = int(encoded, 16) ^ int(iv.hex(), 16)
    message += [bytes.fromhex(format(q, 'x'))]

    for ptblockindex in range(1, len(pt) // 16):
        q = int(aes.encrypt(next(g)).hex(), 16) ^ int(message[ptblockindex - 1].hex(), 16)
        b = bytes.fromhex(format(q, 'x'))
        # print("BYTES", b, len(b))
        message += [b]

    ret = bytearray()

    for m in message:
        # print(m.hex())
        i = bytearray.fromhex(m.hex())
        ret += i
    return ret

def CBCD(ct: bytes, iv: bytes, key: bytes):
    if len(ct) % 16 != 0:
        raise Exception("pad it properly to 16 bytes")
    message = []
    g = repgen(16, ct)
    ctblock = next(g)
    aes = AES.new(key, AES.MODE_ECB)
    o = int(ctblock.hex(), 16) ^ int(iv.hex(), 16)
    # print(hex(o))
    l = '{:032x}'.format(o)
    q = bytes.fromhex(l) # A XOR B = C then C XOR B = A
    # print("BYT", q.hex(), len(q.hex())//2)
    message += [aes.decrypt(q)]
    del q
    for ctblockindex in range(1, len(ct) // 16): # starting from 1 cuz 1st block is already done
        ctblock_new = next(g)

        q = int(ctblock.hex(), 16) ^ int(ctblock_new.hex(), 16)
        z = '{:032x}'.format(q)
        # print("BYTZ"+str(ctblockindex), z, len(z)//2)
        o = bytes.fromhex(z)
        # print("BYTO"+str(ctblockindex), o.hex(), len(o.hex())//2)
        message += [aes.decrypt(o)]
        ctblock = ctblock_new

    ret = bytearray()

    for m in message:
        # print(m.hex())
        i = bytearray.fromhex(m.hex())
        ret += i
    try:
        return ret.decode('utf-8')
    except:
        return ret


pt = padpkcs7("ahmetmehmetaliahmetmehmetaliahmetmehmetaliahmetmehmetaliahmetmehmetali".encode('utf-8'), 16)
iv = "\x00\x00\x00\x00".encode('utf-8')
key = "aaaaaaaaaaaaaaaa".encode('utf-8')
ct = CBCE(pt, iv, key)
# print(ct.hex(), len(ct.hex())//2)
print(ct)
print(CBCD(ct, iv, key))
