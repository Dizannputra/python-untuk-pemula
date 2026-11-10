# main.py
import matematika

print(matematika.tambah(2, 3))   # Output: 5
print(matematika.kali(4, 5))     # Output: 20


import matematika as m

print(m.tambah(10, 5))   # Output: 15


from matematika import tambah

print(tambah(7, 3))   # Output: 10


import math

print(math.sqrt(16))   # Akar kuadrat → 4.0
print(math.pi)         # Nilai π → 3.141592653589793
