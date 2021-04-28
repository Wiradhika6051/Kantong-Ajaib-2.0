import general_function as general
import save
def minta (user,consumable_database,consumable_history):
    if(user[5]=="user"):
        noid = input("Masukan ID item: ")
        if not(noid[0] == 'C'):
            print()
            print("Gagal meminta item karena ID tidak valid.")
        else:#if noid[0] == 'C': #connect to consumable.csv
            i = general.search_idx(consumable_database,noid)
            if(i==-1):
                print("Tidak ada item dengan id",noid+"!!")
            else:
                item = consumable_database[i]
                item[3] = int(item[3])
                Tanggal = input("Tanggal permintaan: ")
                Jumlah = int(input("Jumlah: "))
                if(Jumlah<=item[3]):
                    item[3] -= Jumlah
                    consumable_database[i] = item
                    new_consumable_entry = [str(save.get_last_id(consumable_history)+1),str(user[0]),item[0],Tanggal,str(Jumlah)]
                    consumable_history.append(new_consumable_entry)
                    print("Item",item[1],"(x"+str(Jumlah)+")","telah berhasil diambil!")
                else:
                    print("Jumlah consumable yang diminta melebihi jumlah consumable yang tersedia!!!")
    return (consumable_database,consumable_history) 