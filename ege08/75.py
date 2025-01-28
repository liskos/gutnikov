import itertools


s = set()
for a in itertools.permutations("КОРАБЛИ", r=6):
    b = "".join(a)
    ss = b.replace("К", "1").replace("Р", "1").replace("Б", "1").replace("Л", "1").replace("О", "0").replace("А", "0").replace("И", "0")
    if ss == "101010":
        s.add(b)
print(len(s))