
def score(a):
    a = a.lower()
    lang = {'e': 12,
            't': 11,
            'a': 10,
            'o': 9,
            'i': 8,
            'n': 7,
            's': 6,
            'h': 5,
            'r':4,
            'd':3,
            'l':2,
            'u':1
            }
    score = 0
    for c in a:
        if c in lang.keys():
            score += lang[c] + 5
        if (ord(c) < 97 or ord(c) > 123) and not (ord(c) == 32):
            score -= 2
        # print("----|", c, score)
    # print('--END SCORE--: ', score)
    return score

class ScoredData:
    def __init__(self, points, data):
        self.score = points
        self.data = data

    def __repr__(self):
        return "{0}: {1}\n".format(self.score, self.data)



def solve_one_char_xor(C, n):

    # def xor() TODO: write it proper


    byscore = []
    for char in range(0, 127):
        tr = str("{0:0{1}x}".format(char, 2))*(len(C)//2)
        ty = str("{0:0{1}x}".format(int(C, 16) ^ int(tr, 16), len(C)))
        st = bytearray.fromhex(ty).decode()
        sct = ScoredData(score(st), [st, char])
        # print(sct)
        byscore.append(sct)

    return sorted(byscore, key=lambda s: s.score, reverse=True)[:n]
