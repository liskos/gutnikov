a1best = 0
a2best = 0
p = range(3, 83 + 1)
q = range(62, 131 + 1)
for a1 in range(1, 200):
    for a2 in range(a1, 200):
        a = range(a1, a2 + 1)
        if a2 - a1 > a2best - a1best and all([(x in q) or ((not(x in a)) and (not(x in p)) or (x in q)) for x in range(1, 200)]):
            a1best = a1
            a2best = a2
print(a1best, a2best, a2best - a1best)