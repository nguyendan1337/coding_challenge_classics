def extractAndAppendSponsoredNodes(head):
    # Write your code here
    if not head or not head.next:
        return head

    odd_head = head.next
    odd_tail = odd_head

    even_head = None

    current = head
    i = 0

    while current:
        next_node = current.next

        if i%2==0:
            current.next = even_head
            even_head = current
        else:
            odd_tail.next = current
            odd_tail = current

        current = next_node
        i += 1

    odd_tail.next = even_head
    return odd_head