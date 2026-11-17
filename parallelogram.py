n = 5
for x in range(n):
    for y in range(n):
        print(" ", end = " ")
        if x + y == n - 1 or y == n - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

for x in range(n):
    for y in range(n):
            print(" ", end = " ")
            if x + y == n - 1 or y == 0:
                 print("*", end = " ")
            else:
                 print(" ", end = " ")
    print()