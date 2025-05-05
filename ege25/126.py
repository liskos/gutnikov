def delit(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(152346, 957812 + 1):
    if len(delit(i)) == 3:
        print(max(delit(i)))