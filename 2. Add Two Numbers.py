l1 = [2,4,3]
l2 = [5,6,4]


def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    number1 = ''
    number2 = ''
    for i in l1:
        number1 += str(i)
    for j in l2:
        number2 += str(j)
    summ = int(number1)+int(number2)
    summ_str = str(summ)
    result = [int(i) for i in summ_str]
    reversed_copy = result.copy()
    reversed_copy.reverse()
    return reversed_copy

print(addTwoNumbers(l1,l2))










