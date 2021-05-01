# Gacha.py
# File yang berisi fungsionalitas untuk gacha(FB03)
import os
import time
import general_function as general
import save

def rand_val():
    # Fungsi untuk menghasilkan angka acak menggunakan LCG DENGAN SEED int(time.time*1000)
    # Kamus lokal:
    # random:integer(angka acak yang dihasilkan)
    # Algoritma:
    random = int(time.time()*10000)
    random = (214013*random + 2531011) % (general.basic_pangkat(2,32))
    return random

def fill_inventory(consumable_database,consumable_borrow_database,user_id):
    # Fungsi untuk mengisi inventory user dari consumable yang dipinjam user
    # Kamus Lokal
    # inv: array of Inventory(Array berisi list inventory)
    # i:integer(kounter loop)
    # item_id:string(id consumable yang menjadi bagian dari inventory user)
    # item:Consumable(Data mengenai consumable yang menjadi bagian dari inventori)
    # Algoritma
    inv =[]
    for i in range(general.panjang(consumable_borrow_database)):
        if(consumable_borrow_database[i][1]==user_id):
            item_id = consumable_borrow_database[i][2]
            item = consumable_database[general.search_idx(consumable_database,item_id)]
            inv.append([user_id,item[1],consumable_borrow_database[i][4],item[4],consumable_borrow_database[i][0]])
    return inv

def show(inv):
    # Prosedur untuk menampilkan consumable dalam inventori yang bisa dicombine
    # I.S. inv terdefinisi
    # F.S. Menampilkan list consumable dalam inventori yang bisa dicombine
    # Kamus Lokal
    # i:integer(kounter loop)
    # Algoritma:
    # MENAMPILKAN INVENTORY MILIK USER
    print("==========INVENTORY==========")
    for i in range(general.panjang(inv)):
        print(str(i+1)+'.',inv[i][1],"(Rarity {})".format(inv[i][3]),"({})".format(inv[i][2]))
    print("=============================")    

def use_consumable(inventory,chances,consumable_history_database):
    # Fungsi untuk mengambil consumable dicombine dan mengembalikan rarity dan flag apakah proses gacha perlu dilakukan 
    # Kamus Lokal
    # cons:integer(nomor consumable yang ingin dipakai pengguna)
    # amount:integer(jumlah consumable yang ingin digunakan pengguna)
    # y:array of Char(array berisi list char rarity yang digunakan untuk menentukan rarity hasil gacha)
    # found:boolean(Menghasilkan true jika entri yang sesuai telah ditemukan,selain itu False)
    # id_consum:integer(indeks dari consumable yang diabil dalam database riwayat pengambilan consumable)
    # i:integer(kounter loop)
    # Algoritma
    # MENGGUNAKAN CONSUMABLES YANG DIMILIKI USER UNTEK MENAIKKAN DROP RATE
    show(inventory)
    cons = int(input("Pilih consumable yang mau digunakan: "))
    if(cons>general.panjang(inventory) or cons<1):              #Jika input pengguna diluar 1 sampai indeks ke-N+1.Dalam kasus ini proses gacha tidak berjalan
        print("Masukan tidak valid!!!")
        return (chances,False)
    if(inventory[cons-1][2]==0):                                #Jika stok consumable yang ingin dicombine kosong.Dalam kasus ini proses gacha tidak berjalan
        print("Stok Item kosong!!")
        return (chances,False)
    amount = int(input("Jumlah yang digunakan: "))
    if(amount<0):                                               #Jumlah yang dimasukkan negatif
        print("Jumlah item yang dimasukkan tidak boleh negatif!!!")
        return (chances,False)
    if inventory[cons-1]!=[]:                                   #Jika inventori di opsi yang dimasukkan pengguna tidak kosong
        if inventory[cons-1][2]-amount>=0:                      #Jika yang diminta masih dibawah jumlah stok barang
            inventory[cons-1][2] = inventory[cons-1][2]-amount
        else: # jika jumlah consumable yang ingin digunakan melebihi yang dipunya, yang akan digunakan adalah jumlah maksimal yang dimiliki
            amount = inventory[cons-1][2]
            inventory[cons-1][2] = 0
        print('\n'+inventory[cons-1][1],"(x{})".format(amount),"ditambahkan!")
        y = get_chance(inventory[cons-1][3],amount,chances)
    else:                                                        #Jika inventori di opsi yang dimasukkan pengguna kosong
        if inventory[cons][2]-amount>0:                          #Jika yang diminta masih dibawah jumlah stok barang
            inventory[cons][2] = inventory[cons-1][2]-amount
        else:                                                    #jika jumlah consumable yang ingin digunakan melebihi yang dipunya, yang akan digunakan adalah jumlah maksimal yang dimiliki
            amount = inventory[cons-1][2]
            inventory[cons][2] = 0
        print('\n'+inventory[cons][1],"(x{})".format(amount),"ditambahkan!")
    found = False
    id_consum = 0
    i = 0
    while (i < general.panjang(consumable_history_database)) and not found:
        if(consumable_history_database[i][0]==inventory[cons-1][4]):
            id_consum = i
            found = True
        i+=1
    consumable_history_database[id_consum][4] = consumable_history_database[id_consum][4] - amount
    return (y,True)
    
