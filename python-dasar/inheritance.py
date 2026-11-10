# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

# Child class
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Membuat objek dari class turunan
kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()


class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):
        print(f"{self.nama} sedang terbang!")
        
burung = Burung("Rio")
burung.suara()
burung.terbang()


class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Andi", "Informatika", 2025)
maba.info()
