import itertools


a = []
for i in itertools.permutations("0123456789abc", r=5):
    b = "".join(i)
    xx = b.replace("2", "X").replace("4", "X").replace("6", "X").replace("8", "X").replace("a", "X").replace("c", "X")
    xx1 = xx.replace("1", "Y").replace("3", "Y").replace("5", "Y").replace("7", "Y").replace("9", "Y").replace("b", "Y")
    if b[0] != "0" and "XX" not in xx and "YY" not in xx1:
        a.append(i)
print(len(a))