import fnmatch

k = 0
for i in range(129995040, 2* 10**8,42):
    if fnmatch.fnmatch(str(i),"?2*4*0") and not fnmatch.fnmatch(str(i), "1*7*"):
        print(i, i // 42, sep="\t")
        k += 1
        if k == 5:
            break