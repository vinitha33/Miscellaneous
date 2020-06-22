def matmul(x, y):


    res = [[0, 0, 0],
            [0, 0, 0],
           [0, 0, 0]]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                res[i][j] += x[i][k] * y[k][j]
    return res

x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

a = matmul(x, y)
for i in a:
    print(i)
