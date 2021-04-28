import time

chance = ['C' for i in range(6250)]+['B' for i in range(2500)]+['A' for i in range(1200)]+['S' for i in range(50)]
# DATA RARITY YANG MUNGKIN DIDAPAT (C,B,A,S)

def rand_val():
    # LCG DENGAN SEED int(time.time*1000)
    random = int(time.time()*10000)
    random = (214013*random + 2531011) % (2**32)
    return random

def load_roll():
    # SEBAGAI "LOADING SCREEN" UNTUK GACHA
    x = "Rolling"
    for i in range(4):
        if i == 3:
            print(x)
            time.sleep(0.5)     
        else:    
            print(x, end="\r")
            time.sleep(0.5)
            x += "."

def search_inv(databases,user_id):
    # MENCARI SEMUA ITEM DI INVENTORY YANG DIMILIKI SEORANG USER
    inv = []
    for database in databases:
        temp = []
        for idx in range(len(database)):
            if user_id==database[0]:
                temp.append(database[idx])
        inv.append(temp)
    for i in inv [:]:
        if i==[]: # consumable milik user lain
            inv.remove(i)
    return inv

def show(inv):
    # MENAMPILKAN INVENTORY MILIK USER
    print("==========INVENTORY==========")
    for i in range(len(inv)):
        if inv[i][2]!='0':
            print(str(i+1)+'.',inv[i][1],"(Rarity {})".format(inv[i][3]),"({})".format(inv[i][2]))
    print("=============================")    

def use_consumable(inventory,chances):
    # MENGGUNAKAN CONSUMABLES YANG DIMILIKI USER UNTEK MENAIKKAN DROP RATE
    show(inventory)
    cons = int(input("Pilih consumable yang mau digunakan: "))
    amount = int(input("Jumlah yang digunakan: "))
    if inventory[cons-1]!=[]:
        if int(inventory[cons-1][2])-amount>0:
            inventory[cons-1][2] = str(int(inventory[cons-1][2])-amount)
        else: # jika jumlah consumable yang ingin digunakan melebihi yang dipunya, yang akan digunakan adalah jumlah maksimal yang dimiliki
            amount = int(inventory[cons-1][2])
            inventory[cons-1][2] = '0'
        print('\n'+inventory[cons-1][1],"(x{})".format(amount),"ditambahkan!")
        y = get_chance(inventory[cons-1][3],amount,chances)
    else:
        if int(inventory[cons][2])-amount>0:
            inventory[cons][2] = str(int(inventory[cons-1][2])-amount)
        else:
            amount = int(inventory[cons-1][2])
            inventory[cons][2] = '0'
        print('\n'+inventory[cons][1],"(x{})".format(amount),"ditambahkan!")
        y = get_chance(inventory[cons][3],amount,chances)
    return y
    
def get_chance(rare,amt,chances):
    # MENAIKKAN DROP RATE SESUAI DENGAN RARITY CONSUMABLE YANG DIGUNAKAN
    rarelist = [['C',0.1],['B',0.15],['A',0.2],['S',5.0]]
    len_c = 0
    for i in chances:
        if i=='C':
            len_c+=1
    for i in range(len(rarelist)):
        if rare==rarelist[i][0]:
            if rare=='C' or rare=='B' or rare=='A':
                print("Chance mendapatkan rarity {}".format(rarelist[i+1][0])+" (+ {}%)".format(rarelist[i][1]*amt))
                added_rate = int(rarelist[i][1]*amt*100)
                for j in range(len_c-added_rate,len_c):
                    chances[j] = rarelist[i+1][0]
            elif rare=='S':
                print("Chance mendapatkan rarity S (+ {}%)".format(amt*5.0))
                added_rate = int(amt*5.0*100)
                for j in range(len_c-added_rate,len_c):
                    chances[j] = rarelist[i][0]
    return chances

def get_items(databases, rarity):
    # MENCARI ITEM DI DATA CONSUMABLES YANG SESUAI DENGAN RARITY YANG DI-GACHA-KAN
    items_byrare = []
    for i in databases:
        if i[4]==rarity:
            items_byrare.append(i)
    return items_byrare

# FB03 - GACHA
def gacha(consumables_database, inv_database, user):
    # MELAKUKAN GACHA UNTUK MENDAPATKAN CONSUMABLE BARU YANG *mungkin* RARITY-NYA LEBIH TINGGI
    if user[5] == "user":      
        inventory = search_inv(inv_database,str(user[0])) # user[0] dalam database user adalah user id
        y = use_consumable(inventory,chance)
        choice = input("\nTambahkan item lagi? (y/n) : ")
        while choice=='y' or choice=='Y':
            y = use_consumable(inventory,y)
            choice = input("\nTambahkan item lagi? (y/n) : ")
        print()
        load_roll()
        rarity = rand_val()%len(y[1]) # yang terlebih dahulu digacha adalah rarity
        items = get_items(consumables_database, y[rarity])
        item = items[rand_val()%len(items)][1] # lalu item dalam rarity tersebut digacha
        print("\nSelamat anda mendapatkan",item+"!(Rarity {})".format(y[rarity]))
        new_item = [user[0],item,'1',y[rarity]]
        i = 0
        j = 0
        while i<len(inventory):
            if inventory[i][0]!=inv_database[j][0]:
                j+=1
            else:
                inv_database[j] = inventory[i]
                i+=1
                j+=1  
        inv_database.append(new_item) # Menambahkan item ke inventory
