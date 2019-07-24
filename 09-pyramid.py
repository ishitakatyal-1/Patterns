row1 = int(input("Enter the number of rows: "))

#pyramid
for i in range(0, row1):
    for j in range(row1-i-1, 0, -1):  #here row1-i-1 depends on the output desired.
        print(" ",end=" ")        
    for k in range(i-1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()