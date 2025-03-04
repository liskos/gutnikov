for x in range(2, 11):
    a = 432
    s = []
    while a > 0:
        s = [a % x] + s
        a //= x
    print(x, s)
print(6+8+9+10)