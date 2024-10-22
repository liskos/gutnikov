def sh(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s + s[-1]


def f(n):
    b = sh(n)
    b = bin(int(b))[2:]
    b = b + b[-1]
    return int(b, 2)

def d(n):
    b = int(sh(n))
    b = bin(b)[2:]
    return b
print(bin(211)[2:])