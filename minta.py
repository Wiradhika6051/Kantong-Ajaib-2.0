#minta.py
#Fiel yang berisi fungsi untuk meminta consumable(F10)

import general_function as general
import save

#F10 - MEMINTA CONSUMABLE
def minta (user,consumable_database,consumable_history):
# Fungsi untuk melakukan pengambilan  consumable dan menghasilkan database consumable_database dan consumable_history yang telah diupdate
# Kamus Lokal:
# noid:string(id consumable yang ingin diambil)
# i:integer(indeks consumable tersebut dalam database consumable)
# item:Consumable(data mengenai consumable yang ingin diminta)
# Tanggal:string(tanggal pengambilan consumable)
# Jumlah:integer(jumlah consumable yang diambil)
# new_consumable_entry:RiwayatAmbil(entri riwayat pengambilan consumable yang baru diambil)
# Algoritma:
    if(user[5]=="user"):
        noid = input("Masukan ID item: ")
        if not(noid[0] == 'C'):
            print("Gagal meminta item karena ID tidak valid.")
            print()
        else:    #Jika karakter pertama pada noid bukan 'C' (bisa 'G' atau karakter lain.Jika berupa karakter lain,maka otomatis tidak akan ada entri dengan id tersebut)
            i = general.search_idx(consumable_database,noid)
            if(i==-1):
                print("Tidak ada item dengan id",noid+"!!")
                print()
            else:
                item = consumable_database[i]
                item[3] = int(item[3])
                if(item[3]==0): #Jika stok consumable adalah 0
                    print("Stok consumable sedang kosong!! Anda tidak bisa meminta consumable ini.")
                    print()
                else:           #Jika stok tidak kosong
                    Jumlah = int(input("Jumlah: "))
                    if(Jumlah>item[3]):                                                                     #Jika yang diminta melebihi yang tersedia
                        print("Jumlah consumable yang diminta melebihi jumlah consumable yang tersedia!!!")
                        print()
                        return (consumable_database,consumable_history) 
                    Tanggal = input("Tanggal permintaan: ")
                    item[3] -= Jumlah
                    consumable_database[i] = item
                    new_consumable_entry = [save.get_last_id(consumable_history)+1,user[0],item[0],Tanggal,Jumlah]
                    consumable_history.append(new_consumable_entry)
                    print("Item",item[1],"(x"+str(Jumlah)+")","telah berhasil diambil!")
                    print()
                        
    else:       #Jike role yang login bukan 'user'
        print("Hanya user yang bisa meminta consumable")    
    return (consumable_database,consumable_history) 