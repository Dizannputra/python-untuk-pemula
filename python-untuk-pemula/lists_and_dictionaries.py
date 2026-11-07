# Membuat lists yang berisi nama-nama hewan
animals = ["Ayam", "Bebek", "Cicak"]

# Kita bisa mengakses item di dalam "Lists" berdasarkan urutannya (indexing)
# semisal kita ingin mengakses item "Bebek" (urutan kedua), maka kita bisa menggunakan indexing "1"
# kenapa tidak menggunakan indexing "2"? karena indexing dimulai dari angka 0, bukan 1 (n - 1)

print(animals[1]) # Bebek

# Jika kita ingin mengakses dengan urutan sebaliknya (dari urutan paling akhir),
# kita bisa menggunakan negative indexing
# Jika kita menggunakan indexing "-1", artinya kita mengakses item terakhir
# Jika menggunakan indexing "-2", artinya kita mengakses item kedua dari urutan terakhir

print(animals[-1]) # Cicak
print(animals[-2]) # Bebek



animals = ["Ayam", "Bebek", "Cicak"]

# Menambah item pada "Lists" dengan posisi (indexing) terakhir menggunakan function "append"
animals.append("Domba")
print(animals) # ["Ayam", "Bebek", "Cicak", "Domba"]

# Menambah item pada "Lists" dengan posisi (indexing) tertentu menggunakan function "insert"
# Contoh kita ingin menambahkan 1 item dengan posisi ketiga (indexing = 2)

animals.insert(2, "Buaya")
print(animals) # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']



animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu (Bebek) pada "Lists" dengan method "remove"
animals.remove("Bebek")
print(animals) # ["Ayam", "Cicak"]

# Menghapus item terakhir pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals) # ["Ayam", "Bebek"]

# Menghapus item berdasarkan posisinya (indexing) pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals) # ["Bebek", "Cicak"]

# Menghapus semua item pada "Lists" dengan method "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals) # []



# Menggabungkan sebuah "Lists" dengan "Lists" lainnya
animals = ["Ayam", "Bebek", "Cicak"]
otherAnimals = ["Domba", "Elang", "Gajah"]
animals.extend(otherAnimals)
print(animals) # ["Ayam", "Bebek", "Cicak", "Domba", "Elang", "Gajah"]

fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits) # ["Apel", "Mangga", "Pisang", "Durian", "Semangka", "Jeruk"]



# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
   "first_name": "Dizan",
    "last_name": "Renaldi",
    "age": 16
}

# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name']) # Dizan
# Cara kedua dengan method "get"
print(firstPerson.get('age')) # 16

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['first_name', 'last_name', 'age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values()) # dict_values(['Dizan', 'Renaldi', 16])



firstPerson = {
   "first_name": "Dizan",
    "last_name": "Renaldi",
    "age": 16
}

# Menambahkan item ke dalam Dictionaries
# Menambahkan item berat badan (weight) ke dalam firstPerson
firstPerson['weight'] = 55
print(firstPerson) # {'first_name': 'Dizan', 'last_name': 'Renaldi', 'age': 16, 'weight': 55}



firstPerson = {
   "first_name": "Dizan",
    "last_name": "Renaldi",
    "age": 16
}

# Ada 2 cara untuk mengubah atau mengupdate sebuah value dari item pada Dictionaries

# Cara Pertama
firstPerson['age'] = 15

# Cara Kedua dengan method "update"
# Jika kita menggunakan cara ini, ketika item yang di update berdasarkan key (age) ditemukan,
# maka akan diupdate.
# Namun jika item belum ada, maka otomatis akan menambahkan item baru
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson) # {'first_name': 'Dizan', 'last_name': 'Renaldi', 'age': 15, 'hair_color': 'black'}




firstPerson = {
   "first_name": "Dizan",
    "last_name": "Renaldi",
    "age": 16
}

# Untuk menghapus item dari Dictionaries, kita bisa menggunakan method "pop"
# Kita wajib menambahkan nama "key" jika menggunakan method "pop"
firstPerson.pop("age")
print(firstPerson) # {'first_name': 'Dizan', 'last_name': 'Renaldi'}

# Untuk menghapus semua item, kita bisa menggunakan method "clear"
firstPerson.clear()
print(firstPerson) # {}
