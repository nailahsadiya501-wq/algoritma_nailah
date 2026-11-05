print("=== RUMAH MAKAN TARISHA  ===")

total = 0

while True:
    print("\n=== MENU MAKANAN ===")
    print("1. Pizza kering - Rp25000")
    print("2. Taican manis - Rp15000")
    print("3. Nasi goreng daun - Rp20000")
    print("4. Sweet spagheti - Rp30000")
    print("5. Bakso jerman - Rp18000")
    print("0. Selesai")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        jumlah = int(input("Jumlah pesanan: "))
        subtotal = 25000 * jumlah
        total = total + subtotal
        print("Subtotal: Rp", subtotal)

    elif pilihan == "2":
        jumlah = int(input("Jumlah pesanan: "))
        subtotal = 15000 * jumlah
        total = total + subtotal
        print("Subtotal: Rp", subtotal)

    elif pilihan == "3":
        jumlah = int(input("Jumlah pesanan: "))
        subtotal = 20000 * jumlah
        total = total + subtotal
        print("Subtotal: Rp", subtotal)

    elif pilihan == "4":
        jumlah = int(input("Jumlah pesanan: "))
        subtotal = 30000 * jumlah
        total = total + subtotal
        print("Subtotal: Rp", subtotal)

    elif pilihan == "5":
        jumlah = int(input("Jumlah pesanan: "))
        subtotal = 18000 * jumlah
        total = total + subtotal
        print("Subtotal: Rp", subtotal)

    elif pilihan == "0":
        print("\n=== STRUK PEMBAYARAN ===")
        print("Total Belanja: Rp", total)

        if total > 200000:
            diskon = total * 20 / 100
            print("Diskon 20%: Rp", diskon)
        else:
            diskon = 0
            print("Tidak mendapat diskon")

        print("Total Bayar: Rp", total - diskon)
        print("Terima Kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")

        #Masukkan angka 1-5 untuk memilih pesanan
        #Masukkan angka 0 untuk mengakhiri pesanan