arr = [[1, 3, 8, 7],
       [20, 4, 1, 5],
       [1, 15, 8, 9],
       [10, 3, 3, 1]]
gumar = 0
n = len(arr)
for i in range(0, n -1):
    for j in range(0, n - 1 - i):
        print(arr[i][j], end=" ")
        if arr[i][j] % 2 == 0:
            gumar = gumar + arr[i][j]
    print()
print("gumar =", gumar)