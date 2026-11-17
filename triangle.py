n = 6

for x in range(1, n + 1):
    for y in range(n - x):
        print("-", end = " ")
    for z in range(1, x + 1):
        print(z, end = " ")
    for g in range(x - 1, 0, - 1):
        print(g, end = " ")
    print()