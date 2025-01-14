s = 18 * "8" + 3 * "5"
while "555" in s or "888" in s:
    if "555" in s:
        s = s.replace("555", "8", 1)
    while "888" in s:
        s = s.replace("888", "5", 1)
    if "555" in s:
        s = s.replace("555", "8", 1)

print(s)
