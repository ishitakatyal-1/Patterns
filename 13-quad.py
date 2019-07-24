rows1 = 5
for j in range(rows1+1):
    for i in range(rows1-j+3, 0 ,-1):
        print(" ",end=" ")
    for k in range(1):
        print("0", end=" ")
    for m in range(j):
        print(" ", end=" ")
    for x in range(j):
        print(" ", end=" ")
    for l in range(1):
        print("0", end=" ")
    print()
for m in range(rows1):
    for i in range(m, 0, -1):
        print(" ", end=" ")
    for k in range(1):
        print("0", end=" ")
    for n in range(rows1-m-1):
        print(" ", end=" ")
    for x in range(rows1-m-1):
        print(" ", end=" ")
    for l in range(1):
        print("0", end=" ")
    print()
"""
for j in range(rows1+1):
    for i in range(rows1-j, 0 ,-1):
        print(" ",end=" ")
    for k in range(1):
        print("0", end=" ")
    for m in range(j):
        print(" ", end=" ")
    for x in range(j):
        print(" ", end=" ")
    for l in range(1):
        print("0", end=" ")
    print()
for m in range(rows1):
    for i in range(m+1, 0, -1):
        print(" ", end=" ")
    for k in range(1):
        print("0", end=" ")
    for n in range(rows1-m-1):
        print(" ", end=" ")
    for x in range(rows1-m-1):
        print(" ", end=" ")
    for l in range(1):
        print("0", end=" ")
    print()
"""
"""
for j in range(rows1):
    for i in range(rows1-j, 0 ,-1):
        print(" ",end=" ")
    for k in range(j+1):
        print(k, end=" ")
    for l in range(j):
        print(-l+j-1, end=" ")
    print()
for m in range(rows1):
    for i in range(m+1, 0, -1):
        print(" ", end=" ")
    for k in range(rows1-m):
        print(k, end=" ")
    for l in range(rows1-m, 1, -1):
        print(l-2, end=" ")
    print()
"""