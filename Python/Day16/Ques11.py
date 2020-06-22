A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
C = []

for i in range(len(A)):
    C1 = []
    for j in range(len(B)):
        z = 0
        for k in range(len(A)):
            z += A[i][k] * B[k][j]
        C1.append(z)
    C.append(C1)

b = len(C)
d = len(C[0])
a = 0
c = 0
cc = []
sp = []
spiral = []

while (a < b and c < d):
    for i in range(c, d):
        cc.append(C[a][i])
    a += 1
    for i in range(a, b):
        cc.append(C[i][d - 1])
    d -= 1
    if a < b:
        for i in range(d - 1, c - 1, -1):
            cc.append(C[b - 1][i])
        b -= 1
    if c < d:
        for i in range(b - 1, a - 1, -1):
            cc.append(C[i][c])
        c += 1


for i in range(len(cc)):
    sp.append(cc[i])
    if (i + 1) % len(C[0]) == 0:
        spiral.append(sp)
        sp = []

for i in range(len(spiral)):
    print(spiral[i])