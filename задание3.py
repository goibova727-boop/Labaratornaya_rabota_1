year = int(input("Введите год: "))

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if is_leap(year):
    print(f"{year} — високосный год")
else:
    print(f"{year} — не високосный год")

# Поиск ближайшего високосного года
if is_leap(year):
    nearest = year
else:
    # Ищем в обе стороны
    up = year + 1
    down = year - 1
    while True:
        if is_leap(up):
            nearest = up
            break
        if is_leap(down):
            nearest = down
            break
        up += 1
        down -= 1

print(f"Ближайший високосный год: {nearest}")
