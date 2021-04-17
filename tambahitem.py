def tambahitem(user):
    if user[5] == "admin":
        noid = input("Masukan ID: ")
        if not(noid[0] == 'G' or noid[0] == 'C'):
            print()
            print("Gagal menambahkan item karena ID tidak valid.")
        else:
            if noid == : #found in csv
                print()
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
                        break
                    else:
                        Tahun = int(input("Masukan tahun ditemukan: ")
                    print()                
                    print("Item telah berhasil ditambahkan ke database")
                else: #noid[0] = 'C' -> connect to consumable.csv
                    Nama = input("Masukan Nama: ")
                    Deskripsi = input("Masukan Deskripsi: ")
                    Jumlah = int(input("Masukan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if not(Rarity == 'C' or Rarity == 'B' or Rarity == 'A' or Rarity == 'S'):
                        print()
                        print("Input rarity tidak valid!")
                        break
                    print()
                    print("Item telah berhasil ditambahkan ke database")
       else:
           print()
           print("Hanya admin yang dapat menambah item.")
                        
                
