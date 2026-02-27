# Program menampilkan segitiga bintang

# Input jumlah baris
baris = int(input("Masukkan jumlah baris: "))

# Perulangan untuk membuat pola
for i in range(1, baris + 1):
    # Membuat spasi agar segitiga rata tengah
    print(" " * (baris - i), end="")
    
    # Menampilkan bintang
    print("* " * i)