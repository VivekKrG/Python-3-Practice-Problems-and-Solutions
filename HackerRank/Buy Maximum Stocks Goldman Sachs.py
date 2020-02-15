# https://www.hackerrank.com/contests/gs-codesprint/challenges/buy-maximum-stocks/problem
import sys

def buyMaximumProducts(n, money, a):
    posDict = {}
    temp = 1
    for stoke_price in a:
        if stoke_price in posDict:
            posDict[stoke_price] = posDict[stoke_price]+temp
        else:
            posDict[stoke_price] = temp
        temp += 1

    a = set(a)
    a = sorted(a)
    price = 0
    totalStokes = 0
    for val in a:
        if money-val > 0:
            num = posDict[val]
            poss = money//val
            if poss > num:
                poss = num

            price += val*poss
            totalStokes += poss
            money -= val*poss

    return totalStokes


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)
'''
n - Number of days
Stokes price per piece list
Initial money
Sample Input 0
3
10 7 19
45

Sample Output 0
4
'''