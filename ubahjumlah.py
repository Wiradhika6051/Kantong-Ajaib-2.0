import general_function as general
import save
import constant
def ubahjumlah(user,gadget_database,consumable_database,file_path,gadget_path,consumable_path):
    noid = ""
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        # Cek kolom csv ke (noid) kosong atau nggak -> csv sesuai dulu apakah gadget.csv atau consumable.csv
        #found = False
        i = -1
        database = []
        if(noid[0]=='G'):
            i = general.search_idx(gadget_database,noid)
            database = gadget_database
            """
            while((not found) and (i<general.panjang(gadget_database))):
                if (gadget_database[i][0]== noid ) : #found in csv
                    found=True
                i+=1
            """
        elif(noid[0]=='C'):#Untuk consumable
            i = general.search_idx(consumable_database,noid)
            database = consumable_database
            """
            while((not found) and (i<general.panjang(consumable_database))):
                if (consumable_database[i][0]== noid ) : #found in csv
                    found=True
                i+=1
            """
        #if not found:
        if i==-1:
            print()
            print("Tidak ada item dengan ID tersebut!")
        else: #database.[noid] nya ada, ga None
            database[i][3] = int(database[i][3])
            print("Jumlah", database[i][1] ,"saat ini adalah", database[i][3]) #(biar lebih jelas) ini ngide aja, gaada di spesifikasinya
            tambahan = int(input("Masukan jumlah yang ingin ditambahkan: "))
            if (database[i][3] + tambahan >= 0):
                database[i][3] += tambahan
                print()
                if(tambahan>=0):
                    print(tambahan, database[i][1], "berhasil ditambahkan. Stok sekarang:", database[i][3])
                else:
                    print(tambahan, database[i][1], "berhasil dibuang. Stok sekarang:", database[i][3])
                database[i][3] = str(database[i][3])
            else: #database.jumlah.[noid] + tambahan < 0
                print()
                print(tambahan, database[i][1], "gagal dibuang karena stok kurang. Stok sekarang:", database[i][3], "(<" + str(-tambahan) + ")")
    else: 
        print()
        print("Hanya admin yang dapat mengubah jumlah item.")
    #print(database)
    if(noid[0]=="G"):
        #string_database = save.convert_data_to_string(database, constant.GADGET_FORMAT)
        #print(string_database+"gdhgdwedwe")
        #save.isi_data(file_path+gadget_path,string_database,"w")
        return(database,consumable_database)
    elif(noid[0]=="C"):
        #string_database = save.convert_data_to_string(database, constant.CONSUMABLE_FORMAT)
        #save.isi_data(file_path+consumable_path,string_database,"w")
        return(gadget_database,database)
    else:
        return(gadget_database,consumable_database)