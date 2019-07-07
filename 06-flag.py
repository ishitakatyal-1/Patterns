
rows = 8
cols = 2
for i in range(rows//2):
    for j in range(cols):
        print("*",end=" ")
    for l in range(i, rows//2, 1):
        print("*",end=" ")
    print()
for k in range(rows//2, rows+1, 1):
    for l in range(cols):
        print("*",end=" ")
    print()