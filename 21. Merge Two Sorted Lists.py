list1 = [1, 2, 4]
list2 = [1, 3, 4]
listrestult = list2 + list1


def insertion_sort(InputList):

    for i in range(1, len(InputList)):

        j = i-1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
            InputList[j+1] = nxt_element
    return InputList

def mergeTwoLists(list1, list2):

    sumList = list2 + list1
    sortedList = insertion_sort(sumList)
    return sortedList










print(mergeTwoLists(list1,list2))
