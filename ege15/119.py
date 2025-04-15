p = range(25,51 + 1)
q = range(12, 37 + 1)
a1_best = 0
a2_best = 0
for a1 in range(1,100):
    for a2 in range(a1, 100):
        a = range(a1, a2 + 1)
        if all([not((x in p) == (x in q)) or not(x in a) for x in range(1,100)]) and a2 - a1 > a2_best - a1_best:
            a1_best = a1
            a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)

k = 10
p = range(25*k,51*k + 1)
q = range(12*k, 37*k + 1)
a1_best = 0
a2_best = 0
for a1 in range(35*k,41*k):
    for a2 in range(49*k, 54*k):
        a = range(a1, a2 + 1)
        if all([not((x in p) == (x in q)) or not(x in a) for x in range(1,100*k)]) and a2 - a1 > a2_best - a1_best:
            a1_best = a1
            a2_best = a2
print(a1_best/k, a2_best/k, (a2_best - a1_best) / k)