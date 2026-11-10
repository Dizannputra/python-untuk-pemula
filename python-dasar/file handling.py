# Membaca isi file
file = open("data.txt", "r")  # "r" = read
print(file.read())
file.close()


file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  # strip() untuk hapus newline
file.close()


# Menulis file baru atau menimpa file lama
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()

# Menambah data di akhir file
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()


with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)


# Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())
