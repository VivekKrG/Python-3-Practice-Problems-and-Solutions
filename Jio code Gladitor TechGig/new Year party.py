'''

Neighbours and New Year Party (100 Marks)
In the XYZ society, the neighbours hate each other for their attitude. Various activities are organized in the society for Welcoming the New Year. The tickets were provided to each house with an integer written on it. Some got tickets with positive integers and some got tickets with negative integers. In the evening, people had to carry their tickets to the club house where the eligible ones will get the exciting gifts. The eligibility of winning the gift depends on the maximum sum which can be formed from the tickets numbers keeping in mind that neighbours hate each other. Since the neighbours hate each other, the two cannot be together in the list of maximum sum. 





The President of the society, Mr. Singh, is a wise man and know that neighbours in society don't like each other. Also, he don't wish to become bad in front of people. So, he came up with an idea to design a program which will provide the list of integers forming maximum sum and thus all the members of the list will be given the gifts. The only problem with this idea is that he don't know programming so he is asking you to provide the correct list of integers. The people may be annoying but are smart and will fight if the list provided by you doesn't form the maximum sum.


Note: The integer written on ticket of individuals may or may not be unique. In case, when there are two list with equal maximum sum, the list with first greater element would be considered. For better understanding, look at the explanation of Test case 4 in Sample Test Case. The tickets with integer 0 are not considered for winning the gifts.


Input Format
The first line of input consist of number of test cases, T.

The first line of each test case consist of the number of houses (tickets distributed) in society, N.

The second line of each test case consist of N space separated tickets with integer written on them.




Constraints
1<= T <=10

1<= N <=10000

-1000<= Integer_on_Ticket <=1000



Output Format
For each test case, print the ticket numbers in a single line forming the maximum sum in the format similar to Sample Test Case.

Sample TestCase 1
Input
5
5
-1 7 8 -5 4 
4
3 2 1 -1 
4
11 12 -2 -1 
4
4 5 4 3 
4
5 10 4 -1
Output
48
13
12
44
10
Explanation
Test Case 1: Maximum sum which can be formed is 12. Element considered 8, 4. Note that Output is printed from the reverse side of the array which is TRUE for all the test cases without the space. So, the output is 48.
Test Case 2: Maximum sum which can be formed is 4. Element considered 3, 1. Output = 13.
Test Case 3: Maximum sum which can be formed is 12 as by taking any other element value of maximum sum decreases.
Test Case 4: Maximum sum which can be formed is 8 by taking 3, 5 or 4, 4. But the output is 4, 4 as 3 is smaller than 4.
Test Case 5: Maximum sum which can be formed is 10.
6
4
-4 -3 -1 -2
8
3 -4 2 0 0 -2 4 2
7
90 1 4 3 2 5 50
2
1 2
3
89 90 2
15
2 0 5 7 -1 0 8 4 1 3 -2 0 0 2 -2

Output:
-1
423
502490
2
289
23872
'''
def main():
    testcases=int( input() )

    while(testcases):
        house=int( input() )
           
        sticket  = input().split()   #string input as powers space separated
        
        ticket= []
        for i in sticket:
            ticket+=[ int(i) ] 
        
        big= max(ticket)
        bigindex = ticket.index( max(ticket) )

        # End cases 1
        if bigindex==0:
            big2=max(ticket[2:])
            if big < big + big2:
                print( str( big2) + str(big) )
            else:
                print(big)
            

        # End cases 2
        elif bigindex==house-1:
            big2=max(ticket[2:])
            if big < big + big2:
                print( str( big) + str(big2) )
            else:
                print(big)
        else:
            rbig=ticket[ bigindex +1]
            lbig=ticket[ bigindex -1]

            ticket.remove( lbig )
            ticket.remove( big )
            ticket.remove( rbig )
            
            big2= max(ticket)
            
            ticket.insert(bigindex -1, lbig )
            ticket.insert(bigindex   , big )
            ticket.insert(bigindex +1, rbig )
            big2index=ticket.index(big2)
            #print(str(bigindex) + str(big2index))
            
            if ( big < big + big2 ):
                if (big + big2 > lbig+ rbig):
                    if bigindex > big2index:
                        print( str(big)+ str(big2) )
                    else:
                        print( str(big2)+ str(big) )

                elif( big + big2 == lbig+ rbig ):
                    if bigindex > big2index:
                        print( str(big)+ str(big2) )
                    else:
                        print(str(rbig) + str(lbig))
                        
                else:
                    print(str(rbig) + str(lbig))

            else:
                if (big > lbig+ rbig):    
                    print( str(big))
                else:
                    print(str(rbig) + str(lbig))

        testcases=testcases-1
    
main()




