import general_function as general
import constant
import save
def tambahitem(gadget_database,consumable_database,user,file_path,gadget_path,consumable_path):
    if user[5] == "admin":
        noid = input("Masukan ID: ")
        if not(noid[0] == 'G' or noid[0] == 'C'):
            #print()
            print("Gagal menambahkan item karena ID tidak valid.")
        else:
            i = -1
            if(noid[0] == 'G'):
                i = general.search_idx(gadget_database,noid)
                """
                while((not found) and (i<general.panjang(gadget_database))):
                    if (gadget_database[i][0]== noid) : #found in csv
                        found=True
                    i+=1
                """
            elif(noid[0]=='C'):
                i = general.search_idx(consumable_database,noid)
                """
                while((not found) and (i<general.panjang(consumable_database))):
                    if (consumable_database[i][0]== noid) : #found in csv
                        found=True
                    i+=1
                """
            print()
            if i!=-1:
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                if noid[0] == 'G': #connect to gadget.csv
                    Nama = input("Masukan Nama: ")
                    Deskripsi = input("Masukan Deskripsi: ")
                    Jumlah = int(input("Masukan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if not(Rarity == 'C' or Rarity == 'B' or Rarity == 'A' or Rarity == 'S'):
                        print()
                        print("Input rarity tidak valid!")
                        return (gadget_database,consumable_database)
                        #break
                    else:
                        Tahun = int(input("Masukan tahun ditemukan: "))
                    new_entry = [noid,Nama,Deskripsi,str(Jumlah),Rarity,str(Tahun)]
                    gadget_database.append(new_entry)
                    """
                    item = ";".join(new_entry)
                    item += "\n"
                    print()  
                    #isidatabase  
                    save.isi_data(file_path+gadget_path,item,"a+")
                    """           
                    print("Item telah berhasil ditambahkan ke database")
                else: #noid[0] = 'C' -> connect to consumable.csv
                    Nama = input("Masukan Nama: ")
                    Deskripsi = input("Masukan Deskripsi: ")
                    Jumlah = int(input("Masukan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if not(Rarity == 'C' or Rarity == 'B' or Rarity == 'A' or Rarity == 'S'):
                        print()
                        print("Input rarity tidak valid!")
                        return (gadget_database,consumable_database)
                        #break
                    new_entry = [noid,Nama,Deskripsi,str(Jumlah),Rarity]
                    consumable_database.append(new_entry)
                    """
                    item = ";".join(new_entry)
                    item += "\n"
                    print()  
                    #isidatabase  
                    save.isi_data(file_path+consumable_path,item,"a+") 
                    """
                    print("Item telah berhasil ditambahkan ke database")  
    else:
       print()
       print("Hanya admin yang dapat menambah item.")
    return (gadget_database,consumable_database)
                
