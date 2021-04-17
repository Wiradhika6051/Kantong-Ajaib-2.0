# F03 - PENCARIAN GADGET BERDASARKAN RARITY
def carirarity(databases):
# Mencari semua gadget dengan rarity yang diinput pengguna
# Rarity = C, B, A, dan S
    rarity = input("Masukkan rarity: ")
    print("\nHasil pencarian:\n")
    temp = []
    for database in databases:
        for data in database:
            if data == rarity:
                printfound(database)
                temp = [1]
    if temp == []:
        print("Tidak ada gadget yang ditemukan")

# F04 - PENCARIAN GADGET BERDASARKAN TAHUN
def caritahun(databases):
# Mencari semua gadget sesuai dengan tahun dan kategori yang diinput pengguna
# Kategori : =, >, <, >=, dan <=
    tahun = input("Masukkan tahun: ")
    kategori = input("Masukkan kategori: ")
    print("\nHasil pencarian:\n")
    temp = []
    for database in databases:
        if kategori == "=":
            if tahun == database[len(database)-1]:
                printfound(database)
                temp = [1]
        elif kategori == ">":
            if tahun < database[len(database)-1]:
                printfound(database)
                temp = [1]
        elif kategori == "<":
            if tahun > database[len(database)-1]:
                printfound(database)
                temp = [1]
        elif kategori == ">=":
            if tahun <= database[len(database)-1]:
                printfound(database)
                temp = [1]
        elif kategori == "<=":
            if tahun >= database[len(database)-1]:
                printfound(database)
                temp = [1]
    if temp == []:
        print("Tidak ada gadget yang ditemukan")

def printfound(arr):
# Mencetak semua gadget yang ditemukan dalam hasil pencarian
    temp = arr
    hasil = ["Nama            :","Deskripsi       :","Jumlah          :","Rarity          :","Tahun ditemukan :"]
    for j in range(len(hasil)):
        hasil[j] += temp[j+1]
    for x in range (len(hasil)):
        if x == 2:
            print(hasil[x],"buah")
        else:
            print(hasil[x])
    print()