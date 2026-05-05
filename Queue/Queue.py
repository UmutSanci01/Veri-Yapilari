from LinkedList import *

class Queue(LinkedList):
    def __init__(self, capacity):
        super().__init__()
    
    def insert(self, data):
        super().insert(Node(data))

    def pop(self):
        node : Node = self.head
        if node == None:
            print("Queue, pop failed")
        else:
            self.head = self.head.next
            self.size -= 1
        return node

if __name__ == "__main__":
    print("=== TEST 1: Normal ekleme ve pop ===")
    q = Queue(5)
    q.insert(10)
    q.insert(20)
    q.insert(30)

    n = q.pop()
    if n:
        print("Beklenen: 10 | Gelen:", n.data)

    n = q.pop()
    if n:
        print("Beklenen: 20 | Gelen:", n.data)


    print("\n=== TEST 2: Boş queue pop ===")
    q2 = Queue(3)
    n = q2.pop()
    print("Beklenen: None + hata mesajı | Gelen:", n)


    print("\n=== TEST 3: Tek eleman ===")
    q3 = Queue(3)
    q3.insert(99)

    n = q3.pop()
    if n:
        print("Beklenen: 99 | Gelen:", n.data)

    n = q3.pop()
    print("Beklenen: None | Gelen:", n)


    print("\n=== TEST 4: FIFO kontrol ===")
    q4 = Queue(5)
    q4.insert(1)
    q4.insert(2)
    q4.insert(3)

    print("Beklenen sıra: 1, 2, 3")
    while True:
        n = q4.pop()
        if not n:
            break
        print("Gelen:", n.data)


    print("\n=== TEST 5: Karışık işlemler ===")
    q5 = Queue(5)
    q5.insert(5)
    q5.insert(6)

    n = q5.pop()
    if n:
        print("Beklenen: 5 | Gelen:", n.data)

    q5.insert(7)
    q5.insert(8)

    print("Beklenen sıra: 6, 7, 8")
    while True:
        n = q5.pop()
        if not n:
            break
        print("Gelen:", n.data)