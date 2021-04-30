#general_function.py
#File yang berisi fungsi-fungsi yang bersifat umum dan digunakan di berbagai file program
import time
def panjang(text):
# Menghasilkan panjang dari sebuah list atau string (panjang dari semua variabel yang bisa diiterasi)
# Kamus Lokal:
# counter : integer( kounter untuk menghitung panjang sebuah variabel yang bisa diiterasi)
# i : integer (kounter loop)
# Algoritma
    counter = 0
    for i in text:
        counter += 1
    return counter

def basic_pangkat(basis,pangkat):
# Menghasilkan nilai dari (basis) dipangkatkan dengan (pangkat) (misal 2^3).
# Batasan: Nilai pangkat >=0
# Kamus Lokal:
# hasil = integer( variabel yang menyimpan hasil sementara perpangkatan )
# Algoritma
    hasil = basis
    if(pangkat==0):                                                     #Semua bilangan yang dipangkatkan 0 hasilnya 1
        return 1
    else:
        for i in range(pangkat-1):
            hasil *= basis
    return hasil

def split(line,delimiter):
# Menghasilkan list berisi data hasil parsing  line dengan setiap data pada list dipisahkan oleh <delimiter>
# Kamus Lokal:
# argument_list : array of string (Berisi data-data yang berhasil dipisahkan dari line)
# argument: string (variabel untuk menyimpan data hasil parsing dari line sebelum ditambahkan ke list argument_list)
# i:integer(kounter loop)
# Algoritma
    argument_list = []
    argument =""
    for i in range(panjang(line)):
        if(line[i]!=delimiter):
            argument += line[i]
        else:
            argument_list.append(argument)
            argument = ""
    if(argument!=""):                                               #Jika karakter terakhir bukan delimiter dan nilai argument yang sekarang belum dimasukkan,maka argument perlu dimasukkan ke list
        argument_list.append(argument)
    return argument_list

def search_idx(database,noid):
# Fungsi yang menghasilkan indeks dimana nilai id dari database sama dengan noid pertama kali ditemukan
# Kamus Lokal:
# i:integer(kounter loop)
# Algoritma
    i = 0
    while(i<panjang(database)):
        if (database[i][0]== noid) : #found in csv
            return i
        i+=1
    return -1
def max_idx(array,initial,idx,col):
# Fungsi yang menghasilkan indeks dimana nilai elemen terbesar dari indeks initial hingga elemen terakhir array
# Kamus Lokal:
# maxidx : integer (indeks dengan elemen bernilai terbesar)
# i : integer(kounter loop)
# Algoritma
    maxidx=initial
    for i in range(initial+1,panjang(array)):
        if(array[i][col][idx]>array[maxidx][col][idx]):
           maxidx = i
    return maxidx

def sorting(array,col,idx):
# Fungsi yang menghasilkan array dengan elemen terurut mengecil menggunakan selection sort
# Kamus Lokal:
# id_max : integer(indeks dengan elemen bernilai maksimum)
# i : integer(kounter loop)
# temp: array (variabel sementara untuk menyimpan array dengan elemen yang di sort bernilai terbesar)
# Algoritma
    if(panjang(array)>1):
        for i in range(panjang(array)):
            id_max = max_idx(array,i,idx,col)
            temp = array[id_max]
            array[id_max] = array[i]
            array[i] = temp
    return array

def loading_progress(pesan):        #Membuat pseudo-loading progress untuk memberikan kesan programnya sedang melakukan proses loading kepada pengguna
# I.S. Proses Loading belum dimulai
# F.S. Menampilkan pseuso-loading progress kepada pengguna
# Kamus Lokal
# i:integer(kounter loop)
# Algoritma:                  
    for i in range(4):
        if i == 3:
            print(pesan)
            time.sleep(0.5)     
        else:    
            print(pesan, end="\r")
            time.sleep(0.5)
            pesan += "."