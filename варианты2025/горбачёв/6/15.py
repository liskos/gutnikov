a1best = 0
a2best = 200
p = range(3, 83 + 1)
q = range(62, 131 + 1)
for a1 in range(1, 200):
    for a2 in range(a1, 200):
        a = range(a1, a2 + 1)
        if a2 - a1 < a2best - a1best and all([(x in q) or (not(not(x in a) and (x in p)) or (x in q)) for x in range(1, 200)]):
            a1best = a1
            a2best = a2
print(a1best, a2best, a2best - a1best)

k = 10
a1best = 0
a2best = 200 * k
p = range(3 * k, 83 * k + 1)
q = range(62 * k, 131 * k + 1)
for a1 in range(1 * k, 6 * k):
    for a2 in range(59* k, 65 * k):
        a = range(a1, a2 + 1)
        if a2 - a1 < a2best - a1best and all([(x in q) or (not(not(x in a) and (x in p)) or (x in q)) for x in range(1, 200*k)]):
            a1best = a1
            a2best = a2
print(a1best / k, a2best / k, (a2best - a1best) / k)