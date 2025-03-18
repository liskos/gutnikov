def divided(n):
    a =  set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a

k = 0
for i in reversed(range(1, 650000)):
    d = divided(i)
    d2 = [x for x in d if x % 10 == 9 and x != 9]
    if d2:
        print(i, min(d2))
        k += 1
        if k == 8:
            break