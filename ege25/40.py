def delit_i(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(2943444, 2943529 + 1):
    if len(delit_i(i)) == 2:
        print(delit_i(i))