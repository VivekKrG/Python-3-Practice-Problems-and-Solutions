test = int(input())

for _ in range(test):
    maxOut = 0
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h < c:
        (h, c) = (c, h)
        (p, f) = (f, p)
    if h == c:
        p = p+f
        if b < 2*p:
            maxOut = (b//2)*h
        else:
            maxOut = p*h
    else:
        if b < 2*p:
            maxOut = (b//2)*h
        else:
            maxOut = p*h
            b -= 2*p
            if b < 2*f:
                maxOut += (b//2)*c
            else:
                maxOut += c*f

    print(maxOut)