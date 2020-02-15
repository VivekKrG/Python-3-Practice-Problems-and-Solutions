n, m = map(int, input().split())
for row in range(n):
    #map(int, input().split())
    mat = []
    for i in range(n):
        given = input()
        for k in range(m):
            mat.append([0 for j in range(m)])
            if given[i] == '1':
                mat[i][k] += 1