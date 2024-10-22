import itertools


for i, s in enumerate(itertools.product("БИКНОПР", repeat=6), 1):
    if s.count("О") == 3 and len(set(s)) == 4:

        print(i, s)