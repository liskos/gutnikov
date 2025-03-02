for u in 0, 1:
    for w in 0, 1:
        for x in 0, 1:
            for y in 0, 1:
                f = not (not x or w) or (not u or y)
                print(u,w,x,y,"|",int(f))