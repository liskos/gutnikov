for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                f = not (not x or not(not z or w)) and (not not z or (not w == y))
                print(x, y, z, w, "|", int(f))