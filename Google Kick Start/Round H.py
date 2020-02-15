test = int(input())
for case in range(test):
    count = list(map(int, input().split()))
    remain = [x % 2 for x in count]
    #Check whether a number can be made divsible by 11.



'''
6
0 0 2 0 0 1 0 0 0
0 0 0 0 0 0 0 0 12
0 0 0 0 2 0 1 1 0
3 1 1 1 0 0 0 0 0
3 0 0 0 0 0 3 0 2
0 0 0 0 0 0 0 1 0

  
Case #1: YES
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: YES
Case #6: NO
'''