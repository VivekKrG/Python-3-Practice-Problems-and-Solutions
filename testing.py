def check(n, m):
    #n = candy m= people
    k= (1+8*n)**0.5 - 1
    k = k//(2*m)

    out = []
    if k==0:
        sm = 0
        for i in range(1, m+1):
            if sm+i < n:
                out.append(i)
                sm += i
            else:
                out.append(n-sm)
                for j in range(i+1, m+1):
                    out.append(0)
                break
        
    else:
        tempsum = m*k*(m*k +1)/2
        r = n - tempsum
        r = r -(k*m)
        
        val = k*(k-1)*m/2
        for i in range(1, m+1):
            if i<=r:
                if tempsum + m*k+i < n:
                    out.append( int(val + k*i + m*k+i))
                    tempsum += m*k+i
                else:
                    out.append( int(val + k*i + (n-tempsum)))
            else:
                out.append( int(val + k*i))
                
    return(out)
    
