#LoginRegister.py
# File berisi fungsi-fungsi yang berhubungan dengan kegiatan login dan register(F01 dan F02)
import hashing
import save


def adaDiDatabase(datas,elemen,i):
# Fungsi yang menghasilkan nilai True jika entri dengan elemen "elemen" ada di database,selain itu False
# Kamus Lokal:
# data:User(variabel untuk looping)
# Algoritma:
    for data in datas:
        if(data[i]==elemen):
            return True
    return False


def valid(username,password,database):
# Fungsi yang menghasilkan True jika input login valid(nilai username dan password yang diinput sama dengan nilai username dan password di database),selain itu False
# Kamus Lokal:
# data: User(variabel untuk looping)
# Algoritma:
    for data in database:
        if(data[1]==username and data[4]==password):
            return True
    return False

def get_user(username,password,database):
# Fungsi yang menghasilkan data user yang diminta dari database
# Kamus Lokal:
# data:User(variabel untuk looping)
# Algoritma:
    for data in database:
        if(data[1]==username and data[4]==password):
            return data

#F01 - REGISTER
def register(database,logined_user):
# Fungsi untuk mendaftarkan user baru ke entri di database user. Hanya bisa dilakukan oleh admin
# Kamus Lokal:
# nama:string(nama user yang ingin dimasukkan)
# username:string(username user yang ingin dimasukkan)
# password:string(password user yang ingin dimasukkan)
# alamat:string(alamat user yang ingin dimasukkan)
# last_id:integer(id_terakhir di entri database user.Berguna untuk menulisakan id user yang baru)
# new_entry:User(data user yang ingin dimasukkan)
# Algoritma
    if(logined_user[5]=="admin"):
        nama = input("Masukan nama:")
        username = input("Masukan username:")
        while(adaDiDatabase(database,username,1)):        #Validasi sampai username unik
            print("Username anda harus unik!!!")
            username = input("Masukan username:")
        password = input("Masukan password:")
        while(adaDiDatabase(database,hashing.hashing(password),4)):        #Validasi sampai password unik
            print("Password anda harus unik!!!")
            password = input("Masukan password:")
        alamat = input("Masukan alamat:")
        #Cari last id
        last_id = save.get_last_id(database)
        new_entry = [str(last_id+1),username,nama.title(),alamat,hashing.hashing(password),"user"]
        database.append(new_entry)
        print("User",username,"telah berhasil register ke dalam Kantong Ajaib.")
        return database
    else:
        print("Akses ditolak. Anda bukan admin!!!")
        return database

#F02 - LOGIN
def login(datas):
# Fungsi untuk melakukan mekanisme login dan menghasilkan data user yang berhasil login
# Kamus Lokal:
# username:string(usernam yang dimasukkan pengguna)
# password:string(password yang dimasukkan pengguna)
# logined_user:User(data mengenai user yang berhasil login)
    username = input("Masukan username:")
    password = input("Masukan password:")
    while(not valid(username,hashing.hashing(password),datas)):
        print("Tidak ada akun!!")
        username = input("Masukan username:")
        password = input("Masukan password:")
    print("Halo "+username+"! Selamat Datang di Kantong Ajaib.")
    logined_user = get_user(username,hashing.hashing(password),datas)
    return logined_user

