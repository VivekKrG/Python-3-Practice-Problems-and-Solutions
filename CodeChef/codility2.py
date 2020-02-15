def solution(S):
    dics = dict()
    for c in S:
        if c in dics.keys():
            dics[c] += 1
        else:
            dics[c] = 1
    #print(dics)
    num = sorted(dics.values())
    print(num)
    sol = 0
    prev = num[0]
    n = len(num)
    n = max(n, max(num))
    summ = n*(n+1)//2
    return sum(num) - summ



S= 'aaaabbbb'
solution(S)