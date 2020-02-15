test = int(input())
temp = 0
while temp < test:
    left, right = map(int, input().split())
    left -= 1

    '''
    for v in range(left, right+1):
        sol += v*(v+1)*(v+2)*(v+3)
    '''
    sol1 = ((6 * (right**5 - left**5)) + (15 * (right**4 - left**4)) + (10 * (right**3 - left**3)) - (right - left))//30
    sol1 = sol1 % (10 ** 9 + 7)

    sol2 = 6*((right**4 - left**4) + 2*(right**3 - left**3) + (right**2 - left**2))//4
    sol2 = sol2 % (10 ** 9 + 7)

    sol3 = 11*(2*(right**3 - left**3) + 3*(right**2 - left**2) + (right - left))//6
    sol3 = sol3 % (10 ** 9 + 7)

    sol4 = (3*((right**2 - left**2) + right - left)) % (10 ** 9 + 7)

    sol = ( sol1+sol2+sol3+sol4 ) % (10 ** 9 + 7)
    print(sol)

    temp += 1

'''
1
2 4 

1320
'''