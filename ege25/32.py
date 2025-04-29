
def delit(n):
    a = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)

for i in range(394441, 394505 + 1):
    m = 0
    if len(delit(i)) > m:
        m = len(delit(i))
        if m == 48:
            print(m, i, delit(i))