# cook your dish here
test = int(input())
while test:
    test -= 1

    run = int(input())

    aa = 0
    bb = 0
    for tst in range(run):
        one2, a, b = map(int, input().split())
        if tst == 0:
            if one2 == 2:
                print("NO")
            else:
                print("YES")

            aa = a
            bb = b

        else:
            if one2 == 1:
                print("YES")
            else:
                if a == b:
                    print("YES")
                elif min(a, b) < max(aa, bb):
                    print("YES")
                else:
                    print("NO")
        aa = a
        bb = b

'''
1
6
2 0 1
1 3 1
2 2 4
2 5 6
2 8 8
2 9 10
Example Output
NO
YES
YES
NO
YES
NO

'''