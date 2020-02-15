#!/bin/python3
import sys
def feeOrUpfront(n, k, x, d, p):
    charge = 0
    if d < k*n:
        return "upfront"

    for val in p:
        charge += max(k, val*x/100)
        if charge > d:
            return "upfront"
    if charge <= d:
        return "fee"
    else:
        return "upfront"



if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k, x, d = input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = list(map(int, input().strip().split(' ')))
        result = feeOrUpfront(n, k, x, d, p)
        print(result)

'''
3
3 20 10 60
100 200 300
3 20 15 120
200 250 300
1 1 10 100
1000
'''