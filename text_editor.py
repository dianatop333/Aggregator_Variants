print("=== ТЕКСТОВЫЙ РЕДАКТОР ===")

text = input("Введите текст: ")

print("\nВаш текст:")
print(text)

print("\nКоличество символов:", len(text))
print("Количество слов:", len(text.split()))