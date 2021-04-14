import argparse
import SaveLoad
import LoginRegister
import Help
#Variabel
run = True
#sudah_login = False
user = [0,"-","-","-","-","user"]
#Main program
folder_path = SaveLoad.get_folder_path()
user_database = SaveLoad.import_csv(folder_path+"/user.csv")
consumable_database = SaveLoad.import_csv(folder_path+"/consumable.csv")
gadget_database = SaveLoad.import_csv(folder_path+"/gadget.csv")
consumable_history_database = SaveLoad.import_csv(folder_path+"/consumable_history.csv")
borrow_history_database = SaveLoad.import_csv(folder_path+"/gadget_borrow_history.csv")
return_history_database = SaveLoad.import_csv(folder_path+"/gadget_return_history.csv")
#Preprocessing
consumable_database = SaveLoad.preprocess_consumables(consumable_database)
gadget_database = SaveLoad.preprocess_gadget(gadget_database)
consumable_history_database = SaveLoad.preprocess_history(consumable_history_database)
borrow_history_database = SaveLoad.preprocess_history(borrow_history_database)
return_history_database = SaveLoad.preprocess_history(return_history_database)
#Program utama

print('Selamat datang di "Kantong Ajaib!"')
user = LoginRegister.login(user_database)
while run:
    opsi = input()
    if(opsi=="help"):
        Help.help(user)
    elif(opsi=="register"):
        LoginRegister.register(user_database,folder_path+"/user.csv")
    elif(opsi=="save"):
        SaveLoad.save_data()
    elif(opsi=="exit"):
        jawaban = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if(jawaban=="y" or jawaban=="Y"):
            SaveLoad.save_data()
            run = False
#Debug
"""
print(user_database)
print(consumable_database)
print(gadget_database)
print(consumable_history_database)
print(borrow_history_database)
print(return_history_database)
"""