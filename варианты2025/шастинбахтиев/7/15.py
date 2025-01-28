for a in range(0, 10000):
    if not any(not ((x < 7) or (y >= 5 * x + a - 60) or (x >= 36) or (y < 225)) for x in range(0, 300) for y in range(0, 300)):
        print(a)