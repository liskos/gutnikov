def m(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return i + n // i
    return 0
k = 0
for x in range(159870, 900000):
    s = str(m(x))
    if s[0]=="7" and s[-1] == "7":
        print(x, s)
