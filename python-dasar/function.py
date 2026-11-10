def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()


def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Dizan")


def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)



def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Dizan")  # Menggunakan parameter
sapa_orang()        # Menggunakan default


# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")

