s = ">" + 10 * "7" + 10 * "5" + 10 * "3"

while ">3" in s or ">5" in s or ">7" in s:
    s = s.replace(">3", "55>", 1)
    s = s.replace(">5", "5>3", 1)
    s = s.replace(">7", "3>5", 1)

print(sum(int(x) for x in s[:-1]))