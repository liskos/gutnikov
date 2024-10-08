for a in 1, 0:
    for b in 1, 0:
        for c in 1, 0:
            for d in 1, 0:
                f = ((not a or b) == c) or d
                if not f:
                    print(a, b, c, d, "|", int(f))
