import itertools


s = set()
for a in itertools.permutations("ВЕНТИЛЬ", r=7):
    b = "".join(a)
    ss = b.replace("Е","0").replace("И","0")
    if "0Ь0" not in ss and a[-1] != "Ь":
        s.add(b)
print(len(s))