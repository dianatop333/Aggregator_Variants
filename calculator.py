print("=== КАЛЬКУЛЯТОР ===")

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сумма:", a + b)
    print("Разность:", a - b)
    print("Произведение:", a * b)

    if b != 0:
        print("Деление:", a / b)
    else:
        print("На ноль делить нельзя!")

except ValueError:
    print("Ошибка! Нужно вводить числа.")