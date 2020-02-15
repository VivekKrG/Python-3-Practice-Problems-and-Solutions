#Success ..

def merge(list1, list2):
    if len(list1)==0 or len(list2)==0:
        return list1+list2
    else:
        n1 = len(list1)
        n2 = len(list2)

        out = []
        j = 0
        for i in range(n1):
            if j < n2:
                if list1[i] <= list2[j]:
                    out.append(list1[i])
                else:
                    temp = j
                    while (j < n2 and list2[j]< list1[i]):
                        j += 1
                    out.extend(list2[temp:j])
                    out.append(list1[i])
            else:
                out.extend(list1[i:])
        if j<n2:
            out.extend(list2[j:])

    return out


def mergeSort(numList):
    if len(numList)<2:
        return numList
    else:
        return merge(mergeSort(numList[:len(numList)//2]), mergeSort(numList[len(numList)//2:]))
