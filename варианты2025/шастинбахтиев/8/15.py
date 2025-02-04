for a in range(1, 1000):
    if all([x % a == 0 or not (170 <= x <= 220) or not(x % 24 == 0) for x in range(1, 1000)]):
        print(a)