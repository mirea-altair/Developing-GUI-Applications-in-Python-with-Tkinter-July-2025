# Импортируем библиотеку tkinter для создания оконных программ
import tkinter as tk

# Создаём главное окно
root = tk.Tk()
root.minsize(800, 800)  # Минимальный размер окна
root.config(bg="#FFD9DA")  # Цвет фона окна (нежно-розовый)


# Функция, которая показывает выбранные хобби
def show_choices():
    new_list = []
    for hobby, var in selected_hobbies.items():
        if var.get() == 1:  # Если чекбокс отмечен
            new_list.append(hobby)  # Добавляем хобби в список

    # Обновляем текст метки
    choices_label.config(text=f"Выбранные хобби:\n{'\n'.join(new_list)}")


# Метка, где будет отображаться результат
choices_label = tk.Label(root,
                         text="Выбор:\n-",  # Текст по умолчанию
                         bg="#80A1C1",  # Цвет фона (синевато-серый)
                         fg="#FFF",  # Цвет текста (белый)
                         font=("Montserrat Regular", 60))  # Шрифт и размер
choices_label.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.6)

# Создаём рамку, чтобы красиво расположить элементы
frame = tk.Frame(root, bg="#80A1C1")
frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.6)

# Надпись "Хобби"
info_label = tk.Label(frame, text="Хобби")
info_label.pack(side="top", fill="both", expand=1)

# Список возможных хобби
hobbies = ["Спорт", "Качалка", "Чтение"]

# Словарь для хранения переменных чекбоксов
selected_hobbies = {}

for hobby in hobbies:
    var = tk.IntVar()  # Переменная для хранения состояния чекбокса (0 или 1)
    selected_hobbies[hobby] = var  # Сохраняем её в словаре
    # Создаём чекбокс и добавляем его на форму
    tk.Checkbutton(frame,
                   text=hobby,
                   variable=var).pack(side="top", fill="both", expand=1)

# Кнопка "Сохранить"
save_btn = tk.Button(
    frame,
    text="Сохранить",
    command=show_choices,  # При нажатии обновляем метку
    bg="#30343F",  # Цвет кнопки
    fg="#FFF",  # Цвет текста
    font=("Montserrat Black", 40),  # Шрифт
    activebackground="#10141F",  # Цвет при нажатии
    activeforeground="#FFF"  # Цвет текста при нажатии
)
save_btn.pack(side="top", fill="both", expand=1)

# Запускаем главный цикл программы
root.mainloop()
