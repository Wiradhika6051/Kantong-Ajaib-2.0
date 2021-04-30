#hapusitem.py
#File yang berisi fungsi-fungsi yang berhubungan dengan aktivitas menghapus item dari database(F06)
import general_function as general

#F06 - MENGHAPUS ITEM ATAU CONSUMABLE
def hapusitem(user,gadget_database,consumable_database):
# Fungsi untuk menghapus item dari database dan menghasilkan database sementara yang telah diupdate
# Kamus Lokal:
# idx:integer(indeks database dimana item ditemukan)
# data:Data(data mengenai item yang ingin dihapus)
# noid:string(id dari item yang ingin dihapus)
# item_type:string(tipe item)
# yakin:string(variabel untuk menyimpan hasil konfirmasi)
# Algoritma
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        # Cek kolom csv ke (noid) kosong atau nggak -> csv sesuai dulu apakah gadget.csv atau consumable.csv
        idx = -1
        data = []
        item_type = ""
        if(noid[0] == 'G'):
            idx = general.search_idx(gadget_database,noid)
            data = gadget_database[idx]
            item_type = "gadget"
        elif(noid[0]=='C'):
            idx = general.search_idx(consumable_database,noid)
            data = consumable_database[idx]
            item_type = "consumable"
        if idx==-1:                                         #Item tidak ada di database
            print("Tidak ada item dengan ID tersebut")
        else: #idx!= -1(item ada)
            yakin = input("Apakah anda yakin ingin menghapus "+data[1]+" (Y/N)?")
            while not(yakin == 'Y' or yakin == 'N'):
                print("Jawaban harus Y atau N")
                yakin = input("Apakah anda yakin ingin menghapus "+data[1]+" (Y/N)?")
            if yakin == 'Y':
                if(item_type=="gadget"):
                    gadget_database.pop(idx)                        #Hapus entri item tersebut
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    consumable_database.pop(idx)                    #Hapus entri item tersebut
                    print()
                    print("Item telah berhasil dihapus dari database.")
            else: #yakin == 'N'
                print()
                print("Item gagal dihapus dari database.")
    else:
        print("Hanya admin yang dapat menghapus item.")
        print()
    return (gadget_database,consumable_database)

    
                          
            
        
