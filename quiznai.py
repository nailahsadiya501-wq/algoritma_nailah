print("=== PROGRAM CEK KELULUSAN MAHASISWA ===")

nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama == "andi":
    target = 70
elif nama == "budi":
    target = 75
elif nama == "citra":
    target = 80
else:
    target = 0
    print("Nama mahasiswa tidak terdaftar!")

# Memeriksa nilai ujian
if target != 0:

    print("Nama:", nama)
    print("Target nilai:", target)

    percobaan = 1
    lulus = False

    while percobaan <= 3 and lulus == False:

        print("\nPercobaan ke-", percobaan)
        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            print("Selamat,", nama, "berhasil lulus!")
            print("Lulus pada percobaan ke-", percobaan)
            lulus = True

        else:
            print("Nilai belum mencapai target!")

            if percobaan == 3:
                print(nama, "dinyatakan TIDAK LULUS setelah 3 kali percobaan!")

        percobaan = percobaan + 1