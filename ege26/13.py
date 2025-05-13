def f(file_name):
    file = open(file_name)
    s, n = map(int, file.readline().split())
    print(f"Объём диска:{s}, пользователей:{n}")
    a = [int(file.readline()) for _ in range(n)]
    a.sort()
    print(f"Файлы:{a}")
    v = []
    for x in a:
        if sum(v) + x <= s:
            v.append(x)
    print(f"Выбранные файлы:{v}")
    sv = s - sum(v) + v[-1]
    m = max([x for x in a if x <= sv])
    return len(v), m

print(*f("26test.txt"))
print(*f("26data/26-13.txt"))