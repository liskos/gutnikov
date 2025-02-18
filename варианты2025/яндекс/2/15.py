for a in range(1, 10000):
    if all([((3 * x + y) > a) and (y < x) and (x < 30) for x in range(-10000, 0) for y in range(-10000, 0)]):
        print(a)
        break
