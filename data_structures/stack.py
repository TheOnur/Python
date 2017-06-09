class StackNode(object):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return 'Stack_Node_' + str(self.data)

class Stack(object):
    arr = []
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty!')
        else:
            n = len(self.arr)
            temp = self.arr[n - 1]
            del self.arr[n - 1]
            return temp 
    
    def push(self, data):
        new_node = StackNode(data)
        if self.isEmpty():
            self.head = new_node
            self.arr.append(new_node)
        else:
            self.arr.append(new_node)
    
    def traverse(self):
        n = len(self.arr)
        for i in range(n - 1, -1 , -1):
            print(self.arr[i].data)
    
    def clear(self):
        self.arr = []
        self.head = None

s = Stack()
s.push('2')
s.push('4')
s.push('6')
s.pop()
s.traverse()