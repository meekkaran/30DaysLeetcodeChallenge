def delete_node(head, key):
    prev = None
    current = head

    while current is not None:
      if current.data == key:
        if current == head:
          head = head.next
          current = head
        else:
          prev.next = current.next
          current = current.next
      else:
        prev = current
        current  = current.next

    #if key is not in list
    if current == None:
      return head
    return head
