import itertools


def dw(n):
    t = "0123456789ab"
    s = ""
    while n > 0:
        s = t[n % 12] + s
        n //= 12
    return s


def f(x):
    s1 = x[0] + x[2]
    s2 = x[1] + x[3]
    if s1 > s2:
        return dw(s1) + dw(s2)
    else:
        return dw(s2) + dw(s1)


print(f([4, 4, 1, 11]))
for x in itertools.product([1, 2, 4, 5, 6, 11], repeat=4):
    if f(x) == '115':
        print(x)