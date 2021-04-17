def hapusitem(user):
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        # Cek kolom csv ke (noid) kosong atau nggak -> csv sesuai dulu apakah gadget.csv atau consumable.csv
        if database.[noid] = None 
            print("Tidak ada item dengan ID tersebut")
        else: #database.[noid] nya ada, ga None
            yakin = input("Apakah anda yakin ingin menghapus", Nama, " (Y/N)?")
            while not(yakin = 'Y' or yakin = 'N'):
                print("Jawaban harus Y atau N")
                yakin = input("Apakah anda yakin ingin menghapus", Nama, " (Y/N)?")
            if yakin == 'Y':
                #del.kolom ke-x database tersebut!!
                print()
                print("Item telah berhasil dihapus dari database.")
            else: #yakin == 'N'
                print()
                print("Item gagal dihapus dari database.")
    else:
        print()
        print("Hanya admin yang dapat menghapus item.")
            
#HARUS DI SAVE
#Belom tau implementasinya
                          
            
        
