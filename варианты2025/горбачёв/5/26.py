file = open("26.txt")
n, m, k = map(int, file.readline().split())
print(f"Занятых мест {n}. Количество рядов {m}. Количество мест в ряду {k}.")
a = [m] * (k + 1)
for _ in range(n):
    row, n_mesta = map(int, file.readline().split())
    a[n_mesta] = min(a[n_mesta], row-1)
n_mesta_best = 0
n_row_best = 0
for i in range(1, k - 2):
    c = min(a[i:i+4])
    if c >= n_row_best:
        n_row_best = c
        n_mesta_best = i + 3
print(f"Номер ряда {n_row_best}, номер места {n_mesta_best}")