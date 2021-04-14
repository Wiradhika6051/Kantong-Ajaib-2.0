def help(user):
    print("============HELP============")
    #if(not is_login):
        #print("login - untuk melakukan login kedalam sistem")
       # pass
    if(user[5]=="admin"):
        print("register - untuk melakukan login kedalam sistem")
        print("tambahitem - untuk melakukan penambahan item")
        print("hapusitem - untuk menghapus item pada database")
        print("ubahjumlah - untuk mengubah jumlah gadget atau consumable dalam database")
        print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
        print("riwayatkembali - untuk melihat riwayat pengembalian gadget")
        print("riwayatambil - untuk melihat riwayat pengambilan consumable")
    print("carirarity - untuk mencari gadget dengan raeity tertentu")
    print("caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
    if(user[5]=="user"):
        print("pinjam - untuk meminjam gadget")
        print("kembalikan - untuk mengembalikan gadget")
        print("minta - untuk meminta consumable yang tersedia")
    print("save - untuk melakukan penyimpanan data")
    print("help - untuk mendapatkan petunjuk penggunaan command")
    print("exit - untuk keluar dari program")
