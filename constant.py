#constant.py
#File berisi konstanta-konstanta yang dapat digunakan untuk mempermudah proses pembuatan program
#Format data tiap database
USER_FORMAT = ["id","username","nama","alamat","password","role"]
GADGET_FORMAT = ["id","nama","deskripsi","jumlah","rarity","tahun_ditemukan"]
GADGET_BORROW_HISTORY_FORMAT = ["id","id_peminjam","id_gadget","tanggal_peminjaman","jumlah","is_returned"]
GADGET_RETURN_HISTORY_FORMAT  = ["id","id_peminjaman","tanggal_pengembalian","jumlah"]
CONSUMABLE_FORMAT = ["id","nama","deskripsi","jumlah","rarity"]
CONSUMABLE_HISTORY_FORMAT = ["id","id_pengambil","id_consumable","tanggal_pengambilan","jumlah"]
#Jenis Files Eksternal yang Diperlukan
FILES = ["user.csv","gadget.csv","gadget_return_history.csv","gadget_borrow_history.csv","consumable.csv","consumable_history.csv"]