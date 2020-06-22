def mat_mul(A, B):

    for i in range(2):
        c = []
        for j in range(2):
            z = 0
            for k in range(2):
                z = A[i][k] * B[k][j] + z
            c.append(z)
        C.append(c)


    return C

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = []

res = mat_mul(A, B)
for i in res:
    print(i)