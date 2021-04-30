# peminjaman.py
# File yang berisi fungsi untuk melakukan peminjaman gadget(F08)
import general_function as general
import save
import LoginRegister

def sedang_dipinjam(database,id_gadget,id_peminjam):
# Fungsi yang menghasilkan True jika gadget dengan jenis yang sama sedang dipinjam,selain itu False
# Kamus Lokal
# data:Gadget(variabel untuk looping)
# Algoritma:
    for data in database:
        if(data[1]==id_peminjam and data[2]==id_gadget and data[5]=="False"):
            return True
    return False

# F08 - MEMINJAM GADGET
def pinjam (user,gadget_database,gadget_borrow_history):
# Fungsi untuk meminjam gadget dan menghasilkan database gadget_database dan gadget_borrow database yang telah diupdate
# Kamus Lokal:
# noid:string(id gadget yang ingin dipinjam)
# i:integer(indeks gadget tersebut dalam database gadget)
# item:Gadget(data mengenai gadget yang ingin dipinjam
# Tanggal:string(tanggal peminjaman gadget)
# Jumlah:integer(jumlah gadget yang dipinjam)
# new_borrow_entry:RiwayatPinjam(entri riwayat peminjaman gadget yang baru dipinjam)
# sedang_dalam_peminjaman : boolean(bernilai True jika gadget yang sama sedang dipinjam,selain itu False)
# Algoritma:
    if(user[5]=="user"):
        noid = input("Masukan ID item: ")
        if not(noid[0] == 'G'):
            print()
            print("Gagal meminjam item karena ID tidak valid.")
        else:                                                               #Jika karakter pertama pada noid bukan 'G' (bisa 'C' atau karakter lain.Jika berupa karakter lain,maka otomatis tidak akan ada entri dengan id tersebut)
            i = general.search_idx(gadget_database,noid)
            if(i==-1):                  
                print("Tidak ada item dengan id",noid+"!!")
            else:
                item = gadget_database[i]
                sedang_dalam_peminjaman = sedang_dipinjam(gadget_borrow_history,noid,user[0])
                if(not sedang_dalam_peminjaman):              #Sedang tidak meminjam barang yang sama
                    item[3] = int(item[3])
                    if(item[3]==0): #Jika stok gadget adalah 0
                        print("Stok gadget sedang kosong!! Anda tidak bisa meminjam gadget ini.")
                    else: #Stok gadget tidak kosong
                        Tanggal = input("Tanggal peminjaman: ")
                        Jumlah = int(input("Jumlah peminjaman: "))
                        if(Jumlah<=item[3]):
                            item[3] -= Jumlah
                            gadget_database[i] = item
                            new_borrow_entry = [save.get_last_id(gadget_borrow_history)+1,user[0],item[0],Tanggal,Jumlah,"False"]
                            gadget_borrow_history.append(new_borrow_entry)
                            print("Item",item[1],"(x"+str(Jumlah)+")","berhasil dipinjam")
                        else:           #Jumlah yang dipinjam>gadget yang tersedia
                            print("Jumlah gadget yang dipinjam melebihi jumlah gadget yang tersedia!!!")
                else:                                          #Barang yang ingin dipinjam sedang dalam proses peminjaman user bersangkutan
                    print("Anda sedang meminjam",item[1],"! Anda tidak bisa meminjam gadget bersangkutan jika Anda masih memiliki riwayat peminjaman gadget bersangkutan yang belum dikembalikan.")
                    print()
    else:       #Jike role yang login bukan 'user'
        print("Hanya user yang bisa meminjam gadget")
    return (gadget_database,gadget_borrow_history)