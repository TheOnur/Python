from stack_over_array import Stack

def reverse_stack():
    if not s.is_empty():
        head = s.peek()
        s.pop()
        reverse_stack()
        add_to_bottom(head)

def add_to_bottom(head):
    if s.is_empty():
        s.push(head)
    else:
        top = s.peek()
        s.pop()
        add_to_bottom(head)
        s.push(top)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
reverse_stack()
s.traversal()
