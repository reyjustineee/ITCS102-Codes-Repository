for x in range(8):
    if x < 4:
        d = 3 - x
    else:
        d = x - 3
    for y in range(8):
        if y >= d and y <= 6 - d and (y - d) % 2 == 0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

#n = int(input("Enter a numner: "))
#for x in range(n):
   # d - abs(x - n // 2)
  #  for y in range(n):
   #     if y >= d and y <= n - 1 - d and (y - d) % 2 == 0:
    #        print("*", end = " ")
    #    else:
   #         print(" ", end = " ")
 #   print()