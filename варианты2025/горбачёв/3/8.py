import itertools


k = 0
for i in itertools.product("0123456789ABCDEF", repeat=5):
    b = "".join(i)
    ss = b.replace("1", "X").replace("3", "X").replace("5", "X").replace("7", "X").replace("9", "X").replace("B", "X").replace("D", "X").replace("F", "X")
    if ss[0] != "X" and ss[-1] == "X" and i[0] != "0" and b[0] != b[1] and b[1] != b[2] and b[2] != b[3] and b[3] != b[4]:
        k += 1
print(k)
