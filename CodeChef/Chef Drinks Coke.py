test = int(input())
temp = 0
while temp < test:
    temp += 1
    n, m, k, l, r = map(int, input().split())
    given = []

    lowcost = 10 ** 6 + 1
    for j in range(n):
        try:
            given.append(list(map(int, input().split())))
            if given[j][0] < k:
                if (given[j][0] + m) <= k:
                    if (given[j][0] + m) <= r and (given[j][0] + m) >= l:
                        if lowcost > given[j][1] + m:
                            lowcost = given[j][1]
                else:
                    if k <= r and k >= l:
                        if lowcost > given[j][1]:
                            lowcost = given[j][1]
            else:
                if (given[j][0] - m) >= k:
                    if (given[j][0] - m) <= r and (given[j][0] - m) >= l:
                        if lowcost > (given[j][1] - m):
                            lowcost = given[j][1]
                else:  # now temp will come at k
                    if k <= r and k >= l:
                        if lowcost > given[j][1]:
                            lowcost = given[j][1]

        except:
            pass

    if lowcost == 10 ** 6 + 1:
        print(-1)
    else:
        print(lowcost)