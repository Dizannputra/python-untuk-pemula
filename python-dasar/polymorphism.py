class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

# Polymorphism in action
hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())


class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Semua objek diperlakukan sama sebagai 'Hewan'
daftar_hewan = [Kucing(), Anjing(), Hewan()]

for h in daftar_hewan:
    print(h.suara())


def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())


print(len("Python"))   # string
print(len([1, 2, 3]))  # list
print(len({"a": 1, "b": 2}))  # dictionary
