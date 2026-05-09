from LinkedList import *

class Queue(LinkedList):
    def __init__(self, capacity):
        super().__init__()
        self.cap = capacity
    
    def enqueue(self, data):
        if self.size == self.cap:
            print("Queue, overflow error")
            return
        
        super().insert(Node(data))

    def Dequeue(self):
        if self.size == 0:
            print("Queue, underflow error")
            return

        node : Node = self.head
        self.head = self.head.next
        self.size -= 1
        return node
    
    def peak(self):
        return self.head
    
    def is_full(self):
        if self.size == self.cap:
            return True
        return False

if __name__ == "__main__":
    print("=== TEST 1: Normal ekleme ve Dequeue ===")
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    n = q.Dequeue()
    if n:
        print("Beklenen: 10 | Gelen:", n.data)

    n = q.Dequeue()
    if n:
        print("Beklenen: 20 | Gelen:", n.data)


    print("\n=== TEST 2: Boş queue Dequeue ===")
    q2 = Queue(3)
    n = q2.Dequeue()
    print("Beklenen: None + hata mesajı | Gelen:", n)


    print("\n=== TEST 3: Tek eleman ===")
    q3 = Queue(3)
    q3.enqueue(99)

    n = q3.Dequeue()
    if n:
        print("Beklenen: 99 | Gelen:", n.data)

    n = q3.Dequeue()
    print("Beklenen: None | Gelen:", n)


    print("\n=== TEST 4: FIFO kontrol ===")
    q4 = Queue(5)
    q4.enqueue(1)
    q4.enqueue(2)
    q4.enqueue(3)

    print("Beklenen sıra: 1, 2, 3")
    while True:
        n = q4.Dequeue()
        if not n:
            break
        print("Gelen:", n.data)


    print("\n=== TEST 5: Karışık işlemler ===")
    q5 = Queue(5)
    q5.enqueue(5)
    q5.enqueue(6)

    n = q5.Dequeue()
    if n:
        print("Beklenen: 5 | Gelen:", n.data)

    q5.enqueue(7)
    q5.enqueue(8)

    print("Beklenen sıra: 6, 7, 8")
    while True:
        n = q5.Dequeue()
        if not n:
            break
        print("Gelen:", n.data)
    
    print("\n=== TEST 6: Peak ===")
    q6 = Queue(3)
    q6.enqueue(3)
    q6.enqueue(1)
    q6.enqueue(2)
    print("Beklenen: 3")
    print("Gelen:", q6.peak().data)