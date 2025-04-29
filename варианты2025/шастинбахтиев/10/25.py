import fnmatch


k = 0
for i in range(4321, 10**9, 4321):
    p = 1
    for x in str(i):
        p = p * int(x)
    if fnmatch.fnmatch(str(i), "34*56?7") and p % 10 == 0:
        print(i, p)