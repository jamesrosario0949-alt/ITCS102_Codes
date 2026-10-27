i = int(input("Enter a number: "))
num = 1

for x in range(i):
    for y in range(x + 1):
        print(num, end=" ")
        num += 1
    print()