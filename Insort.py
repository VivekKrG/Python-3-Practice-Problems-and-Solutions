def insert(value, A):
    if A==[]:
        A.append(value)
        return (A)
    elif A[-1]<value:
        A.append(value)
        return(A)
    else:
        temp =A[-1]
        return( insert( temp, insert(value, A[:-2]) ) )
    
def isort(A):
    return( insert(A[0],A[1:]) )
