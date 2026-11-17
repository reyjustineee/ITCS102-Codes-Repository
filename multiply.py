n = int(input("Enter column: "))

for x in range(1, 11):
    for y in range(1, n + 1):
        print(x, "x", y, "=", x * y, end = "\t")
    print()