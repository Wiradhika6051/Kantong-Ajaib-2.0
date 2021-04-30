#Help.py
#File yang berisi fungsi yang berhubungan untuk menampilkan pesan bantuan ke pengguna(F16)

#F16 - HELP
def help(user):
# I.S. user(list berisi informasi tentang user yang sudah login) terdefinisi
# F.S. Menampilkan pesan bantuan ke pengguna sesuai role user
#Kamus Lokal
#-
#Algoritma
    print("============HELP============")
    if(user[5]==""):                                                                        #Jika role nya kosong(belum login)
        print("login - untuk melakukan login ke dalam sistem")
    if(user[5]=="admin" or user[5]==""):                                                                   #Jika user memiliki role "admin" atau user belum login
        print("register - untuk melakukan registrasi user baru")
        print("tambahitem - untuk melakukan penambahan item")
        print("hapusitem - untuk menghapus item pada database")
        print("ubahjumlah - untuk mengubah jumlah gadget atau consumable dalam database")
        print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
        print("riwayatkembali - untuk melihat riwayat pengembalian gadget")
        print("riwayatambil - untuk melihat riwayat pengambilan consumable")
    print("carirarity - untuk mencari gadget dengan rarity tertentu")
    print("caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
    if(user[5]=="user" or user[5]==""):                                                                    #Jika user memiliki role "user" atau user belum login
        print("pinjam - untuk meminjam gadget")
        print("kembalikan - untuk mengembalikan gadget")
        print("minta - untuk meminta consumable yang tersedia")
        print("gacha - untuk melakukan combine consumable")
    print("save - untuk melakukan penyimpanan data")
    print("help - untuk mendapatkan petunjuk penggunaan command")
    print("exit - untuk keluar dari program")
    print()
