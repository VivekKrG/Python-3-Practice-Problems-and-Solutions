def not_readed(tear_page, page_factor):
    ret = 0
    for page in tear_page:
        if page % page_factor == 0:
            ret += 1

    return ret


test = int(input())
for case in range(test):
    N, M, Q = map(int, input().split())
    tear_page = list(map(int, input().split()))
    read_page = list(map(int, input().split()))

    out = 0
    for page_factor in read_page:
        out += N//page_factor
        out -= not_readed(tear_page, page_factor)
    print("Case #{}: {}".format(case+1, out))



"""
T
N M Q
Mi integers not available
Pi


3
11 1 2
8
2 3
11 11 11
1 2 3 4 5 6 7 8 9 10 11
1 2 3 4 5 6 7 8 9 10 11
1000 6 1
4 8 15 16 23 42
1



Case #1: 7
Case #2: 0
Case #3: 994
"""