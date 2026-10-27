
j = int(input("Enter a number: "))
for x in range(j):  
    for y in range(j):  
      if x + y == j-1 or x == y:
         print("*", end=" ")
      else:
         print(" ", end=" ")
    print()

