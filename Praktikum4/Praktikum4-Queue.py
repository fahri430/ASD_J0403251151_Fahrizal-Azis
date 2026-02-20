'''
Nama: Fahrizal Azis
NIM: J0403251151
Kelas: TPL A1
'''
#Implemetasi Dasar: Queue

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/ diinstansiasi
    def __init__(self, data):
        self.data = data #menyimpan data pada node
        self.next = None #pointer untuk menunjuk ke node berikutnya, awalnya None karena belum ada node berikutnya

class queue:
    def __init__(self):
        self.front = None #node depan (front) untuk menunjuk ke node paling depan (awalnya kosong)
        self.rear = None #node belakang (rear) untuk menunjuk ke node paling belakang (awalnya kosong)
    
    def is_empty(self):
        return self.front is None
    
    #membuat fungsi untuk menambahkan data baru pada bagian belakang
    def enqueue(self, data):
        nodeBaru = Node(data)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        self.rear.next = nodeBaru #rear menunjuk ke node baru
        self.rear = nodeBaru #update rear ke node baru

    def tampilkan(self):
        current = self.front
        print("Front ->", end="")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

    def dequeue(self):
        #menghapus data dari depan
        data_terhapus = self.front.data#lihat data terdepan
        self.front = self.front.next #geser front ke node berikutnya
        #jika setelah geser front menjadi none, berarti queue kosong, maka rear queue kosong
        #rear juga harus jadi  none
        if self.front is None:
            self.rear = None
        return data_terhapus
        print("Rear")

q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()