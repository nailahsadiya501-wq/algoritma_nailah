print("-PEMESANAN TIKET BIOSKOP-")

while True:
    nama = input("\nMASUKKAN NAMA PELANGGAN: ")

    print("\nJenis Tiket:")
    print("1. REGULER - Rp35.000")
    print("2. VIP - Rp50.000")
    print("3. PREMIUM - Rp75.000")

    jenis = input("Pilih jenis tiket (1/2/3): ")
    jumlah = int(input("Masukkan jumlah tiket: "))

    if jenis == "1":
        harga = 35000
        tiket = "REGULER"

    elif jenis == "2":
        harga = 50000
        tiket = "VIP"

    elif jenis == "3":
        harga = 75000
        tiket = "PREMIUM"

    else:
        harga = 0
        tiket = "Tidak tersedia"

    if harga > 0 and jumlah > 0:
        total = harga * jumlah

        if jumlah > 3:
            diskon = total * 10 / 100
        else:
            diskon = 0

        bayar = total - diskon

        print("\nSTRUK PEMESANAN")
        print("NAMA:", nama)
        print("JENIS TIKET:", tiket)
        print("JUMLAH TIKET:", jumlah)
        print("TOTAL HARGA: Rp", total)
        print("DISKON: Rp", int(diskon))
        print("TOTAL BAYAR: Rp", int(bayar))

    else:
        print("JENIS TIKET ATAU JUMLAH TIKET TIDAK VALID!")

    #perulangan pelanggan
    ulang = input("\nApakah ingin melayani pelanggan lain? (ya/tidak): ")

    if ulang == "tidak":
        print("PROGRAM SELESAI. TERIMAKASIH!")
        break

