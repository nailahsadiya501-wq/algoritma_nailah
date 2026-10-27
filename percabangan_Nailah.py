# variabel dan tipe data
nama_mhs = "Nailah" 
kelas = "C1"

nama = input("Masukkan nama:")
nilai_a = int(input("Masukkan Nilai algoritma:"))
nilai_b = int(input("Masukkan Nilai basisdata:"))
nilai_c = int(input("Masukkan Nilai agama:"))
nilai_d = int(input("Masukkan Nilai pancasila:"))
nilai_e = int(input("Masukkan Nilai informatika:"))
nilai_f = int(input("Masukkan Nilai mandarin:"))
nilai_g = int(input("Masukkan Nilai bindo:"))
rata_rata = (nilai_a + nilai_b + nilai_c + nilai_d + nilai_e + nilai_f + nilai_g) / 7
print(rata_rata)

# penentuan lulus atau tidak 
if rata_rata >=80 and rata_rata <=100:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata<=80:
    print("rata_rata: B") 
elif rata_rata >=50 and rata_rata<=70:
    print("rata_rata: C")
elif rata_rata >=40 and rata_rata<=50:
    print("Nilai: D")       
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai : E")    