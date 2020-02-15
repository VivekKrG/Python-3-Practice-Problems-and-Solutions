def fabonacci(n):
        term1=1
        term2=1
        if n==1 or n==2:
                return 1
        for i in range(n-2):
                temp=term1+term2
                term1=term2
                term2=temp
        return(term2)
def prime(n):
        if n==1:
                return 2
        temp=1
        while(True):
                for j in range(3,1000):
                        for k in range(2,int(j**0.5)+2):
                                if (j%k==0):
                                        break
                        if (k==int(j**0.5)+1):
                                temp=temp+1
                                if (temp==n):
                                        return j
"""
Series conatin sTwo series(odd: fabonakki even: prime)
odd place : 1  1  2  3  5   8   13   21   34   55
even place:   2  3  5  7  11  13   17   19    23
reurn nth number from series
"""
def nthNum():
        n= int(input("Enter position"))
        if(n%2):
               return( fabonacci(n//2+1))
        else:
               return( prime(n/2) )
