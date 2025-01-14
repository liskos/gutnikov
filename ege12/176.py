s = 200 * "5"
while "555" in s or "333" in s:
    if "555" in s: s = s.replace("555", "3", 1)
    else:
        s = s.replace("333", "5", 1)
print(sum(int (x) for x in s))
