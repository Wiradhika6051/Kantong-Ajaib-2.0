#Program Kantong Ajaib
#Program untuk memodernisasi sistem inventarisasi kantong ajaib Doraemonangis
#Kelompok 04 K-09 IF-1210 Dasar Pemrograman 
#Anggota:
#1. Fawwaz Anugrah Wiradhika Dharmasatya(16520059)
#2. Muhammad Furqan Alfuady(16529339)
#3. Muhamad Fariz Ramadhan(16520409)
#4. Kemas Ahmad Sofyan Hamdany(16520479)

#Input:username dan password,folder database
#Output:Program inventarisasi kantong ajaib dari mulai menambah,,menghapus,dan mengubah jumlah item,mendaftarkan pengguna,meminjam,mengembalikan,dan mengambil item,hingga melihat riwayat peminjaman,pengembalian,dan pengambilan item
import argparse
import save
import LoginRegister
import Help
import os
import CariGadget
import tambahitem
import load
import hapusitem
import ubahjumlah
import peminjaman
import minta
import history
import Gacha
import kembalikan
#KAMUS
#Fungsi
#F17 - EXIT
def exit(user_database,gadget_database,return_history_database,borrow_history_database,consumable_database,consumable_history_database):
# Fungsi yang menghasilkan False(menghentikan program) jika pengguna ingin keluar dari program dan menyimpan database ke folder yang diminta,selain itu True
# Kamus Lokal
# jawaban:string(jawaban untuk konfirmasi penyimpanan)
# Algoritma
    jawaban = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if(jawaban=="Y" or jawaban=="y" or jawaban=="N" or jawaban=="n"):       #Jika masukan valid
        if(jawaban=="y" or jawaban=="Y"):               #Jika pengguna ingin keluar
            save.save_data(user_database,gadget_database,return_history_database,borrow_history_database,consumable_database,consumable_history_database)
            return False
        else:
            print()
    else:#Jika masukan tidak valid
        print("Masukkan tidak valid! Masukan hanya menerima huruf 'y','Y,'n',dan'N'!")
        print()
    return True

#Variabel
#run:boolean(bernilai True jika program masih berjalan,jika bernilai False maka program berhenti)
#user:User(data mengenai user yang sedang login)
#folder_path:string(path folder penyimpanan)
#user_database:User(database user yang sudah dimuat)
#gadget_database:Gadget(database gadget yang sudah dimuat)
#consumable_database:Consumable(database consumable yang sudah dimuat)
#borrow_history_database:RiwayatPinjam(database riwayat peminjaman gadget yang sudah dimuat)
#return_history_database:RiwayatKembali(database riwayat pengembalian gadget yang sudah dimuat)
#consumable_history_database:RiwayatAmbil(database riwayat pengambilan consumable yang sudah dimuat)
#inventory:Consumable(inventori untuk gacha)
#opsi:string(command yang dimasukkan pengguna)
#logined:boolean(bernilai False jika belum login dan True jika sudah login)

#ALGORITMA PROGRAM UTAMA
run = True
logined = False
user = [0,"-","-","-","-",""]
inventory = []
folder_path = load.get_folder_path()
user_database,gadget_database,consumable_database,borrow_history_database,return_history_database,consumable_history_database = load.load(folder_path)
print('Selamat datang di "Kantong Ajaib 2.0"!')
while not logined:
    print("Masukkan command 'login' untuk melakukan login dan command 'help' untuk melihat-lihat list beberapa list command")
    opsi = input("Masukkan Perintah:")
    os.system('cls||clear')
    if(opsi=='help'):
        Help.help(user)
    elif(opsi=='login'):
        print("Silahkan masukkan identitas Anda")
        user = LoginRegister.login(user_database)
        inventory = Gacha.fill_inventory(consumable_database,consumable_history_database,user[0])
        logined = True
    else:
        print("Command tidak valid! masukkan command 'help' untuk melihat daftar command")
        print()
print()
while run:
    print("=================================================== KANTONG AJAIB 2.0 ==================================================")
    print("Inventaris kantong ajaib dengan teknologi terbaru.")
    print("Masukkan command yang ingin dijalankan pada baris dibawah ini. Masukkan command 'help' untuk melihat daftar command.")
    opsi = input("Masukkan Perintah:")
    os.system('cls||clear')
    if(opsi=="carirarity"):
        CariGadget.carirarity(gadget_database)
    elif(opsi=="caritahun"):
        CariGadget.caritahun(gadget_database)
    elif(opsi=="pinjam"):
        gadget_database,borrow_history_database = peminjaman.pinjam(user,gadget_database,borrow_history_database)
    elif(opsi=="kembalikan"):
        borrow_history_database,return_history_database,gadget_database = kembalikan.kembalikan(user,gadget_database,borrow_history_database,return_history_database)
    elif(opsi=="minta"):
        consumable_database,consumable_history_database = minta.minta(user,consumable_database,consumable_history_database)
    elif(opsi=="gacha"):
        inventory,consumable_history_database = Gacha.gacha(consumable_database,inventory,user,consumable_history_database)
    elif(opsi=="help"):
        Help.help(user)
    elif(opsi=="register"):
        user_database = LoginRegister.register(user_database,folder_path+"/user.csv",user)
    elif(opsi=="tambahitem"):
        gadget_database,consumable_database = tambahitem.tambahitem(gadget_database,consumable_database,user,folder_path,"/gadget.csv","/consumable.csv")
    elif(opsi=="hapusitem"):
        gadget_database,consumable_database = hapusitem.hapusitem(user,gadget_database,consumable_database)
    elif(opsi=="ubahjumlah"):
        gadget_database,consumable_database  = ubahjumlah.ubahjumlah(user,gadget_database,consumable_database,folder_path,"/gadget.csv","/consumable.csv")
    elif(opsi=="riwayatpinjam"):
        history.see_borrow_history(borrow_history_database,user,user_database,gadget_database,3)
    elif(opsi=="riwayatkembali"):
        history.see_return_history(return_history_database,user_database,user,gadget_database,borrow_history_database,2)
    elif(opsi=="riwayatambil"):
        history.see_take_history(consumable_history_database,user,user_database,consumable_database,3)
    elif(opsi=="save"):
        save.save_data(user_database,gadget_database,return_history_database,borrow_history_database,consumable_database,consumable_history_database)
    elif(opsi=="exit"):
        run = exit(user_database,gadget_database,return_history_database,borrow_history_database,consumable_database,consumable_history_database)
    else:
        print("Command tidak valid! masukkan command 'help' untuk melihat daftar command")
        print()

#Pesan Penutup
print("Terima kasih telah menggunakan layanan kantong ajaib ini!!")