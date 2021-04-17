def ubahjumlah(user):
    if user[5] == "admin":
        noid = input("Masukan ID item: ")
        # Cek kolom csv ke (noid) kosong atau nggak -> csv sesuai dulu apakah gadget.csv atau consumable.csv
        if database.[noid] = None
            print()
            print("Tidak ada item dengan ID tersebut!")
        else: #database.[noid] nya ada, ga None
            print("Jumlah", database.Nama.[noid] ,"saat ini adalah", database.jumlah.[noid]) #(biar lebih jelas) ini ngide aja, gaada di spesifikasinya
            tambahan = int(input("Masukan jumlah yang ingin ditambahkan: "))
            if (database.jumlah.[noid] + tambahan >= 0):
                database.jumlah.[noid] += tambahan
                print()
                print(tambahan, database.Nama.[noid], "berhasil ditambahkan. Stok sekarang:", database.jumlah.[noid])
            else: #database.jumlah.[noid] + tambahan < 0
                print()
                print(tambahan, database.Nama.[noid], "berhasil ditambahkan. Stok sekarang:", database.jumlah.[noid], "(<" , tambahan + ")")
    else: 
        print()
        print("Hanya admin yang dapat mengubah jumlah item.")
