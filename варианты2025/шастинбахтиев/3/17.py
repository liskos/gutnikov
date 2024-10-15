# import sys
# sys.stdin=open("17.txt")
# a =  [int(input()) for i in range(1112)]

a =  [int(i) for i in open("17.txt")]
m = min([x for x in a if x > 0 and x % 10 == 4])
r = []
for i in range(0, len(a) - 2):
    t = a[i:i + 3]
    if sum(int(x) for x in str(abs(t[0]))) + sum(int(x) for x in str(abs(t[1]))) + sum(int(x) for x in str(abs(t[2]))) == m:
        r.append(sum(t))
print(len(r), max(r))