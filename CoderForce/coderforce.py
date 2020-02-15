tests = int(input())
for __ in range(tests):
    num = int(input())
    if num < 10:
        print(num)
    else:
        count = 9
        k = 2
        value = 11
        while value < num:
            # numstring =
            for digit in range(1, 10):
                numstring = k*str(digit)
                value = int(numstring)
                if value <= num:
                    count += 1
                else:
                    break
            else:
                k += 1
        print(count)
