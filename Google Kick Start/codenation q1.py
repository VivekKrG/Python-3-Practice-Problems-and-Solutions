m, n = map(int, input().split())
temp = 0
mat = []
myset = set()
while temp<m:
    mat.append(0)
    mat[temp] = list(map(int, input().split()))
    myset = myset | set(mat[temp])
    temp += 1

myset = sorted(myset)
temp = 0
while temp < m:
    out = ""
    for num in mat[temp]:
        pass