class Node:
    def __init__(self, data):
        self.data = data
        self.next : Node = None

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
    
    def delete(self, data):
        # liste bos ise
        if self.head == None:
            return
        
        # silinmesi istenen dugum head ise
        if self.head.data == data:
            self.head = self.head.next # None or Node

            if self.head == None:
                self.tail = None
            
            self.size -= 1
            return

        # aradan bir eleman silinmek istendiginde
        n : Node = self.head
        while n:
            if n.next.data == data:
                # tail dugumunun bir onceki elemanina ulasmak icin takip sart
                if n.next == self.tail:
                    self.tail = n
                
                n.next = n.next.next

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
    linked_list.delete(25)

    linked_list.show()