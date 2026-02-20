'''
Nama: Fahrizal Azis
NIM: J0403251151
Kelas: TPL A1
'''
#Implemetasi Dasar: Stack
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/ diinstansiasi
    def __init__(self, data):
        self.data = data #menyimpan data pada node
        self.next = None #pointer untuk menunjuk ke node berikutnya, awalnya None karena belum ada node berikutnya

#Stack ada operasi push(memasukkan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None

    def push(self, data): #memasukkan data baru ke dalam stack
        #1. membuat node baru dengan data yang diberikan
        nodeBaru = Node(data)#instantiasi/ memanggil konstruktor pada class node

        #2. node baru menunjuk ke node yang saat ini menjadi top
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil/menghapus node paling atas(top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
    
    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top ->", end="")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    
#Instansi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek(lihat top):", s.peek())
s.pop()
s.tampilkan()
print("Peek(lihat top):", s.peek())
