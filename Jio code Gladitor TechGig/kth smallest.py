'''
Using Quick sort
'''
def find_kth(arr, l, r, k):
    #pivot in at arr[l]
    #I'll devide array into two halfs, Yellow and Green(for greater values)
    yellow = l+1
    level = 0
    for green in range(l+1,r):
        if arr[green] < arr[l]:
            (arr[yellow], arr[green])=(arr[green], arr[yellow])
            yellow += 1
    #now mov pivot to its own place
    (arr[l], arr[yellow-1]) = (arr[yellow-1], arr[l])
    if yellow-1 == k-1:
        return arr[k-1]
    elif yellow-1 < k-1:
        return find_kth(arr, yellow, r, k)
    else:
        return find_kth(arr, 0, yellow-1, k)

arr = [1,3,2,57,9,5,35,10,12]
print(find_kth(arr, 0, len(arr), 9))
