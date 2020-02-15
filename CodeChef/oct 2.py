test = int(input())

temp = 0
while temp < test:

    n, p = map(int, input().split(' '))

    lis = list(map(int, input().split(' ')))
    # lis.sort()
    lis = sorted(lis)
    c = 0
    while p > 0:
        pi = lis[c]
        p = p - pi
        if p >= 0:
            c += 1
    print(c)

    temp += 1
'''
1
4 7
6 2 1 3

3

2
4 7
6 2 1 3
5 6
1 2 2 4 1
'''