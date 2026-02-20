'''
Nama: Fahrizal Azis
NIM: J0403251151
Kelas: TPL A1
'''
#Implemetasi Dasar: Node pada Linked List
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class node dipanggil/ diinstansiasi
    def __init__(self, data):
        self.data = data #menyimpan data pada node
        self.next = None #pointer untuk menunjuk ke node berikutnya, awalnya None karena belum ada node berikutnya
#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan dan menghubungkan node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB #node A menunjuk ke node B
nodeB.next = nodeC #node B menunjuk ke node C

#4) Transversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #bergerak ke node berikutnya

#Implementasi Dasar: Stack
