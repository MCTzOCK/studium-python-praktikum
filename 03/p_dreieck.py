def loop(n):
    res = []
    for i in range(1, n + 2):
        row = [1]
        for j in range(1, i):
            row.append(row[j - 1] * (i - j) // j)
        res.append(row)
    return res


print(loop(0))