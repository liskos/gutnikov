for a in range(10**10):
    if all((5 < y) or (x > 32) or (x + 2 * y < a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break