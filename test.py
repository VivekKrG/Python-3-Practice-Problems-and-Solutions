def minimizeCost(p, x, y):
    # Write your code here
    n = len(p)
    cost = []
    for city in range(n):
        cost.append([])
        for xcor in range(n):
            for ycor in range(n):
                cost[city].append((abs(xcor - x[xy]) + abs(ycor - y[xy]) * (p[city]))
    finalcost = []
    for xcord in range(n):
        finalcost.append([]);
        for ycor in range(n):
            sumcost = 0
            for i in range(n):
                sumcost += cost[i][xcord][ycor]
            finalcost[xcord].append(sumcost)
    mincost = min(min(value) for value in finalcost)
    return mincost
