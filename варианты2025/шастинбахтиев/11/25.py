def prime_numbers():
    a = [True] * 750_000
    a[0] = a[1] = False
    for i in range(750_000):
        if a[i]:
            for j in range(i ** 2, 750_000, i):
                a[j] = False
    return [i for i in range(750_000) if a[i] and i % 10 == 7]

def f(n):
    global p
    r = [x for x in p if n % x == 0]
    if r:
        return sum(r)//len(r)
    else:
        return 0

k = 0
p = prime_numbers()
for x in reversed(range(1, 750_000)):
    r = f(x)
    if r != 0 and r % 111 == 0:
        print(x, r)
        k += 1
        if k == 5:
            break