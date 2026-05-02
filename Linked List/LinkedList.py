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
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def delete(self, node : Node):
        # liste bos ise
        if self.head == None:
            return
        
        # silinmesi istenen dugum head ise
        if self.head == node:
            self.head = self.head.next # None or Node

            if self.head == None:
                self.tail = None
            
            self.size -= 1
            return

        # aradan bir eleman silinmek istendiginde
        n : Node = self.head
        while n:
            if n.next == node:
                # tail dugumunun bir onceki elemanina ulasmak icin takip sart
                if node == self.tail:
                    self.tail = n

                n.next = node.next

                self.size -= 1
                break
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