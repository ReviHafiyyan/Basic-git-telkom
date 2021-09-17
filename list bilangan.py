'''sebuah program yang menerima input sejumlah bilangan bulat.
Kemudian, program akan memanggil fungsi printList(),
menambahkan list_bilangan[0] dengan 1,
dan memanggil kembali fungsi printList().
Fungsi printList() akan mencetak bilangan-bilangan ganjil dari list_bilangan

lengkapi fungsi printList() dan memanggilnya pada main program.'''


list_bilangan = list(map(int, input().split(" ")))

def printList():
  for x in list_bilangan :
    if (x % 2 == 1):
      print (x, end = " ")
  print ()

printList()
list_bilangan[0] += 1
printList()
