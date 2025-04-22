def delit(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a

def prime_number(n):
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, n):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = False
    return [i for i in range(n) if a[i]]


print(prime_number(1000_000))