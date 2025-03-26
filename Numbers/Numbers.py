a = -87.e100
# Complex numbers are written with a "j" as the imaginary part:
b = 3+5j
x = 1 
y = 2.8
z = 1j

print(type(z))
print("Type of a:", type(a))
print("Type of b:", type(b))

print(2 + 2)

y_complex = complex(y)


print("y int made complex:" , y_complex)

# You can convert from one type to another with the int(), float(), and complex() methods:

print(float(x))
print(int(y))
print(complex(y))