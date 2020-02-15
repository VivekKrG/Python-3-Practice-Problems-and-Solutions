def testPowerOf2(n):            '''Basic concept'''
        while(n//2>2 and n%2==0):
            n=n//2

        if(n%2):
            return False
        else:
            return True
            
def testPowerOf2b(n):           '''same work in short way'''
        while(n/2>2):
            n=n/2

        if(n%2):
            return False
        else:
            return True
