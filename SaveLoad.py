#Untuk proses loading
import argparse
import sys
import time
def get_folder_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder",type=str,nargs="?")
    args = parser.parse_args()
    if(args.nama_folder is not None):
        print("Loading...")
        time.sleep(3)
        return args.nama_folder
    else:
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python kantongajaib.py <nama_folder>")
        sys.exit()
def import_csv(path):
    f = open(path,"r")
    lines = f.readlines()
    lines.pop(0)
    lines = [line.replace('\n',"") for line in lines]
    datas = []
    for line in lines:
        data = line.split(";")
        data = [(subdata.strip()) for subdata in data]
        data[0] = int(data[0])
        datas.append(data)
    return datas
def preprocess_consumables(databases):
    for database in databases:
        database[3] = int(database[3])
        database[4] = int(database[4])
def preprocess_gadget(databases):
    for database in databases:
        database[3] = int(database[3])
        database[4] = int(database[4])
        database[5] = int(database[5])
def preprocess_history(databases):
    for database in databases:
        database[1] = int(database[1])
        database[2] = int(database[2])
        database[3] = int(database[3])
#Save
def save_data():
    pass