t = int(input())
temp = 0
while temp < t:
    n, k = map(int, input().split())
    to_print = "case #{}:".format(temp+1)
    lis = list(map(int, input().split()))

    changes1 = 0
    changes2 = 0
    prev = lis[0]
    checker = 2
    for i in range(1, n):
        if lis[i-1] != lis[i]:
            changes1 += 1

        if i > 1:
            if lis[i-2] == lis[i] and checker > 1:
                changes2 += 1
                changes1 -= 2
                checker = 0

        checker += 1

    if changes1 + 2*changes2 <= k:
        print(to_print, 0)
    else:
        if changes1 - k < 0:
            if (changes1 - k + 2*changes2)%2:
                sol = (changes1 - k + 2 * changes2) // 2 + 1
            else:
                sol = (changes1 - k + 2 * changes2) // 2
        else:
            sol = changes1 - k + changes2
        print(to_print, sol)
    temp += 1

'''
5
8 2
300 100 300 300 200 100 800 500
5 3
100 100 100 100 3
7 3
10 20 40 10 10 30 30
10 2
30 30 60 60 90 90 60 60 30 30
12 4
2 3 2 3 2 2 3 2 2 1 3 4

Case #1: 3
Case #2: 0
Case #3: 1
Case #4: 2
'''