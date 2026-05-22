# List sinifindan kalitim alarak [3] * 5 gibi bir islem dene
class Array:
    def __init__(self, capacity):
        self.cap = capacity
        self.datas = [0] * self.cap
        self.size = 0

    # Insertions : At Beginning, At given position and At the end.
    def insert(self, data, index = -1):
        self.datas[self.size] = data
        self.size += 1

        if self.size == self.cap:
            self.cap *= 2
            self.datas += [0] * (self.cap // 2)

    # Deletion : From Beginning, Given Position, First Occurrence, All occurrences and From End
    # Ilk eslesen degeri siler ve listeyi kaydirir. Yoksa -1 doner.
    def delete(self, data):
        index = self.search(data)
        if index > -1:
            deleted = self.datas[index]
            for i in range(index + 1, self.size):
                self.datas[index] = self.datas[i]
                index = i
            return deleted
        return index

    # Searching : Linear Search and Binary Search
    def search(self, data, binary = False) -> int:
        for i in range(self.size):
            if self.datas[i] == data:
                return i
        return -1

    def sort(self, reverse = False):
        pass



if __name__ == "__main__":
    pass