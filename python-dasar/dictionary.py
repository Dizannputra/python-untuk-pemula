# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

print(mahasiswa["nama"])    # Budi
print(mahasiswa.get("umur")) # 20

mahasiswa["angkatan"] = 2023   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

for key, value in mahasiswa.items():
    print(key, ":", value)

kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi
print(kampus["mahasiswa2"]["umur"])  # 22