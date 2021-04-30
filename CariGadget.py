#CariGadget,py
#File berisi fungsi-fungsi untuk menjalankan command yang berhubungan dengan pencarian gadget (F03 dan F04)
import general_function as general

def printfound(arr):
# I.S. : arr terdefinisi
# F.S. : Mencetak semua gadget yang ditemukan dalam hasil pencarian. 
# hasil : array of string (Untuk menyimpan data yang ingin ditampilkan)
# j : integer (kounter loop)
# x : integer (kounter loop)
# Algoritma
    hasil = ["Nama            :","Deskripsi       :","Jumlah          :","Rarity          :","Tahun ditemukan :"]
    for j in range(general.panjang(hasil)):                                 #Menambahkan isi arr ke tiap elemen hasil
        if(j==2 or j==4):#jumlah dan tahun ditemukan perlu dikonversi ke string
            hasil[j] += str(arr[j+1])
        else:#Jika selain kolom jumlah dan tahun ditemukan
            hasil[j] += arr[j+1]
    for x in range (general.panjang(hasil)):                                #Menampilkan hasil
        if x == 2:
            print(hasil[x],"buah")
        else:
            print(hasil[x])
    print()

# F03 - PENCARIAN GADGET BERDASARKAN RARITY
def carirarity(databases):
# I.S. : databases terdefinisi
# F.S. : Mencari semua gadget dengan rarity yang diinput pengguna dan menampilkan hasilnya. Jika tidak ada,maka mencetak "Tidak ada gadget yang ditemukan"
# Rarity = C, B, A, dan S
# Kamus Lokal:
# rarity:string  (kriteria rarity yang dicari)
# database : Gadget (kounter loop untuk databases. Berupa elemen dari databases)
# ada : boolean( mengasilkan true jika minimal ada 1 item yang sesuai kriteria rarity,selain itu false)
# Algoritma
    rarity = input("Masukkan rarity: ")
    print("\nHasil pencarian:\n")
    ada = False
    for database in databases:
        if database[4] == rarity:
                printfound(database)
                ada = True
    if not ada:
        print("Tidak ada gadget yang ditemukan")
        print()

# F04 - PENCARIAN GADGET BERDASARKAN TAHUN DITEMUKAN
def caritahun(databases):
# Mencari semua gadget sesuai dengan tahun dan kategori yang diinput pengguna dan menampilkan hasilnya. Jika tidak ada,maka mencetak "Tidak ada gadget yang ditemukan"
# I.S. : databases tedefinisi
# F.S. : Mencari semua gadget sesuai dengan tahun dan kategori yang diinput pengguna
# Kategori : =, >, <, >=, dan <=
# Kamus Lokal:
# tahun : integer (tahun yang menjadi kriteria pencarian)
# kategori : string (kategori(lebih besar,lebih kecil,dsb.) untuk melakukan pencarian)
# ada : boolean( mengasilkan true jika minimal ada 1 item yang sesuai kriteria rarity,selain itu false)
# database : Gadget (kounter loop untuk databases. Berupa elemen dari databases)
# Algoritma 
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print("\nHasil pencarian:\n")
    ada = False
    for database in databases:
        if kategori == "=":
            if tahun == database[general.panjang(database)-1]:
                printfound(database)
                ada = True
        elif kategori == ">":
            if tahun < database[general.panjang(database)-1]:
                printfound(database)
                ada = True
        elif kategori == "<":
            if tahun > database[general.panjang(database)-1]:
                printfound(database)
                ada = True
        elif kategori == ">=":
            if tahun <= database[general.panjang(database)-1]:
                printfound(database)
                ada = True
        elif kategori == "<=":
            if tahun >= database[general.panjang(database)-1]:
                printfound(database)
                ada = True
    if not ada:
        print("Tidak ada gadget yang ditemukan")
        print()

