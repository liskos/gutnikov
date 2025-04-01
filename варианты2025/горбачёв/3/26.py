file = open("26_18338.txt")
n, k = map(int, file.readline().split())
print("кандидатов", n)
print("мест", k)
a = [list(map(int, file.readline().split())) for _ in range(n)]
print("кандидаты", a)
a.sort(key=lambda x:(x[1]+x[2]+x[3],x[4], x[0]), reverse=True)
for i in range(530):
    print(i+1, *a[i], a[i][1]+a[i][2]+ a[i][3])
print("последний зачисленный", a[k-1])
polu = a[k-1][1] + a[k-1][2] + a[k-1][3]
ans2 = [a[i] for i in range(k, n) if a[i][1] + a[i][2]+ a[i][3] == polu]
print("не зачисленные с полупроходным баллом", len(ans2))