def get_chance(rare,amt,chances):
    # Fungsi untuk menaikkan drop rate seusai rarity consumable yang digunakan dengan memanipulasi array chances dan mengembalikan array chances yang telah dimanipulasi
    # Kamus Lokal
    # rarelist:Array of Rarity (array yang menyimpan pasangan rarity dan chancenya)
    # len_c:integer(jumlah elemen dengan karakter 'C' di dalamnya)
    # chance:char(variabel untuk looping)
    # i,j:integer(kounter loop)
    # added_rate:integer(rate tambahan yang didapatkan setelah penambahan consumable)
    # Algoritma
    # MENAIKKAN DROP RATE SESUAI DENGAN RARITY CONSUMABLE YANG DIGUNAKAN
    rarelist = [['C',0.1],['B',0.15],['A',0.2],['S',5.0]]
    len_c = 0
    for chance in chances:              #Menghitung jumlah elemen 'C' dalam array
        if chance=='C':
            len_c+=1
    for i in range(general.panjang(rarelist)):
        if rare==rarelist[i][0]:        #Untuk menemukan chance yang didapatkan dari penambahan consumable
            if rare=='C' or rare=='B' or rare=='A':     
                print("Chance mendapatkan rarity {}".format(rarelist[i+1][0])+" (+ {}%)".format(rarelist[i][1]*amt))
                added_rate = int(rarelist[i][1]*amt*100)            #Jumlah peningkatan rate
                for j in range(len_c-added_rate,len_c):             #Mekanisme peningkatan rate(dengan mengganti elemen di akhir-akhir dengan rarity satu tingkat diatasnya)
                    chances[j] = rarelist[i+1][0]
            elif rare=='S':                                         
                print("Chance mendapatkan rarity S (+ {}%)".format(amt*5.0))
                added_rate = int(amt*5.0*100)                       #Jumlah peningkatan rate
                for j in range(len_c-added_rate,len_c):             #Mekanisme peningkatan rate(dengan mengganti elemen di akhir-akhir dengan rarity satu tingkat diatasnya)
                    chances[j] = rarelist[i][0]
    return chances

def get_items(databases, rarity):
    # Fungsi untuk MENCARI ITEM DI DATA CONSUMABLES YANG SESUAI DENGAN RARITY YANG DI-GACHA-KAN dan me-return item tersebut
    # Kamus Lokal
    # items_byrare = Array of Consumable(list berisi Consumable dengan rarity hasil gacha)
    # i:Consumable(variabel untuk looping)
    # Algoritma:
    items_byrare = []
    for i in databases:
        if i[4]==rarity:
            items_byrare.append(i)
    return items_byrare

