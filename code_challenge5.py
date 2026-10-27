size = int(input("Input your size ---> "))

for x in range(size):
    for y in range(size):
        if x + y == size - 1 or y == x:
            print("*", end = " ")
        else:
           print(" ", end = " ")
    print()
