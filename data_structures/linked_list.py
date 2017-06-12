class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def traversal(self):
        temp = self.head
        while temp:
            print(str(temp.data))
            temp = temp.next

    def is_empty(self):
        return self.head is None

    def get_length_iterative(self):
        length = 0
        if self.is_empty():
            return length
        temp = self.head
        while temp:
            length = length + 1
            temp = temp.next
        return length

    def get_length_recursive(self, node):
        if node is None:
            return 0
        return self.get_length_recursive(node.next) + 1

    def delete_node(self, data):
        if self.is_empty():
            raise Exception('Empty List!')
        delete_node = self.head
        if delete_node.data == data:
            self.head = delete_node.next
            return
        while delete_node:
            if delete_node.data == data:
                break
            prev = delete_node
            delete_node = delete_node.next
        if delete_node is None:
            return
        prev.next = delete_node.next


linkedList = LinkedList()
linkedList.add_node(2)
linkedList.add_node(4)
linkedList.add_node(6)
print('Before Delete:' + str(linkedList.get_length_recursive(linkedList.head)))
linkedList.delete_node(2)
print('After Delete:' + str(linkedList.get_length_recursive(linkedList.head)))
linkedList.traversal()
