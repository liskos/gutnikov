for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                f = w and(y == (not z or (x or y)))
                print(x, y, z, w, "|", int(f))