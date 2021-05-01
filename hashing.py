#hashing.py
#File yang berisi fungsi untuk melakukan hashing(FB01)
import general_function as general
#FB01 - HASHING
def hashing(text):
#Fungsi yang menghasilkan nilai hashing berupa 16 digit kombinasi angka dan karakter dari text
#Kamus Lokal:
#first_char : char (character pertama pada text)
#string: string( string awal berisi text yang sudah diubah menjadi hash yang masih mentah(masih berupa full angka))
#iteration : integer(menghitung jumlah iterasi saat konversi text menjadi hash mentah)
#count_ascii: integer(total nilai ascii dari semua karakter di text)
#char : char(kounter loop saat melakukan konversi text jadi hash mentah)
#initial: integer(komponen faktor "pengacak" hash yang berupa character pertama pada text)
#pengacak : integer (faktor "pengacak" utama pada hash agar hasil hashing semakin acak dan perubahan 1 karakter bisa merubah hash secara siginifikan)
#i : integer (kounter loop untuk bagian terakhir hashing)
#hash_text : string(nilai hash dari text)
#Algoritma
    first_char = text[0]
    string = ""
    iteration = 0
    count_ascii =0
    for char in text:
        string += str(ord(char)+general.basic_pangkat(2,iteration))
        iteration += 1
        count_ascii += ord(char)
    string = str(int(string) % general.basic_pangkat(10, 16))
    initial = 0
    while(general.panjang(string)<16):
        string += str((initial+count_ascii)%10)
        initial += ord(first_char)
    hash_text=""
    pengacak = general.panjang(string) + ord(first_char)+count_ascii
    for i in range(general.panjang(string)):
        if(i%2==0):
            hash_text += str((int(string[i])+((i+1)*pengacak))%10)
        else:
            hash_text += chr(64+(int(string[i])+64+(2*pengacak))%59) 
        pengacak += count_ascii
    return hash_text

