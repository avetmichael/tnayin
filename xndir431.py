arr = [[1, 15, 8, 12],
       [2, 2, 1, 5],
       [1, 8, 7, 9],
       [10, 3, 4, 1]]
a = 0
n = len(arr)
for i in range(0, n):
    for j in range(n - i - 1, n):
        if (i + j) % 2 == 1:
            a = a + 1
        print(arr[i][j], end=" ")
    print()
print(a)
