test = int(input())
while test:
    test -= 1

    n, m = map(int, input().split())

    order = list(map(int, input().split()))
    check = dict()
    for i in range(1, n+1):
        check[i] = 0

    temp1 = 0
    temp2 = 0
    for i in range(m // n):

        for j in range(n):
            check[order[i * n + j]] += 1

        for val in check.values():
            if val > 1:
                temp1 = 1
                print("NO")
                break

        for j in range(1, n+1):
            check[j] = 0

        if temp1:
            temp2 = 1
            break

    if temp2 == 0:
        temp3 = 0
        for i in range(1, m % n + 1):
            check[int(order[-i])] += 1

        for val in check.values():
            if val > 1:
                temp3 = 1
                print("oho")
                break

        if temp3 == 0:
            print("YES")

"""
7
3 9
1 2 3 1 2 3 1 2 3
3 9
1 2 3 3 2 1 1 2 3
3 5
2 3 1 1 2
3 6
2 1 1 3 2 3
2 8
1 2 1 2 1 2 1 1
5 3
5 3 1
4 5
1 2 3 1 4
"""