class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        d=ListNode(0)
        c=d
        carry=0
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            c.next = ListNode(digit)
            c = c.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return d.next