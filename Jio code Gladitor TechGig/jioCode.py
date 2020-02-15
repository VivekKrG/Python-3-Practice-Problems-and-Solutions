''' Read input from STDIN. Print your output to STDOUT '''
'''Find the maximum sum such that the subset of given integer array should not have any digit in common.

Let me give you an example, Suppose there is an array of 5 integers with positive integers as 14, 12, 23, 45, 39 .

14 and 12 cannot be taken in the subset as 1 is common in both. Similarly {12, 23}, {23, 39}, {14, 45} cannot be included in the same subset.

So the subset which forms the maximum sum is {12, 45, 39}. The maximum sum such formed is 96'''

# Use input() to read input from STDIN and use print to write your output to STDOUT


def integers(num):
    intg = set()
    while num:
        intg.add(num % 10)
        num //= 10
    return intg


def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        nums = input()
        nums = nums.split()

        num = []
        for i in range(n):
            num.append(int(nums[i]))
        num = sorted(num)
        num.reverse()   # Decreasing order, first will be max.

        grp = []        # Now making all possible set having no digit in common
        for i in range(n):
            grp.append(num[i])
            grpintg = integers(num[i])
            for j in range(i+1,n):      # loop from i+1 gives 24 marks, from 0 gives 37 marks
                temp = integers(num[j])
                if not grpintg & temp:
                    grp[i] += num[j]
                    grpintg = grpintg | temp
        print(max(grp))


main()
'''Sample input
3
4
3 5 7 2
5
121 23 3 333 4
7
32 42 52 62 72 82 92
'''
