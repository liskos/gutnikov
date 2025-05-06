def f(file_name):
    file = open(file_name)
    n, k = map(int, file.readline().split())
    print(f"Количество: {n}, Распродажа: {k}")
    a = [int(file.readline()) for _ in range(n)]
    a.sort(reverse=True)
    print(f"Цены: {a}")
    print(f"Самый дорогой неучаствующий : {a[k]}")
    return a[k], sum(a[:k]) * 0.2
print(f("21test.txt"))
print(f("26data/26-k1.txt"))