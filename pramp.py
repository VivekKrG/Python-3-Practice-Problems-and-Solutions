arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]


def spiral_copy(arr):
    row = len(arr)
    col = len(arr[0])

    i = 0  # for row
    j = -1  # for column

    left = 0
    right = col - 1

    up = 0
    down = row - 1

    mov = 0
    ans = []
    prev = 0  # for row or col
    dirn = 0  # for dir lr

    print(row * col)
    for count in range(row * col):
        print(count)
        #L->R
        if mov == 0:#if prev == 0 and dirn == 0:  # Now row-wise #in row left to right
            j += 1
            ans.append(arr[i][j])

            if j == right:
                mov = 1
                prev = 1  # for col
                dirn = 0  # Next will be up to down
                up += 1

        # '''for col up to down'''
        elif mov ==1: #prev == 1 and dirn == 0:  # Now column -wise # in col up to down
            i += 1
            ans.append(arr[i][j])

            if i == down:
                mov = 2
                prev = 0  # for col
                dirn = 1  # Next will be right to left
                right -= 1
        # arr = 1,2,3,4,5,10,15,20 j =col-1-1, i = row-1
        # '''for right to left'''
        elif mov == 2:#prev == 0 and dirn == 1:  # Now row-wise # in row right left
            print("inside 01", i, j)
            j -= 1
            ans.append(arr[i][j])

            if j == left:
                mov = 3
                prev = 1  # for col
                dirn = 1  # Next will be down to up
                down -= 1
        # arr = 1,2,3,4,5,10,15,20,19,--16, j =0, i = down= row-1-1
        #''' Else down to up'''
        else:
            i -= 1
            ans.append(arr[i][j])

            if i == up:
                mov = 0
                prev = 0  # for row
                dirn = 0  # Next will be left to right
                left += 1
    # arr = 1,2,3,4,5,10,15,20,19,--16,11,6, j =0, i = row-2

    return ans

print(spiral_copy(arr))
'''
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]

'''
'''
[1,    2,   3,  4,    5],
[6,    7,   8,  9,   10],
[11,  12,  13,  14,  15],
[16,  17,  18,  19,  20] 

# row = 2
# col = 3
row = len(inputMatrix)
col = len(inputMatrix[0])
'''