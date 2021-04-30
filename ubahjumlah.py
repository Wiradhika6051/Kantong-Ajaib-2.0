# tambahitem.py
# Folder berisi fungsi untuk melakukan pengubahan jumlah item(F07)
import general_function as general
import save
import constant

#F07 - MENGUBAH JUMLAH GADGET ATAU CONSUMABLE PADA INVENTORI
def ubahjumlah(user,gadget_database,consumable_database,file_path,gadget_path,consumable_path):
# Fungsi untuk mengubah jumlah item di database dan menghasilkan database yang telah diupdate
# Kamus Lokal
# noid:string(id item yang ingin diubah jumlahnya)
# i:integer(indeks item yang ingin diubah di database)
# database:array of Data(database yang ingin diubah) 
# Algoritma:
    noid =" "
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        i = -1
        database = []
        if(noid[0]=='G'):                                                   #Untuk gadget
            i = general.search_idx(gadget_database,noid)
            database = gadget_database
        elif(noid[0]=='C'):                                                 #Untuk consumable
            i = general.search_idx(consumable_database,noid)
            database = consumable_database
        if i==-1:                                                           #Tidak ada item dengan ID yang dicari
            print()
            print("Tidak ada item dengan ID tersebut!")
        else:                                                               #Item yang dicari ada di database
            database[i][3] = int(database[i][3])
            tambahan = int(input("Masukan jumlah yang ingin ditambahkan(untuk mengurangi jumlah,sisipkan tanda '-' di jumlah(misal -10)): "))
            if (database[i][3] + tambahan >= 0):                            #Jika jumlah akhirnya lebih besar sama dengan 0
                database[i][3] += tambahan  
                print()
                if(tambahan>=0):
                    print(tambahan, database[i][1], "berhasil ditambahkan. Stok sekarang:", database[i][3])
                else:
                    print(tambahan, database[i][1], "berhasil dibuang. Stok sekarang:", database[i][3])
                database[i][3] = str(database[i][3])
            else:                                                           #Jika jumlah akhirnya negatif
                print()
                print(tambahan, database[i][1], "gagal dibuang karena stok kurang. Stok sekarang:", database[i][3], "(<" + str(-tambahan) + ")")
    else: 
        print("Hanya admin yang dapat mengubah jumlah item.")
        print()
    if(noid[0]=="G"):                                       #Jika huruf pertama id 'G' namun item dengan id tersebut tidak ada id database gadget
        return(database,consumable_database)
    elif(noid[0]=="C"):                                     #Jika huruf pertama id 'C' namun item dengan id tersebut tidak ada id database consumable
        return(gadget_database,database)
    else:
        return(gadget_database,consumable_database)         #Jika huruf pertama id bukan 'G' atau 'C'