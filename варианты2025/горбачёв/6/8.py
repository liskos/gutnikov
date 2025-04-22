import itertools


a = []
for i in itertools.permutations(range(13), r=5):
    s = [x%2 for x in i]
    if (i[0] != 0) and ((s == [1,0,1,0,1]) or (s == [0, 1, 0, 1, 0])):
        a.append(i)
print(len(a))