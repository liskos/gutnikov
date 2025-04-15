a1_best = 0
a2_best = 0
p = range(15, 33 + 1)
q = range(45, 68 + 1)
for a1 in range(1, 100):
    for a2 in range(a1, 100):
        a = range(a1, a2 + 1)
        if all([not((x in a) and (not(x in q))) or ((x in p) or (x in q)) for x in range(1, 100)]) and a2 - a1 > a2_best - a1_best:
            a1_best = a1
            a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)

k = 10
a1_best = 0
a2_best = 0
p = range(15*k, 33*k + 1)
q = range(45*k, 68*k + 1)
for a1 in range(40*k, 50*k):
    for a2 in range(65*k, 70*k):
        a = range(a1, a2 + 1)
        if all([not((x in a) and (not(x in q))) or ((x in p) or (x in q)) for x in range(1, 100*k)]) and a2 - a1 > a2_best - a1_best:
            a1_best = a1
            a2_best = a2
print(a1_best/k, a2_best/k, (a2_best - a1_best) / k)