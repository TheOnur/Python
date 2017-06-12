class Stack:
    def __init__(self):
        self.arr = []
        self.count = 0

    def is_empty(self):
        return len(self.arr) == 0

    def push(self, data):
        self.arr.append(data)
        self.count = self.count + 1

    def pop(self):
        self.arr.pop(len(self.arr) - 1)
        self.count = self.count - 1

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is Empty!')
        n = len(self.arr)
        return self.arr[n - 1]

    def traversal(self):
        n = len(self.arr)
        for i in range(n-1, -1, -1):
            print(self.arr[i])

    def get_count(self):
        return self.count


s = Stack()
s.push(2)
s.push(4)
s.push(6)
