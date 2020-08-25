def padpkcs7(x:bytes, y:int):
    """Pad bytes data with PKCS7.
    padpkcs7(x,y)
    x: bytes, the data you wanna pad
    y: the length you wanna pad to
    """
    extra = 0
    if not len(x) % y == 0:
        extra = y - ( len(x) % y )
    return x+bytes.fromhex("04"*extra)

if __name__ == '__main__':
    print(padpkcs7(bytes.fromhex("6162636461626364"), 7))
