x = -1
y = 1
z = 0
test = 0
while(test <60001):
    z = x+y
    print(z,end=', ')
    x = y
    y = z
    test += 1
