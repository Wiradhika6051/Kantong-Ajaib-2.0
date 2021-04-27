def kembalikan(user):
    if user[5] = "user":
        #cetak entry peminjaman (aku bikin sebisa aku ya)
        # misal A[x] = entry history peminjaman)
        print("Berikut adalah gadget-gadget yang dipinjam :")
        for i in range (1, length(A)+1):
            print(i + ".", A[i])
            
        print() #ngasih enter
        nominjam = int(input("Masukan nomor peminjaman: "))
        tgl = input("Tanggal pengembalian: ")
        
        print()
        print("Item", A[nominjam], "(x" + A[nominjam].jumlah + ")", "telah dikembalikan.")
        #terus delete si A[nominjam] dari entry peminjaman terus sort lagi entry)
        delete(A[nominjam]) from A
        sort(A) based on abjad #biar gampang yeah
