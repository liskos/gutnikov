a = [int(x) for x in open("17data/17-204.txt")]
r = []
tr = [i for i in range(len(a) - 2) if (abs(a[i - 1]) % 10 != 9 or a[i - 1] < 0) and (a[i] > 0 and a[i] % 10 == 9) and (a[i + 1] < 0 or a[i + 1] % 10 != 9)]
print(len(tr), max([sum(a[i-1:i+2]) for i in tr]))
      