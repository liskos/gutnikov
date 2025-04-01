import time
t1 = time.time()
s = open("24_18537.txt").read()

m = 0
k_a = 0
t = ""
for i in s:
    if i == "F":
        t = ""
        k_a = 0
    else:
        t += i
        if i == "A":
            k_a += 1
        while k_a > 22:
            if t[0] == "A":
                k_a -= 1
            t = t[1:]
        if k_a == 22:
            m = max(m, len(t))
print(m)
print(time.time() - t1)