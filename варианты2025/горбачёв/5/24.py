s = open("24.txt").read()
import re

num  = r"(([1-9][0-9]*)|0)"
vir = rf"{num}([+*]{num})+"
r = [x.group() for x in re.finditer(vir, s)]
r2 = sorted([x for x in r], key=len, reverse=True)
for x in r2:
    if eval(x) == 100:
        print(len(x), eval(x), x)