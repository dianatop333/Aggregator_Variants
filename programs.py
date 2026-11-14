programs = [
    {
        "name": "Калькулятор",
        "file": "calculator.py"
    },
    {
        "name": "Конвертер единиц",
        "file": "converter.py"
    },
    {
        "name": "Текстовый редактор",
        "file": "text_editor.py"
    }
]

def show_programs():
    print("\nДоступные программы:")

    for number, program in enumerate(programs, start=1):
        print(f"{number}. {program['name']}")