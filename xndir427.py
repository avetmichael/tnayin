arr = [[1, 3, 8, 7],
       [20, 4, 1, 5],
       [1, 15, 8, 9],
       [10, 3, 3, 1]]
a = 1
k = 2
n = len(arr)
for i in range(0, n):
    for j in range(0, n - i):
        if arr[i][j] % k == 0:
            a = a * arr[i][j]
        print(arr[i][j], end=" ")
    print()
print(a)