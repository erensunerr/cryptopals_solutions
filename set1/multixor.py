import base64, binascii
from one_char import solve_one_char_xor, score
from repxor import repXor
import codecs
ct = base64.b64decode(open('6.txt', 'r').read())
# print(ct)

def repgen(n, A):
        c = 0
        while True:
            try:
                yield A[c*n:(c+1)*n]
            except IndexError:
                raise StopIteration
            c += 1

def HamDist(a, b):
    # print(a, b)
    a_hex, b_hex = a, b
    if not isinstance(a, bytes):
        a_hex = a.encode('utf-8')
    if not isinstance(b, bytes):
        b_hex = b.encode('utf-8')
    if a_hex.hex() == '' or b_hex.hex() == '':
        return 0
    a_hex, b_hex = int(a_hex.hex(), 16), int(b_hex.hex(), 16)
    st = bin(a_hex ^ b_hex)
    x = sum([int(i) for i in st[2:]])
    return x

def main():
    scoredKeysizeList = []
    HamDist("hello", 'byeee')
    for keysize in range(2, 40):
        h1 = HamDist(ct[0: keysize], ct[keysize:2*keysize])
        h2 = HamDist(ct[2*keysize: 3*keysize], ct[3*keysize:4*keysize])
        keyscore = (h1 + h2) / (2*keysize)
        scoredKeysizeList += [(keyscore, keysize)]


    top5 = sorted(scoredKeysizeList, key=lambda x: x[0])[:10]
    print(top5)
    # print(top5) #TOP5 key sizes
    #TOP 5:
    tr = {}
    keys = {}
    topN = 4 # number of keys to generate per keysize
    for i in [i[1] for i in top5]:
        tr[i] = [str() for q in range(i)]
        keys[i] = [str() for q in range(topN)]
        g = repgen(i, ct)
        print("KEYSIZE ",i)

        for j in g:
            # print(j)
            for x in range(len(j)): # bucketing
                tr[i][x] += '{:02x}'.format(j[x])
            if len(j) < i:
                break

        for l in range(i):
            block = tr[i][l]
            d = solve_one_char_xor(block, topN)
            # print([a.score for a in d])
            for n in range(topN):
                keys[i][n] += chr(d[n].key)
                # print(i, n, keys[i][n])


        # input("FINISHED ONE OF TOP 5, press enter to c")

    print(keys)
    for keysize in keys.keys():
        for i in range(len(keys[keysize])):
            rx = repXor(keys[keysize][i], ct)
            rx = codecs.decode(rx, 'hex').decode('utf-8')
            print(keysize, i, score(rx), '\n---\n', rx, '\n\n--------===========++++=======--------\n\n')
