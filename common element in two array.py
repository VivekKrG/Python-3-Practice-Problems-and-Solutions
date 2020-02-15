#Common Element in two arrays:-

def commonElem(arr1, arr2):
    common  = []
    j = 0
    for i in range(len(arr1)):
        if j < len(arr2):
            if arr1[i] == arr2[j]:
                common.append(arr1[i])
                j += 1
            elif arr2[j] < arr1[i]:
                while j < len(arr2) and arr2[j] < arr1[i]:
                    j += 1
                common.append(arr1[i])
                j += 1
        else:
            break
    return common
            
