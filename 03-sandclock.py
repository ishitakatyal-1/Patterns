#sandclock

row1 = int(input("Enter the number of rows: "))
for i in range(row1):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(row1-i, 1, -1):
        print("*",end=" ")
    for l in range(row1-i+1, 1, -1):
        print("*",end=" ")    
    print()  
for i in range(row1, 0, -1):
    for j in range(i):
        print(" ",end=" ")
    for k in range(row1-i+1, 0, -1):
        print("*",end=" ")
    for l in range(row1-i+1, 1, -1):
        print("*",end=" ")
    print()