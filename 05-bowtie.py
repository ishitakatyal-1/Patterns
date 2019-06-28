rows = int(input("Enter the number of rows:"))
iter1 = int(input("Enter the number of iterations:"))
num = 1
while num <= iter1:
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        for k in range(rows-i-1):
            print(" ",end=" ")
        for o in range(rows-i-1):
            print(" ",end=" ")
        for q in range(i+1):
            print("*",end=" ")
        print()
    for n in range(rows, 0 , -1):
        for l in range(n):
            print("*",end=" ")
        for m in range(rows-n):
            print(" ",end=" ")
        for p in range(rows-n):
            print(" ",end=" ")
        for r in range(n):
            print("*",end=" ")
        print()
    print()
    num += 1