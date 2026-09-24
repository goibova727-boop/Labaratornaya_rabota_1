import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

# Полупериметр
p = (a + b + c) / 2

# Площадь по формуле Герона
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Площадь треугольника: {area:.2f}")

# Определение вида треугольника
sides = sorted([a, b, c])
x, y, z = sides[0]**2, sides[1]**2, sides[2]**2

if abs(x + y - z) < 1e-6:
    print("Треугольник прямоугольный")
elif x + y < z:
    print("Треугольник тупоугольный")
else:
    print("Треугольник остроугольный")
