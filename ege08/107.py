import itertools


s = set()
for a in itertools.permutations("КОЛУН", r=5):
    b = "".join(a)
    ss = b.replace("К","1").replace("Л","1").replace("Н","1").replace("О","0").replace("У","0")
    if "11" not in ss and "00" not in ss:
        s.add(b)
print(len(s))
import itertools


s = set()
for a in itertools.permutations("КОЛУН", r=5):
    b = "".join(a)
    ss = b.replace("К","1").replace("Л","1").replace("Н","1").replace("О","0").replace("У","0")
    if ss == "10101" or ss == "01010":
        s.add(b)
print(len(s),s)