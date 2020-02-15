n = int(input())
temp = 0
while temp < n:
    input()
    ins1 = input()
    ins2 = input()
    if ins1.count('0')==ins2.count('0') and ins1.count('1')==ins2.count('1'):
        print('YES')
    else:
        print("NO")
    temp += 1