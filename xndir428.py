arr = [[1, 3, 8, 0],
       [0, 4, 1, 5],
       [1, 0, 8, 9],
       [10, 3, 3, 1]]
a = 0
n = len(arr)
for i in range(0, n):
    for j in range(0, n - i):
        if arr[i][j] == 0:
            a = a + 1
        print(arr[i][j], end=" ")
    print()
print("qanak =", a)