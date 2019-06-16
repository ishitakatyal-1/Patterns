"""
It's a code written to print diamonds multiple times.
"""
row1 = int(input("Enter the number of rows: "))
iter1 = int(input("Enter the number of iterations: "))
a = 0
#diamond
while a < iter1:
    for i in range(row1, 0, -1):
        for j in range(i):
            print(" ",end=" ")
        for k in range(row1-i+1, 1, -1):
            print("*",end=" ")
        for l in range(row1-i, 1, -1):
            print("*",end=" ")
        print()  
    for i in range(2, row1):
        for j in range(i):
            print(" ",end=" ")
        for k in range(row1-i+1, 1, -1):
            print("*",end=" ")
        for l in range(row1-i, 1, -1):
            print("*",end=" ")    
        print()
    a = a + 1   
#for horizontal printing, it has to be written code-wise. iterations won't work.