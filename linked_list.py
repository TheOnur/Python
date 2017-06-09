class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return 'Node_' + self.data

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def delete(self, data):
        temp = self.head
        prev = self.head
        while temp:
            if temp.data == data:
                break
            temp = temp.next
        
        while prev:
            if prev.next and prev.next.data == data:
                break
            prev = prev.next

        if temp:
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
           

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



llist = LinkedList()
llist.append('2')    
llist.append('4')
llist.append('6')
llist.append('8')
llist.delete('8')
llist.print()