import fnmatch


for i in range(25641,10 ** 11, 25641):
    if fnmatch.fnmatch(str(i), "4?78*82?1") and not fnmatch.fnmatch(str(i), "4?78?82?1"):
        print(i, i // 3489)