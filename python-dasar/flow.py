nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B


buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Output:
# apel
# jeruk
# mangga


count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

# Output:
# Hitung: 0
# Hitung: 1
# Hitung: 2
# Hitung: 3
# Hitung: 4


for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)

# Output:
# 1
# 2
# 4
