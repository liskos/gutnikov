for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                f = not (not y or (x == w)) and (not z or x)
                print(x, y, z, w, "|", int(f))