class QueueNode(object):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return 'Queue_Node_' + self.data

class Queue(object):
    arr = []
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
        self.arr.append(new_node)
    
    def dequeue(self):
        if self.head is None:
            raise Exception('Queue is empty!')
        else:
            del self.arr[0]
            self.head = self.arr[0]
    
        
    def isExist(self, data):
        n = len(self.arr)
        for i in range(n):
            if self.arr[i].data == data:
                return True
        return False 

    def clear(self):
        self.arr = []
        self.head = None
        self.tail = None
    
    def traverse(self):
        if self.head is None:
            raise Exception('Queue is Empty')
        
        n = len(self.arr)
        for i in range(n):
            print(self.arr[i].data)

q = Queue()
q.enqueue('2')
q.enqueue('4')
q.enqueue('6')
q.dequeue()
q.enqueue('2')
q.traverse()