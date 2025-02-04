import itertools


s = set()
for a in itertools.permutations("АБРИКОС", r=7):
    b = "".join(a)
    ss = b.replace("Б","1").replace("Р","1").replace("К","1").replace("С","1").replace("А","0").replace("И","0").replace("О","0")
    if ss == "1010101" or ss == "0101010":
        s.add(b)
print(len(s))