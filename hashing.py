def panjang(text):
    counter = 0
    for i in text:
        counter += 1
    return counter
def basic_pangkat(basis,pangkat):
    hasil = basis
    if(pangkat==0):
        return 1
    else:
        for i in range(pangkat-1):
            hasil *= basis
    return hasil
def hashing(text):
    first_char = text[0]
    string = ""
    iteration = 0
    count_ascii =0
    for char in text:
        string += str(ord(char)+basic_pangkat(2,iteration))
        iteration += 1
        count_ascii += ord(char)
    string = str(int(string) % 100000000) # Menghasilkan hash berisi 8 digit
    initial = 0
    while(panjang(string)<8):
        string += str((initial+count_ascii)%10)
        initial += ord(first_char)
    hash_text=""
    pengacak = panjang(string) + ord(first_char)+count_ascii
    for i in range(panjang(string)):
        if(i%2==0):
            hash_text += str((int(string[i])+((i+1)*pengacak))%10)
        else:
            hash_text += chr(64+(int(string[i])+64+(2*pengacak))%59) 
        pengacak += count_ascii

    return hash_text