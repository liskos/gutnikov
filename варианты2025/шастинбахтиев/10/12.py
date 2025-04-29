s = 222 * "4"
k = 0
while "4444" in s or "222" in s:
    if "4444" in s:
        s = s.replace("4444", "2", 1)
        k += 1
    else:
        s = s.replace("222", "44", 1)
        k += 1
print(k)