s = 120 * "7"
while "88777" in s or "7" in s:
    if "88777" in s:
        s = s.replace("88777", "8", 1)
    else:
        s = s.replace("7", "8", 1)
print(s)