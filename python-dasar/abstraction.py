from abc import ABC, abstractmethod

# Abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Tidak bisa langsung membuat object dari class abstract
# h = Hewan()  # Error!

# Hanya bisa dari subclass
k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())


from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")

# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)

# Memanggil dengan berbagai metode
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)
