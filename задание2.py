# Коэффициенты перевода в метры
to_meters = {
    "км": 1000,
    "м": 1,
    "см": 0.01,
    "мм": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254
}

print("Доступные единицы: км, м, см, мм, mi, yd, ft, in")

from_unit = input("Исходная единица: ").strip().lower()
to_unit = input("Целевая единица: ").strip().lower()
value = float(input("Значение: "))

if from_unit not in to_meters or to_unit not in to_meters:
    print("Ошибка: неизвестная единица измерения")
else:
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    print(f"{value} {from_unit} = {result} {to_unit}")
