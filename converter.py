print("=== КОНВЕРТЕР ЕДИНИЦ ===")

try:
    meters = float(input("Введите расстояние в метрах: "))

    print("Сантиметры:", meters * 100)
    print("Километры:", meters / 1000)
    print("Миллиметры:", meters * 1000)

except ValueError:
    print("Ошибка! Нужно вводить число.")