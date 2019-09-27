arr = [[1, 15, 8, 12],
       [2, 2, 1, 5],
       [1, 8, 7, 9],
       [10, 3, 4, 1]]
a = 0
b = 0
n = len(arr)
for i in range(0, n):
    for j in range(0, i + 1):
        if arr[i][j] % 2 == 0:
            a = a + 1
            b = b + arr[i][j]
            k = b / a
        print(arr[i][j], end=" ")
    print()
print(a, k)