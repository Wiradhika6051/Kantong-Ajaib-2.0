#history.py
#File berisi fungsi yang berhubungan dengan fungsionalitas untuk melihat riwayat(F11,F12,F13)

import general_function as general
def convert_to_date(string):
#Fungsi untuk mengkonversi string tanggal menjadi tipe Tanggal
#Kamus Lokal
#-
#Algoritma
    return [int(string[0:2]),int(string[3:5]),int(string[6:])]

def convert_to_string(date):
#Fungsi untuk mengkonversi tipe Tanggal menjadi string
#Kamus Lokal
#-
#Algoritma
    if(date[0]<10):
        date[0] = "0" + str(date[0])
    else:   #Jika hari sama dengan atau lebih besar dari 10
        date[0] = str(date[0])
    if(date[1]<10):
        date[1] = "0" + str(date[1])
    else:   #Jika bulan sama dengan atau lebih besar dari 10
        date[1] = str(date[1])
    return date[0]+"/"+date[1]+"/"+str(date[2])

def sort_by_x(array,x,col):
#Fungsi untuk mengurutkan entri berdasarkan elemen tanggal dari elemen tanggal terbaru ke elemen tanggal terlama dan mengembalikan entri yang sudah disort
#Kamus Lokal
# i:integer(kounter loop)
# new_array: RiwayatPinjam (array akhir berisi entri dengan tanggal terurut dari terbaru ke terlama)
# same_after_x_value: Tanggal (array yang menyimpan entri dengan elemen after_x pada tanggal yang sama.(Misal jika kita atur x=1 yang merupakan indeks untuk kolom bulan,
# maka fungsi ini akan berisi entri dengan nilai tahun sama.(tahun berada pada indeks 2 atau x+1.Maksud dari after_x adalah ini)))
# after_x_value: integer(nilai after_x)
# last:boolean(menghasilkan true jika elemen ini adalah elemen terakhir array)
# date: RiwayatPinjam(variabel untuk looping elemen dalam same_after_x_value)
#Algoritma
    if(general.panjang(array)>1):
        i=0
        new_array = []
        same_after_x_value = []
        after_x_value = array[i][col][x+1]
        while(i<general.panjang(array)):
            last = False
            while(array[i][col][x+1]==after_x_value and not(last)):
                same_after_x_value.append(array[i])
                if(i+1==general.panjang(array)):
                    last = True
                else:
                    i+=1
            same_after_x_value = general.sorting(same_after_x_value,col,x)
            for date in same_after_x_value:
                new_array.append(date)
            same_after_x_value = []
            if( not last):
                same_after_x_value = [array[i]]
                after_x_value = array[i][col][x+1]
            if(last or i+1 ==general.panjang(array)):
                for date in same_after_x_value:
                    new_array.append(date)
            i+=1
    else:
        new_array = array
    return new_array

def sort_date(date_array,col):
# Fungsi untuk mengurutkan entri riwayat dari tanggal terbaru ke tanggal terlama (tanggal secara keseluruhan)
# Kamus Lokal
# -
# Algoritma
    date_array = general.sorting(date_array,col,2)                          #Sorting tahun
    date_array = sort_by_x(date_array,1,col)                                #Sorting bulan
    date_array = sort_by_x(date_array,0,col)                                #Sorting hari
    return date_array

def search_item(database,id_):
# Fungsi yang menghasilkan item dengan id yang sesuai dengan id_ dalam database
# Kamus Lokal
# data: Data (variabel untuk looping)
# Algoritma:
    for data in database:
        if(data[0]==id_):
            return data

def process_history(database,date_idx):
# Fungsi untuk memproses riwayat seebelum ditampilkan(merubah string tanggal menjadi tipe Tanggal,menyortir entrinya,dan merubah Tanggal menjadi string kembali)
# Kamus Lokal:
# data:Data(variabel untuk looping)
# Algoritma:
    for data in database:
        data[date_idx] = convert_to_date(data[date_idx])
    database = sort_date(database,date_idx)
    for data in database:
        data[date_idx] = convert_to_string(data[date_idx])
    return database

