import itertools

mas = 0
ch = 0
for i, a in enumerate(itertools.product("АЕИКМСЧ", repeat=5), 1):
    z = "".join(a)
    if z == "МАСИК":
        mas = i
    elif z == "ЧЕЧИК":
        ch = i
print(ch - mas - 1)