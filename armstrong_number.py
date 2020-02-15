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
