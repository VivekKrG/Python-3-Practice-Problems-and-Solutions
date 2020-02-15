def solution(S):
    # write your code in Python 3.6
    curmax = 0
    prevmax = 0
    abcount = 0
    prevchar = 'c'
    for c in S:
        if c == prevchar:
            if abcount == 2:
                if curmax > prevmax:
                    prevmax = curmax
                abcount = 2
                curmax = 2
            else:
                abcount += 1
                curmax += 1
        else:
            abcount = 1
            curmax += 1
            prevchar = c
        #print(prevchar, abcount, curmax,prevmax)
    return max(prevmax, curmax)

S= 'aaaaaa'
print(solution(S))
