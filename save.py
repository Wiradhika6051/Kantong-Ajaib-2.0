#Untuk proses loading
import os
import time
import constant
import general_function as general
#Converter
def convert_data_to_string(datas,format_):
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
def isFolderExist(path):
    #Sumber referensi:https://www.geeksforgeeks.org/os-walk-python/
    #Sumber referensi:https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    folder_path = os.path.dirname(os.path.realpath(__file__))
    for (root,dirs,files) in os.walk(folder_path,topdown=True):
        for dir_ in dirs:
            if(dir_==path):
                return True
    return False
def adaDiFolder(path,file_save):
    #Sumber referensi:https://www.geeksforgeeks.org/os-walk-python/
    for (root,dirs,files) in os.walk(path,topdown=True):
        for file_ in files:
            if(file_==file_save):
                return True
    return False

def isi_data(file_path,file_data,mode):
    f = open(file_path,mode)
    f.write(file_data)
    f.close()
#Save
#Sumber referensi:https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
def save_data(user_data,gadget_data,return_history_data,borrow_history_data,consumables_data,consumables_history_data):
    path = input("Masukkan nama folder penyimpanan:")
    print("Saving...")
    time.sleep(2)
    string_user = convert_data_to_string(user_data,constant.USER_FORMAT)
    string_gadget = convert_data_to_string(gadget_data,constant.GADGET_FORMAT)
    string_return_history = convert_data_to_string(return_history_data,constant.GADGET_RETURN_HISTORY_FORMAT)
    string_borrow_history = convert_data_to_string(borrow_history_data,constant.GADGET_BORROW_HISTORY_FORMAT)
    string_consumables = convert_data_to_string(consumables_data,constant.CONSUMABLE_FORMAT)
    string_consumables_history = convert_data_to_string(consumables_history_data,constant.CONSUMABLE_HISTORY_FORMAT)
    string_list = [string_user,string_gadget,string_return_history,string_borrow_history,string_consumables,string_consumables_history]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pemisah = '\/'
    folder_path = dir_path+pemisah[0]+path
    #Cek apakah folder sudah ada
    if(not isFolderExist(path)):#Jika folder belum ada
        os.mkdir(folder_path)
        for i in range(general.panjang(constant.FILES)):
            file_path = folder_path+pemisah[0]+constant.FILES[i]
            isi_data(file_path,string_list[i],"w")  
    else:#Jika folder sudah ada
        for i in range(general.panjang(constant.FILES)):
            file_path = folder_path+pemisah[0]+constant.FILES[i]
            if(adaDiFolder(folder_path,constant.FILES[i])):#JIka file sudah ada
                os.remove(file_path)
                isi_data(file_path,string_list[i],"w")
            else:#Jika file tidak ada,maka buat baru
                isi_data(file_path,string_list[i],"w")  
def get_last_id(database):
    #Cari last id
    last_id =-1
    for data in database:
        if(data[0]>last_id):
            last_id = data[0]
    return last_id