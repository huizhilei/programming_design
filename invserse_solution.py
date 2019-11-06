def exgcd(a, b, x, y):
    if b == 0:
        y[0] = 0
        x[0] = 1
        return a
    ret = exgcd(b, a % b, y, x)
    m = x[0]
    n = y[0]
    n -= int(a/b)*m
    y[0] = n
    return ret


def getInv(a, mod):
    x = [0]
    y = [0]
    d = exgcd(a, mod, x, y)
    if d == 1:
        d = (int(x[0]) % mod+mod) % mod
    else:
        d = -1
    return d
