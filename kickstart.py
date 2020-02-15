T = int( input() )
print(T)
while(T):
    T = T-1
    limit = input()
    print(limit)
    rangeint = limit.split(" ")
    a = int( rangeint[0] )
    b = int( rangeint[1] )
    n = int( input() )

    for guess in range(n):
        a+=1
        print( a )
        resp = input()
        
        if resp == "CORRECT":
            break
