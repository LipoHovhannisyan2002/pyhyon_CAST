class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:

        val1 = l1.val
        val2 = l2.val


        total = val1 + val2 + carry

        carry = total // 10

        digit = total % 10
        print(digit)

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next
        l2 = l2.next

    return dummy_head.next


l1 = ListNode()
l1.next = ListNode(5)
l1.next.next = ListNode(4)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next




