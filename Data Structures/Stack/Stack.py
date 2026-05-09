class Stack:
    def __init__(self, capacity):
        self.datas = [0] * capacity
        self.cap = capacity
        self.length = 0
    
    def push(self, data):
        if self.length == self.cap:
            self.datas += [0] * self.cap
            self.cap += self.cap
        
        self.datas[self.length] = data
        self.length += 1


    def pop(self):
        if self.length == 0:
            print("Stack, pop failed")
            return
        
        self.length -= 1
        return self.datas[self.length]
    
    def top(self):
        if self.length == 0:
            print("Stack, top failed")
            return
        return self.datas[self.length - 1]

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def size(self):
        return self.length
    
    def __str__(self):
        return str(self.datas[:self.length])

if __name__ == "__main__":
    print("--- 1. Stack Oluşturuluyor ---")
    s = Stack(2)
    print(s)
    print(f"Kapasite: {s.cap}, Boyut: {s.size()}")

    print("\n--- 2. Eleman Ekleniyor (Push) ---")
    s.push(10)
    s.push(20)
    print(s)
    print(f"Kapasite: {s.cap}, Boyut: {s.size()}")

    print("\n--- 3. Dinamik Kapasite Artışı (Taşma Testi) ---")
    s.push(30) # Burada kapasitenin 4'e çıkması lazım
    s.push(40)
    print(s)
    print(f"Kapasite: {s.cap}, Boyut: {s.size()}")
    
    print("\n--- 4. Okuma ve Silme (Top & Pop) ---")
    print(f"En üstteki eleman (Top): {s.top()}")
    print(f"Silinen eleman (Pop): {s.pop()}")
    print(s)
    
    print("\n--- 5. Dinamik Hafıza Daraltma (Shrink Testi) ---")
    s.pop()
    s.pop() # Bu noktada length 1, cap 4 kalacak. Oran %25 olduğu için cap 2'ye düşmeli.
    print(s)
    print(f"Kapasite: {s.cap}, Boyut: {s.size()}")

    print("\n--- 6. Uç Durum (Edge Case) Testleri ---")
    s.pop() # Son elemanı da sildik
    s.pop() # Boşken silmeye çalışma hatası
    s.top() # Boşken okumaya çalışma hatası