n = int(input())
temp = 0
while temp < n:
    ins = input()
    out = 0
    if len(ins) >= 2:
        test = 1
        while (test + test ** 2) <= len(ins):
            t = test + test ** 2
            for i in range(t, len(ins)+1):
                if ins[i - t: i].count('0') == ins[i - t: i].count('1') ** 2:
                    out += 1
            test += 1

    print(out)
    temp += 1
    '''
2
010001
101
    
    '''