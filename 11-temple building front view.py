rows1=6
print("           *")
print("           |")
for i in range(rows1):
    for j in range(rows1-i, 1, -1):
        print(" ",end=" ")
    #print()
    for k in range(i+1):
        print("/",end=" ")
    #print()
    for l in range(i+1):
        print('\\',end=" ")
    print()
for i in range(rows1):
    for j in range(rows1-i+1, 1, -1):
        print("|",end=" ")
    for l in range(i):
        print(" ",end=" ")
    for m in range(i):
        print(" ",end=" ")
    for n in range(rows1-i):
        print("|",end=" ")
    print()
    