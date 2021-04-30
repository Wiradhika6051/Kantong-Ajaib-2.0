#save.py
#File yang berisi fungsi-fungsi yang berhubungan dengan fungsionalitas menyimpan data(F15)
import os
import time
import constant
import general_function as general
import history

#Converter
def convert_data_to_string(datas,format_):
# Fungsi yang merubah tipe Data menjadi string
# Kamus Lokal
# data_baru:string(string hasil konversi Data)
# i:integer(kounter loop)
# data:Data(variabel untuk looping)
# Algoritma:
    data_baru = ""
    for i in range(general.panjang(format_)):
        if(i!=general.panjang(format_)-1):
            data_baru = data_baru+format_[i]+";"
        else:#Elemen terakhir
            data_baru = data_baru+format_[i]+"\n"
    for data in datas:
        for i in range(general.panjang(data)):
            data_ = str(data[i])
            if(i!=general.panjang(data)-1):
                data_baru = data_baru + data_ + ";"
            else:
                data_baru = data_baru + data_ + "\n"
    return data_baru

# Sumber referensi:https://www.geeksforgeeks.org/os-walk-python/
# Sumber referensi:https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
def isFolderExist(path):
# Fungsi yang menghasilkan true jika path folder berada dalam direktori program ini,selain itu false
# Kamus Lokal
# folder_path:string(path penuh dari folder ini)
# root:string(root path dari tiap iterasi)
# dirs:array of string(array berisi daftar direktori dalam tiap root)
# files:array of string(array berisi daftar files dalam tiap root)
# dir_:string(variabel untuk looping)
# Algoritma:
    folder_path = os.path.dirname(os.path.realpath(__file__))
    for (root,dirs,files) in os.walk(folder_path,topdown=True):
        for dir_ in dirs:
            if(dir_==path):
                return True
    return False

# Sumber referensi:https://www.geeksforgeeks.org/os-walk-python/
def adaDiFolder(path,file_save):
# Fungsi yang menghasilkan true jika file_save(file penyimpanan database) berada di folder yang dispesifikasi,selain itu false
# Kamus Lokal
# root:string(root path dari tiap iterasi)
# dirs:array of string(array berisi daftar direktori dalam tiap root)
# files:array of string(array berisi daftar files dalam tiap root)
# file_:string(variabel untuk looping)
# Algoritma:
    for (root,dirs,files) in os.walk(path,topdown=True):
        for file_ in files:
            if(file_==file_save):
                return True
    return False

def isi_data(file_path,file_data,mode):
# I.S. file_path(path file penyimpanan),file_data,dan mode penyimpanan terdefinisi
# F.S. Menuliskan data pada file
# Kamus Lokal
# f:SEQFILE of string(variabel untuk membuka file)
# Algoritma
    f = open(file_path,mode)
    f.write(file_data)
    f.close()

def get_last_id(database):
# Fungsi untuk mendapatkan id terakhir(id terbesar) dalam database
# Kamus Lokal
# last_id:integer(id terbesar dalam database)
# data:Data(variabel untuk looping)
# Algoritma
    last_id =-1
    for data in database:
        if(data[0]>last_id):
            last_id = data[0]
    return last_id

#F15 - SAVE DATA
#Sumber referensi:https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
def save_data(user_data,gadget_data,return_history_data,borrow_history_data,consumables_data,consumables_history_data):
# I.S. semua database terdefinisi(user_data,gadget_data,return_history_data,borrow_history_data,consumables_data,consumables_history_data)
# F.S. semua database tersimpan di folder yang telah dispesifikasi
# Kamus Lokal
# path:string(nama folder penyimpanan)
# string_user:string(database user yang telah dikonversi menjadi string)
# string_gadget:string(database gadget yang telah dikonversi menjadi string)
# string_consumables:string(database consumable yang telah dikonversi menjadi string)
# string_borrow_history:string(database riwayat peminjaman gadget yang telah dikonversi menjadi string)
# string_return_history:string(database riwayat pengembalian gadget yang telah dikonversi menjadi string)
# string_consumables_history:string(database riwayat pengambilan consumable yang telah dikonversi menjadi string)
# string_list:array of string(array berisi string tiap database)
# dir_path:string(path untuk direktori penyimpanan folder)
# folder_path:string(path folder)
# i:integer(kounter loop)
# file_path:string(path penyimpanan file)
# Algoritma:
    path = input("Masukkan nama folder penyimpanan:")
    if(general.panjang(path)==0):#Jika user tidak memasukkan input folder penyimpanan
        print("Penyimpanan gagal. Anda perlu memasukkan folder penyimpanan!!!")
        print()
        return
    general.loading_progress("Saving")
    #Sort histori agar terurut descending(tetap ada sorting di bagian melihat riwayat karena ada kasus entri riwayat ditambah sebelum disimpan)
    borrow_history_data = history.process_history(borrow_history_data,3)
    return_history_data = history.process_history(return_history_data,2)
    consumables_history_data = history.process_history(consumables_history_data,3)
    #Konersi ke string
    string_user = convert_data_to_string(user_data,constant.USER_FORMAT)
    string_gadget = convert_data_to_string(gadget_data,constant.GADGET_FORMAT)
    string_return_history = convert_data_to_string(return_history_data,constant.GADGET_RETURN_HISTORY_FORMAT)
    string_borrow_history = convert_data_to_string(borrow_history_data,constant.GADGET_BORROW_HISTORY_FORMAT)
    string_consumables = convert_data_to_string(consumables_data,constant.CONSUMABLE_FORMAT)
    string_consumables_history = convert_data_to_string(consumables_history_data,constant.CONSUMABLE_HISTORY_FORMAT)
    string_list = [string_user,string_gadget,string_return_history,string_borrow_history,string_consumables,string_consumables_history]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder_path = dir_path+"\\"+path
    #Cek apakah folder sudah ada
    if(not isFolderExist(path)):                #Jika folder belum ada
        os.mkdir(folder_path)
        for i in range(general.panjang(constant.FILES)):
            file_path = folder_path+"\\"+constant.FILES[i]
            isi_data(file_path,string_list[i],"w")  
    else:                                       #Jika folder sudah ada
        for i in range(general.panjang(constant.FILES)):
            file_path = folder_path+"\\"+constant.FILES[i]
            if(adaDiFolder(folder_path,constant.FILES[i])):#JIka file sudah ada
                os.remove(file_path)
                isi_data(file_path,string_list[i],"w")
            else:#Jika file tidak ada,maka buat baru
                isi_data(file_path,string_list[i],"w")  
    print("Data telah disimpan pada folder "+path+"!")
