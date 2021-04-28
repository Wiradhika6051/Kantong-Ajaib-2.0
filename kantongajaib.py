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
#Variabel
run = True
#sudah_login = False
user = [0,"-","-","-","-","user"]
#Main program
folder_path = load.get_folder_path()
user_database = load.import_csv(folder_path+"/user.csv")
consumable_database = load.import_csv(folder_path+"/consumable.csv")
gadget_database = load.import_csv(folder_path+"/gadget.csv")
consumable_history_database = load.import_csv(folder_path+"/consumable_history.csv")
borrow_history_database = load.import_csv(folder_path+"/gadget_borrow_history.csv")
return_history_database = load.import_csv(folder_path+"/gadget_return_history.csv")

#Preprocessing
user_database = load.preprocess_user(user_database)
gadget_database = load.preprocess_gadget(gadget_database)
consumable_database = load.preprocess_consumables(consumable_database)
#gadget_database = load.preprocess_gadget(gadget_database)
consumable_history_database = load.preprocess_borrow_history(consumable_history_database)
borrow_history_database = load.preprocess_borrow_history(borrow_history_database)
return_history_database = load.preprocess_return_history(return_history_database)
#Debug



#Program utama
print('Selamat datang di "Kantong Ajaib!"')
user = LoginRegister.login(user_database)
inventory = Gacha.fill_inventory(consumable_database,consumable_history_database,user[0])
#print(inventory)
print()
while run:
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
        jawaban = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if(jawaban=="y" or jawaban=="Y"):
            save.save_data(user_database,gadget_database,return_history_database,borrow_history_database,consumable_database,consumable_history_database)
            run = False
    #print(user_database)
    #print(consumable_database)
    #print(gadget_database)
    #print(consumable_history_database)
    #print(borrow_history_database)
    #print(return_history_database)
    #print(gadget_database,consumable_database)

