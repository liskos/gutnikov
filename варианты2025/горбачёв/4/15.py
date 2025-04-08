p = range(17, 61 + 1)
q = range(39, 91 + 1)
a1_best = 0
a2_best = 100
for a1 in range(0, 100):
    for a2 in range(a1, 100):
        a = range(a1, a2 + 1)
        if all([(((x in q) and not(x in a)) and ((x in a) or (x not in p))) == False for x in range(0, 100)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)
k = 10
p = range(17 * k, 61 * k + 1)
q = range(39 * k, 91 * k + 1)
a1_best = 0 * k
a2_best = 100 * k
for a1 in range(59* k, 65 * k):
    for a2 in range(89 * k, 95 * k):
        a = range(a1, a2 + 1)
        if all([(((x in q) and not(x in a)) and ((x in a) or (x not in p))) == False for x in range(0, 100 * k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best - a1_best) / k)