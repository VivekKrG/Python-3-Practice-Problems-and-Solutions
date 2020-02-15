test = int(input())
while test:
    test -= 1
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(q):
        r, s = map(int, input().split())
        (r, s) = (min(r,s), max(r,s))
        sm = 0
        if (r-s-1) % 2:
            print("UNKNOWN")
        else:
            if r == s+1 or s == r+1:
                sm = arr[r-1]
            else:
                bit = 0
                for j in range(r-1, s-1):
                    if bit == 0:
                        sm += arr[j]
                        bit = 1
                    else:
                        sm -= arr[j]
                        bit = 0
            print(sm)



'''
1
5 3
4 5 6 7
1 2
1 3
4 1

4
UNKNOWN
5
'''