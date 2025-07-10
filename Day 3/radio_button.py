# Импортируем tkinter
import tkinter as tk

# Создаём главное окно
root = tk.Tk()
root.minsize(800, 800)         # Размер окна
root.config(bg="#FFD9DA")      # Цвет фона (нежно-розовый)

# Функция, которая обновляет метку при выборе радиокнопки
def show_choice():
    choice_label.config(text=f"Выбор:\n{choice.get()}")  # Получаем значение из переменной choice

# Переменная для хранения выбранного значения
choice = tk.StringVar()

# Рамка для радиокнопок
frame = tk.Frame(root, bg="#80A1C1")
frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.6)

# Метка, где будет отображаться результат
choice_label = tk.Label(root,
                        text="Выбор:\n-",              # Текст по умолчанию
                        bg="#80A1C1",                  # Цвет фона
                        fg="#FFF",                     # Цвет текста
                        font=("Montserrat Regular", 60))
choice_label.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.6)

# Первая радиокнопка — "Муж"
tk.Radiobutton(
    frame,
    text="Муж",
    value="Муж",                     # Значение, которое передается в переменную choice
    command=show_choice,             # Вызываем функцию при выборе
    variable=choice,                 # Переменная для хранения результата
    bg="#80A1C1",
    fg="#FFF",
    font=("Montserrat Black", 40),
    activebackground="#30343F",
    activeforeground="#FFF",
    selectcolor="#000"               # Цвет кружочка при выборе
).pack(side="top", fill="both", expand=1)

# Вторая радиокнопка — "Жен"
tk.Radiobutton(
    frame,
    text="Жен",
    value="Жен",
    command=show_choice,
    variable=choice,
    bg="#80A1C1",
    fg="#FFF",
    font=("Montserrat Black", 40),
    activebackground="#30343F",
    activeforeground="#FFF",
    selectcolor="#000"
).pack(side="top", fill="both", expand=1)

# Запускаем окно
root.mainloop()