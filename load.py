#load.py
#FIle berisi fungsi yang berhubungan dengan loading data(F14)
import argparse
import time
import sys
import general_function as general
import os


        
def get_folder_path():
# Fungsi yang menghasilkan folder path database setelah melakukan parsing command input,jika tidak ada,maka akan menampilkan pesan(Tidak ada nama folder yang diberikan!)
# Kamus Lokal:
# parser: ArgumentParser (objek untuk melakukan parsing command)
# args: Argument(List argumen hasil parsing)
# nama_folder:string(nama folder yang diperoleh dari parsing)
# Algoritma:
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder",type=str,nargs="?")
    args = parser.parse_args()
    if(args.nama_folder is not None):
        general.loading_progress("Loading")
        os.system("cls||clear")
        return args.nama_folder
    else:
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python kantongajaib.py <nama_folder>")
        sys.exit()

def import_csv(path):
# Sumber Referensi:https://13518114.medium.com/tubes-walkthrough-1-read-data-dari-csv-tanpa-library-605a6afe92db dengan berbagai modifikasi sesuai kebutuhan
# Fungsi yang mengimport csv dari path yang ada,memparsingnya,dan menghasilkan array of Data
# f: SEQFILE of string(fungsi untuk membuka data dan menyimpan hasilnya)
# lines:array of string(baris-baris hasil pembacaan csv)
# line:string(variabel kounter untuk looping)
# datas: array of Data(data hasil pembacaan dan pengolahan csv)
# subdata:string(bagian tiap elemen data yang membentuk data. Variabel ini digunakan untuk looping)
# Algoritma:
    f = open(path,"r")
    lines = f.readlines()
    lines.pop(0)
    lines = [line.replace('\n',"") for line in lines]
    datas = []
    for line in lines:
        data = general.split(line,";")                          #Note :Fungsi split ini ada realisasinya di file general_function.py dan kami tidak menggunakan fungsi split() bawaan python
        data = [(subdata.strip()) for subdata in data]
        datas.append(data)
    return datas

def preprocess_user(databases):
# Fungsi yang mengonversi kolom id pada database user menjadi integer
# Kamus Lokal:
# database:User(variabel untuk looping)
# Algoritma:
    for database in databases:
        database[0] = int(database[0])
    return databases

def preprocess_gadget(databases):
# Fungsi yang mengonversi kolom jumlah dan tahun_ditemukan pada database gadget menjadi integer
# Kamus Lokal:
# database:Gadget(variabel untuk looping)
# Algoritma:
    for database in databases:
        database[3] = int(database[3])
        database[5] = int(database[5])
    return databases

def preprocess_consumables(databases):
# Fungsi yang mengonversi kolom jumlah pada database consumable menjadi integer
# Kamus Lokal:
# database:Consumable(variabel untuk looping)
# Algoritma:
    for database in databases:
        database[3] = int(database[3])
    return databases

def preprocess_borrow_history(databases):
# Fungsi yang mengonversi kolom id,id_pengambil atau id_peminjam,dan jumlah pada database gadget_borrow_history atau consumable_history menjadi integer
# Kamus Lokal:
# database:Data(variabel untuk looping)
# Algoritma:
    for database in databases:
        database[0] = int(database[0])
        database[1] = int(database[1])
        database[4] = int(database[4])
    return databases

def preprocess_return_history(databases):
# Fungsi yang mengonversi kolom id,id_peminjaman,dan jumlah pada database gadget_return_history menjadi integer
# Kamus Lokal:
# database:RiwayatKembali(variabel untuk looping)
# Algoritma:
    for database in databases:
        database[0] = int(database[0])
        database[1] = int(database[1])
        database[3] = int(database[3])
    return databases

#F14 - LOAD DATA
def load(folder_path):                      
# Fungsi yang memuat database dalam folder_path yang ada dan menghasilkan array of Data untuk masing-masing database
# user_database:array of User(Database user)
# gadget_database:array of Gadget(database gadget)
# consumable_database:array of Consumable(database consumable)
# borrow_history_database:array of RiwayatPinjam(database peminjaman gadget)
# return_history_database:array of RiwayatKembali(database pengembalian gadget)
# consumable_history_database:array of RiwayatAmbil(database pengambilan consumable)
# Algoritma:
    user_database = import_csv(folder_path+"/user.csv")
    consumable_database = import_csv(folder_path+"/consumable.csv")
    gadget_database = import_csv(folder_path+"/gadget.csv")
    consumable_history_database = import_csv(folder_path+"/consumable_history.csv")
    borrow_history_database = import_csv(folder_path+"/gadget_borrow_history.csv")
    return_history_database = import_csv(folder_path+"/gadget_return_history.csv")
    #Preprocessing
    user_database = preprocess_user(user_database)
    gadget_database = preprocess_gadget(gadget_database)
    consumable_database = preprocess_consumables(consumable_database)
    consumable_history_database = preprocess_borrow_history(consumable_history_database)
    borrow_history_database = preprocess_borrow_history(borrow_history_database)
    return_history_database = preprocess_return_history(return_history_database)
    return(user_database,gadget_database,consumable_database,borrow_history_database,return_history_database,consumable_history_database)