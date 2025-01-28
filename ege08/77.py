import itertools


s = set()
for a in itertools.permutations("ТАРКНИЩЕ", r=6):
    b = "".join(a)
    ss = b.replace("Т", "1").replace("Р", "1").replace("К", "1").replace("Н", "1").replace("Щ", "1").replace("А", "0").replace("И", "0").replace("Е", "0")
    if ss == "101010":
        s.add(b)
print(len(s))