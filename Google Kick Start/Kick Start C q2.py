t = int(input())
case =1
while case <= t:
    rcv = input()
    rcv = rcv.split()
    r = int(rcv[0])
    c = int(rcv[1])
    k = int(rcv[2])

    v = []
    for i in range(r):
        val = input().split()
        for j in range(c):
            v[i] = v.append(int(val[j]))

    for i in range(1, r):
        for j in range(c):
            if  v[i][j] - v[i][j-1] <= k and v[i][j] - v[i][j-1] >= -k:
                print(v[i])