# FB03 - GACHA
def gacha(consumables_database, inventory, user,consumable_history_database):
    # Fungsi untuk MELAKUKAN GACHA UNTUK MENDAPATKAN CONSUMABLE BARU YANG *mungkin* RARITY-NYA LEBIH TINGGI dan mengembalikan inventori dan riwayat pengambilan consumable yang telah terupdate dengan
    # Hasil gacha dan consumable yang terpakai saat melakukan gacha
    # Inventori pengguna didapatkan dari riwayat pengambilan consumable mereka
    # Kamus Lokal:  
    # chance:array of char(list rarity yang bisa didapatkan)
    # y:array of Char(array berisi list char rarity yang digunakan untuk menentukan rarity hasil gacha.)
    # run_gacha:boolean(variabel untuk melakukan apakah gacha akan berjalan atau tidak. Jika True make berjalan selain itu tidak.)
    # choice:Char(variabel untuk menentukan apakah pengguna ingin menambahkan item lagi atau tidak)
    # rarity:integer(angka acak untuk menentukan rarity mana yang akan didapatkan)
    # items: array of Consumables(array berisi consumable dengan rarity hasil gacha mana saja yang bisa didapatkan)
    # gacha_result_id:integer(indeks dari item hasil gacha)
    # item: string(nama item hasil gacha)
    # idx:integer(indeks item hasil gacha dalam inventori. Bila belum ada di inventori,nilai dari variabel ini -1)
    # i:integer(kounter loop)
    # found:boolean(boolean(Menghasilkan true jika entri yang sesuai telah ditemukan,selain itu False)
    # last_took_id:integer(id terbesar dalam riwayat pengambilan consumable)
    # new_item:Item(data mengenai item hasil gacha)
    # new_took_entry:RiwayatAmbil(entri 'pengambilan' hasil gacha)
    # id_consum:integer(indeks dari consumable yang diabil dalam database riwayat pengambilan consumable)
    # Algoritma:
    if user[5] == "user":      
        # DATA RARITY YANG MUNGKIN DIDAPAT (C,B,A,S)
        chance = ['C' for i in range(6250)]+['B' for i in range(2500)]+['A' for i in range(1200)]+['S' for i in range(50)]
        y,run_gacha = use_consumable(inventory,chance,consumable_history_database)
        choice = input("\nTambahkan item lagi? (y/n) : ")
        while choice=='y' or choice=='Y':
            os.system('cls||clear')
            y,run_gacha = use_consumable(inventory,y,consumable_history_database)
            choice = input("\nTambahkan item lagi? (y/n) : ")
        print()
        if((choice=='n' or choice=='N') and run_gacha):
        # SEBAGAI "LOADING SCREEN" UNTUK GACHA
            general.loading_progress("Rolling")
            rarity = rand_val()% (general.panjang(y[1])) # yang terlebih dahulu digacha adalah rarity
            items = get_items(consumables_database, y[rarity])
            gacha_result_id = rand_val()%(general.panjang(items))
            item = items[gacha_result_id][1] # lalu item dalam rarity tersebut digacha
            idx = -1
            i = 0
            found = False
            while (i < general.panjang(inventory))and not found:
                if(inventory[i][1]==item):
                    idx = i
                    found = True
                i+=1
            last_took_id = save.get_last_id(consumable_history_database)
            print("\nSelamat anda mendapatkan",item+"!(Rarity {})".format(y[rarity]))
            if(idx==-1):                                                        #Jika hasil gacha belum ada di inventori,buat entri baru
                new_item = [user[0],item,1,y[rarity],last_took_id+1]
                inventory.append(new_item) # Menambahkan item ke inventory
                new_took_entry = [last_took_id+1,user[0],items[gacha_result_id][0],consumable_history_database[gacha_result_id][3],1]
                consumable_history_database.append(new_took_entry)
            else:                                                                #Jika hasil gacha sudah ada di inventori,langsung tambahkan dan ubah
                found = False   
                id_consum = 0
                i = 0
                inventory[idx][2]+=1
                while (i < general.panjang(consumable_history_database)) and not found:
                    if(consumable_history_database[i][0]==inventory[idx][4]):
                        id_consum = i
                        found = True
                    i+=1
                consumable_history_database[id_consum][4]= consumable_history_database[id_consum][4] + 1
    else:                                               #Jika yang mengakses bukan user
        print("Hanya user yang dapat melakukan gacha!!")
    return(inventory,consumable_history_database)