a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000


x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True


a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0


buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True
print("pisang" not in buah) # True


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (b menunjuk objek yang sama dengan a)
print(a is c)     # False (c objek berbeda walau isinya sama)
print(a == c)     # True (nilai isinya sama)
