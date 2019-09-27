arr = [[1, 3, 8, 7],
       [20, 4, 1, 5],
       [1, 15, 8, 9],
       [10, 3, 2, 1]]
t = 0
k = 5
n = len(arr)
for i in range(1, n):
    for j in range(0, i):
        print(arr[i][j], end=" ")
        if arr[i][j] % 5 == 0:
            t = t + 1
    print()
print("qanak =", t)

