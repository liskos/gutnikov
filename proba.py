a, b = map(int, input().split())
if a >= 30 and b >= 30:
    print(f"Можно отрезать {a // 30 * b // 30} квадратов.")
else:
    print("Можно отрезать 0 квадратов.")
print(a // 30)
print(b // 30)
print(a // 30 * b // 30)