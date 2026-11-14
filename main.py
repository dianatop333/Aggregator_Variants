import subprocess
import sys
from pathlib import Path

from programs import show_programs, programs
def show_menu():
    print("\n=== АГРЕГАТОР ВАРИАНТОВ ===")
    print("1. Просмотреть доступные программы")
    print("2. Запустить программу")
    print("0. Выход")

def main():
    while True:
        show_menu()

        choice = input("Выберите действие: ")
        print("Получено:", repr(choice))

        if choice == "1":
            show_programs()

        elif choice == "2":
            show_programs()
            program_choice = input("Введите номер программы: ")

            if program_choice.isdigit() and 1 <= int(program_choice) <= len(programs):
                selected_program = programs[int(program_choice) - 1]
                print(f"Вы выбрали: {selected_program['name']}")

                program_path = Path(__file__).parent / selected_program["file"]
                subprocess.run([sys.executable, str(program_path)])
            else:
                print("Ошибка! Такого номера нет.")

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Ошибка! Выберите существующий пункт меню.")

if __name__ == "__main__":
    main()
