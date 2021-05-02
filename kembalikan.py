#kembalikan.py
#File berisi fungsi-fungsi yang berhubungan dengan pengembalian gadget(F09 dan FB02)
import general_function as general
import save

#F09 - MENGEMBALIKAN GADGET dan FB02 - MENGEMBALIKAN GADGET SECARA PARSIAL
def kembalikan(user,gadget_database,gadget_borrow_history,gadget_return_history):
# Fungsi yang mengembalikan gadget ke database dan menghasilkan database yang telah diupdate
# Kamus Lokal
# n:array of integer(kounter untuk menampilkan nomor list gadget yang ingin dikembalikan)
# i:integer(kounter loop)
# gadget_id:string(id dari gadget)
# gadget: Gadget(data dari gadget)
# nominjam:integer(nomor peminjaman gadget)
# tgl:string(tanggal pengembalian gadget)
# jumlah:integer(jumlah gadget yang dikembalikan)
# new_return_entry:RiwayatKembali (entri pengembalian gadget)
# Algoritma:
    if user[5] == "user":
        #cetak entry peminjaman 
        n = []
        print("Berikut adalah gadget-gadget yang dipinjam :")
        for i in range (general.panjang(gadget_borrow_history)):
            if(gadget_borrow_history[i][1]==user[0] and gadget_borrow_history[i][4]!=0):
                gadget_id = general.search_idx(gadget_database,gadget_borrow_history[i][2])
                if(gadget_id!=-1):
                    gadget = gadget_database[gadget_id]
                    print(str(general.panjang(n)+1) + ".", gadget[1]+" (x"+str(gadget_borrow_history[i][4])+")")
                    n.append(i)
        print() #ngasih enter
        nominjam = int(input("Masukan nomor peminjaman: "))
        if(nominjam<1 or nominjam>=general.panjang(n)+1):      #Jika diluar list
            print("Nomor peminjaman tidak valid!!")
            return (gadget_borrow_history,gadget_return_history,gadget_database)
        tgl = input("Tanggal pengembalian: ")
        jumlah = int(input("Masukkan jumlah yang ingin dikembalikan:"))
        print()
        if(gadget_borrow_history[n[nominjam-1]][4]-jumlah>=0):
            if(gadget_borrow_history[n[nominjam-1]][4]==jumlah):
                gadget_borrow_history[n[nominjam-1]][5] = "True"
            gadget_borrow_history[n[nominjam-1]][4] -= jumlah
            gadget_id = general.search_idx(gadget_database,gadget_borrow_history[n[nominjam-1]][2])
            gadget_database[gadget_id][3] += jumlah
            new_return_entry = [save.get_last_id(gadget_return_history)+1,str(gadget_borrow_history[n[nominjam-1]][0]),tgl,str(jumlah)]
            gadget_return_history.append(new_return_entry)
            print("Item", gadget_database[gadget_id][1], "(x" + str(jumlah) + ")", "telah dikembalikan.")
        else: # jumlah yang dipinjam < jumlah yang dikembalikan
            print("Jumlah yang dikembalikan lebih banyak dari yang dipinjam!!")
            print()
    else:       #Jike role yang login bukan 'user'
        print("Hanya user yang bisa mengembalikan gadget")
    return (gadget_borrow_history,gadget_return_history,gadget_database)


