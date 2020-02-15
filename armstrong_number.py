'''
Program for Armstrong Numbers
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called
an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Example:

Input : 153
Output : True
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : False
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1253
Output : False
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input : 1634
Output : True
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
'''
def checkArmStrong(num):
    given_number = num
    n_digits = len(str(num))
    sum = 0
    while num:
        sum += (num%10)**n_digits
        num //=10
    if sum == given_number:
        return True
    else:
        return False
