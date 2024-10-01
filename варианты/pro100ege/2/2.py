for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                f = (x and not y) or (x == z) or w
                print(x, y, z, w, '|', int(f))