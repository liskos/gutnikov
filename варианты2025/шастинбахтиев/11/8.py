import itertools


r = []
for a in itertools.permutations("0123456789abcdefg", r=6):
    b = "".join(a)
    ss = b.replace("1", "X").replace("3", "X").replace("5", "X").replace("7", "X").replace("9", "X").replace("b", "X").replace("d", "X").replace("f", "X")
    ss1 = ss.replace("0", "Y").replace("2", "Y").replace("4", "Y").replace("6", "Y").replace("8", "Y").replace("a", "Y").replace("c", "Y").replace("e", "Y").replace("g", "Y")
    if (a[0] != "0") and "XXX" not in ss1 and "YYY" not in ss1:
        r.append(a)
print(len(r))