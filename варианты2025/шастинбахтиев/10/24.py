s = open("24.txt").read()
a = [i for i in range(len(s) - 4) if s[i] == s[i + 2] == s[i + 4] and s[i + 1] == s[i + 3]]
k = 170 #170
m = 10**10
for i in range(len(a) - (k-1)):
    m = min(m,a[i + (k - 1)] - a[i] + 5)
print(m)

