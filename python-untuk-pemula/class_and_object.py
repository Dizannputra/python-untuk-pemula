# Membuat Class Cat dengan property color

class Cat:
    color = "black"

# Kita bisa membuat object dari sebuah Class, di bawah ini kita akan membuat object dengan nama cat1
cat1 = Cat();
# Kita juga bisa mengakses property yang di definiskan di dalam Class
print(cat1.color) # black
    



# Membuat Class Cat dengan property color dan menambahkan method constructor
# Kita akan menambahkan method constructor untuk mengubah nilai dari properti color
class Cat:
    color = "black"
    
    def __init__(self, color):
        self.color = color

# Membuat objek baru
cat1 = Cat("orange")
print(cat1.color) # orange




# Membuat Class Cat dan menambahkan method say
# Kita akan menambahkan method say yang berisi perintah untuk mencetak teks "Meong..meong"
class Cat:
    def say(self):
        print("Meong..meong")

# Membuat objek baru
cat1 = Cat()
# Mengakses method di dalam class dari objek yang diinisiasi dari sebuah CLass
cat1.say() # Meong..meong



# Membuat class Cat dengan method say
# Kita mengubah penamaan parameter "self" dengan nama "myParam"
class Cat:
	color = "black"
    
	def say(myParam):
		print("My color is %s" % myParam.color)
 
# Membuat objek baru
cat1 = Cat()
# Memanggil method di dalam Class
cat1.say()
		
