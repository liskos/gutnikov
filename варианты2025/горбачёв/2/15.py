def f(x):
    P = 32 <= x <= 55
    Q = 40 <= x <= 79
    A = a1 <= x <= a2
    return (Q <= (not A)) <= ((not A) == (not P))


Ox = [x / 4 for x in range(30 * 4, 83 * 4)]
s = []
for a1 in Ox:
    for a2 in Ox:
        if all(f(x)==1 for x in Ox):
            s.append(a2 - a1)
print(min(s))