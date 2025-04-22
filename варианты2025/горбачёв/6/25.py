import fnmatch


k = 0
for i in reversed(range(10**7)):
    if fnmatch.fnmatch(str(i), "89?45*75"):
        print(i, i // 25)
