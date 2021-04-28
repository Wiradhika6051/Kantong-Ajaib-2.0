import argparse
import time
import sys
import general_function as general
import os
#Loading
def get_folder_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder",type=str,nargs="?")
    args = parser.parse_args()
    if(args.nama_folder is not None):
        print("Loading...")
        time.sleep(1)
        os.system("cls||clear")
        return args.nama_folder
    else:
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python kantongajaib.py <nama_folder>")
        sys.exit()
def import_csv(path):
    #Sumber Referensi:https://13518114.medium.com/tubes-walkthrough-1-read-data-dari-csv-tanpa-library-605a6afe92db dengan berbagai modifikasi sesuai kebutuhan
    f = open(path,"r")
    lines = f.readlines()
    lines.pop(0)
    lines = [line.replace('\n',"") for line in lines]
    datas = []
    for line in lines:
        data = general.split(line,";")
        data = [(subdata.strip()) for subdata in data]
        datas.append(data)
    return datas
def preprocess_user(databases):
    for database in databases:
        database[0] = int(database[0])
    return databases
def preprocess_gadget(databases):
    for database in databases:
        database[3] = int(database[3])
        database[5] = int(database[5])
    return databases
def preprocess_consumables(databases):
    for database in databases:
        database[3] = int(database[3])
    return databases
def preprocess_borrow_history(databases):
    for database in databases:
        database[0] = int(database[0])
        database[1] = int(database[1])
        database[4] = int(database[4])
    return databases
def preprocess_return_history(databases):
    for database in databases:
        database[0] = int(database[0])
        database[1] = int(database[1])
        database[3] = int(database[3])
    return databases
