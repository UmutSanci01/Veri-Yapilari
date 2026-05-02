class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, node : Node):
        if self.size == 0:
            head = node
            tail = head
            return
        
        tail.next = node
        tail = node
    
    def delete(self, node : Node):
        n : Node = self.head
        while n:
            if n == node or n.next == node:
                if node.next:
                    n.next = node.next
                else:
                    n.next = None
            n = n.next
    
    def show(self):
        n : Node = self.head
        while n:
            print(n.data)
            n = n.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert(Node(15))
    linked_list.insert(Node(25))
    linked_list.insert(Node(35))

    linked_list.show()