#F11 - MELIHAT RIWAYAT PEMINJAMAN GADGET
def see_borrow_history(database,user,user_database,gadget_database,date_idx):
# I.S. : database riwayat(database),database user(user_database),database gadget(gadget_database),dan indeks untuk kolom tanggal(date_idx) terdefinisi
# F.S. : Menampilkan riwayat peminjaman gadget dari tanggal terbaru ke tanggal terlama
# Kamus Lokal
# lanjut: boolean( Variabel yang jika bernilai true,proses looping entri database berlanjut,selain itu tidak berlanjut)
# i:integer(kounter loop)
# borrower: User(data tentang user yang meminjam)
# item: Gadget (data tentang gadget yang dipinjam)
# jawaban: string(variabel untuk menentukan apakah pembacaan 5 entri berikutnya ingin dilakukan oleh pengguna)
# Algoritma
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            borrower =search_item(user_database,database[i][1])
            item = search_item(gadget_database, database[i][2])       
            print("ID Peminjaman:        "+str(database[i][0]))
            print("Nama Pengambil:       "+borrower[2])
            print("Nama Gadget:          "+item[1])
            print("Tanggal Peminjaman:   "+database[i][3])
            print("Jumlah:               "+str(database[i][4]))
            if(database[i][5]=="False"):                                            # Belum dikembalikan seluruhnya
                print("Status:               Masih dalam peminjaman")
            else:                                                                   # Sudah dikembalikan seluruhnya
                print("Status:               Sudah dikembalikan seluruhnya")
            print()                   
            i+=1
            if(i%5==0):
                jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                if(jawaban=='n'):                                                   # Pembacaan entri selesai
                    lanjut = False
        if(i==general.panjang(database)):                                   #Jika sudah di ujung database
            print("Tidak ada lagi entri yang ditemukan!!")
            print()
    else:                                                                           #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
        print()

#F12 - MELIHAT RIWAYAT PENGEMBALIAN GADGET
def see_return_history(database,user_database,user,gadget_database,borrow_database,date_idx):
# I.S. : database riwayat(database),database user(user_database),database gadget(gadget_database),dan indeks untuk kolom tanggal(date_idx) terdefinisi
# F.S. : Menampilkan riwayat pengembalian gadget dari tanggal terbaru ke tanggal terlama
# Kamus Lokal
# lanjut: boolean( Variabel yang jika bernilai true,proses looping entri database berlanjut,selain itu tidak berlanjut)
# i:integer(kounter loop)
# returner: User(data tentang user yang mengembalikan gadget)
# item: Gadget (data tentang Gadget yang dikembalikan)
# jawaban: string(variabel untuk menentukan apakah pembacaan 5 entri berikutnya ingin dilakukan oleh pengguna)
# Algoritma
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            borrow_id = general.search_idx(borrow_database, database[i][1])
            if(borrow_id!=-1):
                borrow_entry = borrow_database[borrow_id]
                returner =search_item(user_database,borrow_entry[1])
                item = search_item(gadget_database, borrow_entry[2])    
                print("ID Pengembalian:        "+str(database[i][0]))
                print("Nama Pengambil:         "+returner[2])
                print("Nama Gadget:            "+item[1])
                print("Tanggal Pengembalian:   "+database[i][2])
                print("Jumlah:                 "+str(database[i][3]))
                print()
                i+=1
                if(i%5==0):
                    jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                    if(jawaban=='n'):
                        lanjut = False   
        if(i==general.panjang(database)):       #Jika sudah di ujung database
            print("Tidak ada lagi entri yang ditemukan!!")
            print()
    else: #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
        print()

#F13 - MELIHAT RIWAYAT PENGAMBILAN CONSUMABLE
def see_take_history(database,user,user_database,consumable_database,date_idx):
# I.S. : database riwayat(database),database user(user_database),database consumable(cosumable_database),dan indeks untuk kolom tanggal(date_idx) terdefinisi
# F.S. : Menampilkan riwayat pengambilan consumable dari tanggal terbaru ke tanggal terlama
# Kamus Lokal
# lanjut: boolean( Variabel yang jika bernilai true,proses looping entri database berlanjut,selain itu tidak berlanjut)
# i:integer(kounter loop)
# taker: User(data tentang user yang mengambil consumable)
# item: Consumable (data tentang Consumable yang diambil)
# jawaban: string(variabel untuk menentukan apakah pembacaan 5 entri berikutnya ingin dilakukan oleh pengguna)
# Algoritma
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            taker =search_item(user_database,database[i][1])
            item = search_item(consumable_database, database[i][2])  
            print("ID Pengambilan:       "+str(database[i][0]))
            print("Nama Pengambil:       "+taker[2])
            print("Nama Consumable:      "+item[1])
            print("Tanggal Pengambilan:  "+database[i][3])
            print("Jumlah:               "+str(database[i][4]))
            print()            
            i+=1
            if(i%5==0):
                jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                if(jawaban=='n'):
                    lanjut = False
        if(i==general.panjang(database)):               #Jika sudah di ujung database
            print("Tidak ada lagi entri yang ditemukan!!")
            print()
    else: #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
        print()


