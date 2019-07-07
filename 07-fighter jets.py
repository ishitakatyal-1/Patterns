row1 = int(input("Enter the number of rows:"))
for i in range(1, row1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
    for j in range(i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(row1, 0, -1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
    for j in range(i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()