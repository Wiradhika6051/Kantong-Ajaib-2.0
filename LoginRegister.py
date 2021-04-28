import hashing
import save
def register(database,user_data_file,logined_user):
    if(logined_user[5]=="admin"):
        nama = input("Masukan nama:")
        username = input("Masukan username:")
        while(adaDiDatabase(database,username)):
            print("Username anda harus unik!!!")
            username = input("Masukan username:")
        password = input("Masukan password:")
        alamat = input("Masukan alamat:")
        #Cari last id
        last_id = save.get_last_id(database)
        new_entry = [str(last_id+1),username,nama.title(),alamat,password,"user"]
        #new_entry = isiDatabase(last_id,nama.title(),username,hashing.hashing(password),alamat,user_data_file)
        #print(new_entry)
        database.append(new_entry)
        # print(database)
        print("User",username,"telah berhasil register ke dalam Kantong Ajaib.")
        return database
    else:
        print("Akses ditolak. Anda bukan admin!!!")
def adaDiDatabase(datas,username):
    for data in datas:
        if(data[1]==username):
            return True
    return False
    """
def isiDatabase(user_id,name,username,password,alamat,file_path):
    data_baru = ";".join([str(user_id+1),username,name,alamat,password,"user\n"])
    save.isi_data(file_path,data_baru,"a+")
    return [str(user_id+1),username,name,alamat,password,"user"]
    """
def valid(username,password,database):
    for data in database:
        if(data[1]==username and data[4]==password):
            return True
    return False
def get_user(username,password,database):
    for data in database:
        if(data[1]==username and data[4]==password):
            return data
def login(datas):
    username = input("Masukan username:")
    password = input("Masukan password:")
    while(not valid(username,hashing.hashing(password),datas)):
        print("Tidak ada akun!!")
        username = input("Masukan username:")
        password = input("Masukan password:")
    print("Halo "+username+"! Selamat Datang di Kantong Ajaib.")
    logined_user = get_user(username,hashing.hashing(password),datas)
    return logined_user

