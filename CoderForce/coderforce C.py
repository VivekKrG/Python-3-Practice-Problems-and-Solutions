tests = int(input())
for __ in range(tests):
    string = input()
    count = 0
    out = ''
    index = 0
    while index+2 < len(string):
        if string[index] == 'o': #one or two
            if string[index+1:index+3] == 'ne':
                out += " "+str(index+1)
                count += 1
                index += 3
            else:
                index += 1
        elif string[index] == 't':
            if index+4 < len(string) and string[index + 1:index + 5] == 'wone':
                out += " " + str(index+2+1)
                count += 1
                index += 5
            elif string[index + 1:index + 3] == 'wo':
                out += " " + str(index+1)
                count += 1
                index += 3
            else:
                index += 1
        else:
            index += 1
        #print(out)
    print(count)
    print(out[1:])
'''
4
onetwone
testme
oneoneone
twotwo


2
6 3
0

3
4 1 7 
2
1 4


10
onetwonetwooneooonetwooo
two
one
twooooo
ttttwo
ttwwoo
ooone
onnne
oneeeee
oneeeeeeetwooooo


6
18 11 12 1 6 21 
1
1 
1
3 
1
2 
1
6 
0

1
4 
0

1
1 
2
1 11 

'''