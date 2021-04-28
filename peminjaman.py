import general_function as general
import save
def pinjam (user,gadget_database,gadget_borrow_history):
    if(user[5]=="user"):
        noid = input("Masukan ID item: ")
        if not(noid[0] == 'G'):
            print()
            print("Gagal meminjam item karena ID tidak valid.")
        else:#if noid[0] == 'G': #connect to gadget.csv
            i = general.search_idx(gadget_database,noid)
            if(i==-1):
                print("Tidak ada item dengan id",noid+"!!")
            else:
                item = gadget_database[i]
                item[3] = int(item[3])
                Tanggal = input("Tanggal peminjaman: ")
                Jumlah = int(input("Jumlah peminjaman: "))
                if(Jumlah<=item[3]):
                    item[3] -= Jumlah
                    gadget_database[i] = item
                    new_borrow_entry = [save.get_last_id(gadget_borrow_history)+1,str(user[0]),item[0],Tanggal,str(Jumlah),"False"]
                    gadget_borrow_history.append(new_borrow_entry)
                    print("Item",item[1],"(x"+str(Jumlah)+")","berhasil dipinjam")
                else:
                    print("Jumlah gadget yang dipinjam melebihi jumlah gadget yang tersedia!!!")
    return (gadget_database,gadget_borrow_history)