s = ">" + 17 * "0" + 1 * "3" + 17 * "2"
while ">3" in s or ">2" in s or ">0" in s:
    if ">0" in s: s.replace(">0", "3>", 1)
    if ">3" in s: s.replace(">3", "22>", 1)
    if ">2" in s: s.replace(">2", "2>", 1)

print(sum(int(c) for c in s[-1]))