arr = [[1, 15, 8, 12],
       [0, 2, 1, 5],
       [1, 0, 7, 9],
       [10, 3, 3, 1]]
a = 0
n = len(arr)
for i in range(0, n):
    for j in range(i, n):
        if arr[i][j] % 5 == 2:
            a = a + 1
        print(arr[i][j], end=" ")
    print()
print("qanak =", a)