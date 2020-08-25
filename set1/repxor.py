
def repXor(KEY, MESSAGE):
    def yKey(): # Generator for the repeating-key functionality
            c = 0
            while True:
                c %= len(KEY)
                yield KEY[c]
                c += 1

    q = ""
    gen = yKey()
    for x in MESSAGE:
        if isinstance(x, str):
            x = ord(x)
        y = next(gen)
        z = "{:02x}".format( x ^ ord(y))#hex formatting
        # print(ord(x), x,'\t', ord(y), y, int(z, 16))
        q += z
    return q
