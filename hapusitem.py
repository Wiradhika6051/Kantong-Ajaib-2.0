import general_function as general
def hapusitem(user,gadget_database,consumable_database):
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        # Cek kolom csv ke (noid) kosong atau nggak -> csv sesuai dulu apakah gadget.csv atau consumable.csv
        #found = False
        i = -1
        data = []
        item_type = ""
        if(noid[0] == 'G'):
            i = general.search_idx(gadget_database,noid)
            data = gadget_database[i]
            item_type = "gadget"
            """
            while((not found) and (i<general.panjang(gadget_database))):
                if (gadget_database[i][0]== noid) : #found in csv
                    #found=True
                    data = gadget_database[i]
                    item_type = "gadget"
                i+=1
            """
        elif(noid[0]=='C'):
            i = general.search_idx(consumable_database,noid)
            data = consumable_database[i]
            item_type = "consumable"
            """
            while((not found) and (i<general.panjang(consumable_database))):
                if (consumable_database[i][0]== noid) : #found in csv
                    found=True
                    data = consumable_database[i]
                    item_type = "consumable"
                i+=1
        while((not found) and (i<general.panjang(gadget_database) and (i<general.panjang(consumable_database)))):
            if (gadget_database[i][0]== noid) : #found in csv
                found=True
                data = gadget_database[i]
                item_type = "gadget"
            elif(consumable_database[i][0]==noid):
                found = True
                data = consumable_database[i]
                item_type = "consumable"
            i+=1
            """
        #if database.[noid] = None 
        if i==-1:
            print("Tidak ada item dengan ID tersebut")
        else: #database.[noid] nya ada, ga None
            yakin = input("Apakah anda yakin ingin menghapus "+data[1]+" (Y/N)?")
            while not(yakin == 'Y' or yakin == 'N'):
                print("Jawaban harus Y atau N")
                yakin = input("Apakah anda yakin ingin menghapus "+data[1]+" (Y/N)?")
            if yakin == 'Y':
                if(item_type=="gadget"):
                    #del.kolom ke-x database tersebut!!
                    gadget_database.pop(i)
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    consumable_database.pop(i)
                    print()
                    print("Item telah berhasil dihapus dari database.")
            else: #yakin == 'N'
                print()
                print("Item gagal dihapus dari database.")
    else:
        print()
        print("Hanya admin yang dapat menghapus item.")
    return (gadget_database,consumable_database)
#HARUS DI SAVE
#Belom tau implementasinya
    
                          
            
        
