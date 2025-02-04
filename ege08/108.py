import itertools


s = set()
for a in itertools.permutations("КОМЕТА", r=6):
    b = "".join(a)
    ss = b.replace("К","1").replace("М","1").replace("Т","1").replace("А","0").replace("О","0").replace("Е","0")
    if ss == "101010" or ss == "010101":
        s.add(b)
print(len(s),s)