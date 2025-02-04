import itertools

s = set()
for a in itertools.permutations("ВОРОТА", r=6):
    b = "".join(a)
    ss = b.replace("О", "Х").replace("А", "Х")
    if "ХХ" not in ss:
        s.add(b)
print(len(s),s )