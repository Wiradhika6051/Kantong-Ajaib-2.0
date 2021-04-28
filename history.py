import general_function as general
def convert_to_date(string):
    #print(int(string[0:2]),int(string[3:5]),int(string[6:]))
    return [int(string[0:2]),int(string[3:5]),int(string[6:])]
def convert_to_string(date):
    if(date[0]<10):
        date[0] = "0" + str(date[0])
    else:
        date[0] = str(date[0])
    if(date[1]<10):
        date[1] = "0" + str(date[1])
    else:
        date[1] = str(date[1])
    return date[0]+"/"+date[1]+"/"+str(date[2])
def sort_by_x(array,x,col):
    if(general.panjang(array)>1):
        i=0
        new_array = []
        same_after_x_value = []
        after_x_value = array[i][col][x+1]
        while(i<general.panjang(array)):
            last = False
            while(array[i][col][x+1]==after_x_value and not(last)):
                same_after_x_value.append(array[i])
                if(i+1==general.panjang(array)):
                    last = True
                else:
                    i+=1
            same_after_x_value = general.sorting(same_after_x_value,col,x)
            for date in same_after_x_value:
                new_array.append(date)
            same_after_x_value = []
            if( not last):
                same_after_x_value = [array[i]]
                after_x_value = array[i][col][x+1]
            if(last or i+1 ==general.panjang(array)):
                for date in same_after_x_value:
                    new_array.append(date)
            i+=1
    else:
        new_array = array
    return new_array

def sort_date(date_array,col):
    date_array = general.sorting(date_array,col,2)#Sorting tahun
    #print(date_array)
    date_array = sort_by_x(date_array,1,col)#Sorting bulan
    #print(date_array)
    date_array = sort_by_x(date_array,0,col)#Sorting hari
    #print(date_array)
    return date_array
def search_item(database,id_):
    for data in database:
        if(data[0]==id_):
            return data
def see_borrow_history(database,user,user_database,gadget_database,date_idx):
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            user =search_item(user_database,database[i][1])
            item = search_item(gadget_database, database[i][2])       
            print("ID Peminjaman:        "+str(database[i][0]))
            print("Nama Pengambil:       "+user[2])
            print("Nama Gadget:          "+item[1])
            print("Tanggal Peminjaman:   "+database[i][3])
            print("Jumlah:               "+str(database[i][4]))
            if(database[i][5]=="False"):
                print("Status:               Masih dalam peminjaman")
            else: # Sudah dikembalikan seluruhnya
                print("Status:               Sudah dikembalikan seluruhnya")
            print()                   
            i+=1
            if(i%5==0):
                jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                if(jawaban=='n'):
                    lanjut = False
                if(i==general.panjang(database)):
                    print("Tidak ada lagi entri yang ditemukan!!")
    else: #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
def see_take_history(database,user,user_database,consumable_database,date_idx):
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            user =search_item(user_database,database[i][1])
            item = search_item(consumable_database, database[i][2])  
            print("ID Peminjaman:        "+str(database[i][0]))
            print("Nama Pengambil:       "+user[2])
            print("Nama Consumable:      "+item[1])
            print("Tanggal Pengambilan:  "+database[i][3])
            print("Jumlah:               "+str(database[i][4]))
            print()            
            i+=1
            if(i%5==0):
                jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                if(jawaban=='n'):
                    lanjut = False
                if(i==general.panjang(database)):
                    print("Tidak ada lagi entri yang ditemukan!!")
    else: #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
def see_return_history(database,user_database,user,gadget_database,borrow_database,date_idx):
    if(user[5]=="admin"):
        database = process_history(database,date_idx)
        lanjut = True
        i = 0
        while lanjut and i<general.panjang(database):
            borrow_id = general.search_idx(borrow_database, database[i][1])
            borrow_entry = borrow_database[borrow_id]
            user =search_item(user_database,borrow_entry[1])
            item = search_item(gadget_database, borrow_entry[2])    
            print("ID Pengembalian:      "+str(database[i][0]))
            print("Nama Pengambil:       "+user[2])
            print("Nama Gadget:          "+item[1])
            print("Tanggal Peminjaman:   "+database[i][2])
            print("Jumlah:               "+str(database[i][3]))
            print()
            i+=1
            if(i%5==0):
                jawaban = input("Apakah Anda ingin melihat 5 entri berikutnya?(y/n)")
                if(jawaban=='n'):
                    lanjut = False   
                if(i==general.panjang(database)):
                    print("Tidak ada lagi entri yang ditemukan!!")
    else: #role adalah "user"
        print("Akses ditolak!! Anda bukan admin")
def process_history(database,date_idx):
    temp_arr = database
    for data in database:
        data[date_idx] = convert_to_date(data[date_idx])
    #print(temp_arr)
#print(temp_arr)
    temp_arr = sort_date(temp_arr,date_idx)
    for data in temp_arr:
        data[date_idx] = convert_to_string(data[date_idx])
    #print(temp_arr)
    return temp_arr


#temp_arr = [[1,"01/01/1904"],[2,"02/02/6789"],[2,"01/02/6789"]]
#see_history(temp_arr, 1)
"""
for data in temp_arr:
    data[1] = convert_to_date(data[1])
#print(temp_arr)
temp_arr = sort_date(temp_arr,1)
for data in temp_arr:
    data[1] = convert_to_string(data[1])
print(temp_arr)
"""