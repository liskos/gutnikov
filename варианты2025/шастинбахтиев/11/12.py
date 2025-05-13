s = "1" + 110 * "8"
while "1" in s:
    if "18" in s: s = s.replace("18", "8881")
    else: s = s.replace("1", "888")
print(s.count("8") * 8)
print(sum(map(int, s)))