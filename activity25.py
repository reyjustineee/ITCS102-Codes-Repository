def taga_triangle(number):
    for x in range(number, 0 , -1):
        for y in range(1, x + 1):
            print("*", end = " ")
        print()

def sum(x, y):
    return x + y

def box(size):
    for x in range(size + 1):
        for y in range(size + 1):
            if y == 0 or x == 0 or y == size or x == size:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact


# box(12)
# box(21)



# taga_triangle(9)
# taga_triangle(7)
# taga_triangle(12)
# taga_triangle(5)

# print(sum(21, 12))
# print(sum(11, 2) * 200)

