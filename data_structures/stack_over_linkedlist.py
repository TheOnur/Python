class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.head
        self.head = node

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        return self.head.data

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        temp = self.head
        self.head = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def get_length_iterative(self):
        length = 0
        temp = self.head
        while temp:
            length = length + 1
            temp = temp.next
        return length

    def get_length_recursive(self, head):
        if head is None:
            return 0
        return 1 + self.get_length_recursive(head.next)

s = Stack()
s.push(2)
s.push(4)
s.push(6)
s.traverse()
