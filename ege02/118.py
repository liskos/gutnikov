for a in 1, 0:
    for b in 1, 0:
        for c in 1, 0:
            f = (a and not c) or (not b and not c)
            print(a, b, c, "|", int(f))