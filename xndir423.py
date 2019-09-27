import math
arr = [[1, 3, 8, 7],
       [20, 4, 1, 5],
       [1, 15, 8, 9],
       [10, 3, 3, 1]]
a = 0
b = 0
n = len(arr)
for i in range(0, n):
    for j in range(0, i + 1):
        print(arr[i][j], end=" ")
        if arr[i][j] % 2 == 0:
            b = b + arr[i][j]**2
            a = math.sqrt(b)
    print()
print(a)


