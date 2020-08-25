import codecs
def fxor(a, b):
    if len(a) != len(b):
        raise Exception("fxor: Lengths of A and B must be equal.")
    a_bin = int(a, 16)
    b_bin = int(b, 16)
    x = a_bin ^ b_bin
    return str(hex(x))[2:]

print(fxor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965') == '746865206b696420646f6e277420706c6179')
