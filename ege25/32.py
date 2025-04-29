
def delit(n):
    a = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a, reverse=True)

m = [0, 0, [0, 0]]
for i in range(394441, 394505 + 1):
    if len(delit(i)) > m[1]:
        m = [i, len(delit(i)), delit(i)[:2]]
print(m[0], *m[2])