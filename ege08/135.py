import itertools

s = set()
for a in itertools.permutations("КАБАЛА", r=6):
    b = "".join(a)
    ss = b.replace("А", "Х")
    if "ХХ" not in ss:
        s.add(b)
print(len(s),s )