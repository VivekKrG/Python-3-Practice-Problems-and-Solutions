'''
Solution for a^3 + b^3 = c^3 + d^3
Using Python3 Programming Language
'''
Sums = dict()
solutions = []
for a in range(1, 21):
    for b in range(a+1, 21): #Making a,b distinct
        if (a**3 + b**3)not in Sums:
            Sums[a**3 + b**3] = (a, b)
        else:
            if (b, a) != Sums[a**3 + b**3]:#Insuring a,b and c,d are distinct
                solutions.append([(a,b), Sums[a**3 + b**3]])
print(solutions)
