def search(matrix, m, n, key):
    i, j = 0, n - 1
    while i < m and j >= 0:
        if matrix[i][j] == key:
            return i, j
        elif key > matrix[i][j]:
            i = i + 1
        elif key < matrix[i][j]:
            j = j - 1
    return -1


if __name__ == '__main__':
    t = [[0 for j in range(4)] for i in range(4)]
    k = 1
    for i in range(4):
        for j in range(4):
            t[i][j] = k
            k = k+1
    print(search(t, 4, 4, 13))
