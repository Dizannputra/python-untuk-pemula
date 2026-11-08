# Membuat Function baru dengan nama belajar_python
def belajar_python():
    print("Halo")

# Memanggil Function "say_hello"
belajar_python() # Halo



# Membuat Function dengan nama belajar_python yang memiliki satu Arguments "name"
def belajar_python(name):
    print("Halo, Saya %s" % name)

# Memanggil Function belajar_python dengan Arguments "name" berupa string dengan value "Rizqi"
belajar_python("Dizan") # Halo, Saya Dizan



# Membuat Function dengan nama belajar_python yang memiliki dua Arguments: "name" dan "age"
def belajar_python(name, age):
    print("Halo, Saya %s. Umur saya %d" % (name, age))

# Memanggil Function belajar_python 
# dengan Arguments "name" berupa string dengan value "Dizan"
# dan Arguments "age" berupa integer dengan value "16"
belajar_python("Dizan", 16) # Halo, Saya Dizan




# Membuat Function dengan nama belajar_python
# yang memiliki Arbitrary Arguments dengan nama "names"
def belajar_python(*names):
    for name in names:
        print("Halo, Saya %s" % name)

# Karena Function di atas memiliki Arbitrary Arguments, 
# maka kita bisa mengirimkan banyak value sebagai Arguments ke dalam Function tersebut
belajar_python("Dizan", "Rafa", "Ibe")




def belajar_python(name, age):
    print("Halo, Saya %s. Umur Saya %d" % (name, age))

# Contoh Function di atas. Jika kita memanggil Function dan mengirim Arguments tanpa nama "key" nya
# maka kita harus menuliskannya secara berurutan (name, age)
belajar_python("Dizan", 16) # Halo, Saya Dizan. Umur Saya 16

# Tetapi jika kita memanggil Function dan mengirim Arguments dengan nama "key" nya
# maka kita tidak harus menulliskannya secara berurutan (age, name)
belajar_python(age = 25, name="Fika") # Halo, Saya Fika. Umur Saya 25



def belajar_python(**student):
    print("Halo, Saya %s. Umur Saya %d" % (student['name'], student['age']))

# Memanggil Function belajar_python dengan Arbitrary Keyword Arguments
belajar_python(age=16, name="Dizan") # Halo, Saya Dizan. Umur Saya 16



# Membuat Function belajar_python dengan Arguments "name" dan menentukan Default valuenya sebagai "Alien".
def belajar_python(name="Alien"):
    print("Halo, Saya %s" % name)

# Memanggil Function belajar_python tanpa mengirimkan Arguments nya.
belajar_python() # Halo, Saya Alien
