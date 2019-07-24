rows1 = 4
cols1 = 5
iter1 = 2
num = 0

for i in range(rows1):
    for j in range(i+1):
        print('*',end=" ")
    print()
    
while num < iter1:
    for i in range(rows1):
        for j in range(i+1):
            print(' ',end=" ")
        for k in range(i+1):
            print('*',end=" ")
        print()
    for l in range(rows1, 0, -1):
        for m in range(l-1):
            print(' ',end=" ")
        for n in range(l):
            print('*',end=" ")
        print()
    num += 1;
    
