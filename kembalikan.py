import general_function as general
import save
def kembalikan(user,gadget_database,gadget_borrow_history,gadget_return_history):
    if user[5] == "user":
        #cetak entry peminjaman (aku bikin sebisa aku ya)
        # misal A[x] = entry history peminjaman)
        n = 1
        print("Berikut adalah gadget-gadget yang dipinjam :")
        for i in range (general.panjang(gadget_borrow_history)):
            if(gadget_borrow_history[i][1]==user[0] and gadget_borrow_history[i][4]!=0):
                gadget_id = general.search_idx(gadget_database,gadget_borrow_history[i][2])
                gadget = gadget_database[gadget_id]
                print(str(n) + ".", gadget[1]+" (x"+str(gadget_borrow_history[i][4])+")")
                n+=1
            
        print() #ngasih enter
        nominjam = int(input("Masukan nomor peminjaman: "))
        tgl = input("Tanggal pengembalian: ")
        jumlah = int(input("Masukkan jumlah yang ingin dikembalikan:"))
        print()
        if(gadget_borrow_history[nominjam-1][4]-jumlah>=0):
            if(gadget_borrow_history[nominjam-1][4]==jumlah):
                gadget_borrow_history[nominjam-1][5] = "True"
            gadget_borrow_history[nominjam-1][4] -= jumlah
            gadget_id = general.search_idx(gadget_database,gadget_borrow_history[nominjam-1][2])
            gadget_database[gadget_id][3] += jumlah

            new_return_entry = [save.get_last_id(gadget_return_history)+1,str(gadget_borrow_history[nominjam-1][0]),tgl,str(jumlah)]
            gadget_return_history.append(new_return_entry)
            print("Item", gadget_database[gadget_id][1], "(x" + str(jumlah) + ")", "telah dikembalikan.")

        else: # jumlah yang dipinjam < jumlah yang dikembalikan
            print("Jumlah yang dikembalikan lebih banyak dari yang dipinjam!!")
            print()
    return (gadget_borrow_history,gadget_return_history,gadget_database)


