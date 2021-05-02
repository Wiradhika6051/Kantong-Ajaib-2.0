# tambahitem.py
# Folder berisi fungsi untuk menambah entri item(F05)
import general_function as general

#F05 - MENAMBAH ITEM
def tambahitem(gadget_database,consumable_database,user):
# Fungsi untuk menambah item ke dalam database,menghasilkan database yang telah terupdate
# Kamus Lokal
# noid:string(id item yang ingin ditambahkan)
# i:integer(indeks untuk mengecek apakah data sudah ada di dtaabase.Jika ada maka nilainya bukan -1,sedangkan jika belum nilainya -1)
# Nama:string(nama item yang ditambahkan)
# Deskripsi:string(deskripsi item yang ditambahkan)
# Jumlah:integer(jumlah item yang ditambahkan)
# Rarity:string(rarity item yang ditambahkan(yang valid:C,B,A,S))
# Tahun:integer(Tahun item ditemukan)
# new_entry:Data(entri data item baru yang ditambahkan)
# Algoritma
    if user[5] == "admin":
        noid = input("Masukan ID: ")
        if not(noid[0] == 'G' or noid[0] == 'C'):
            print("Gagal menambahkan item karena ID tidak valid.")
        else:                                                       #ID Valid(diawali 'G' atau 'C')
            i = -1
            if(noid[0] == 'G'):
                i = general.search_idx(gadget_database,noid)
            elif(noid[0]=='C'):
                i = general.search_idx(consumable_database,noid)
            print()
            if i!=-1:
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                if noid[0] == 'G':                                                          #Item yang dimasukkan berupa gadget
                    Nama = input("Masukan Nama: ")
                    Deskripsi = input("Masukan Deskripsi: ")
                    Jumlah = int(input("Masukan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if not(Rarity == 'C' or Rarity == 'B' or Rarity == 'A' or Rarity == 'S'):
                        print()
                        print("Input rarity tidak valid!")
                        return (gadget_database,consumable_database)
                    else:
                        Tahun = int(input("Masukan tahun ditemukan: "))
                    new_entry = [noid,Nama,Deskripsi,str(Jumlah),Rarity,Tahun]
                    gadget_database.append(new_entry)          
                    print("Item telah berhasil ditambahkan ke database")
                else:                                                                       #Item yang dimasukkan berupa consumable
                    Nama = input("Masukan Nama: ")
                    Deskripsi = input("Masukan Deskripsi: ")
                    Jumlah = int(input("Masukan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if not(Rarity == 'C' or Rarity == 'B' or Rarity == 'A' or Rarity == 'S'):
                        print()
                        print("Input rarity tidak valid!")
                        return (gadget_database,consumable_database)
                    new_entry = [noid,Nama,Deskripsi,str(Jumlah),Rarity]
                    consumable_database.append(new_entry)
                    print("Item telah berhasil ditambahkan ke database")  
    else:
       print("Hanya admin yang dapat menambah item.")
       print()
    return (gadget_database,consumable_database)
                
