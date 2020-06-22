def mat_add(A, B):

    for i in range(2):
        c = []
        for j in range(2):
            c.append(A[i][j] + B[i][j])
        C.append(c)

    return C

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = []

res = mat_add(A, B)
for i in res:
    print(i)