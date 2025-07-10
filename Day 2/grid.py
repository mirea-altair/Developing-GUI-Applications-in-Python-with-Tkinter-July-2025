# Импортируем библиотеку tkinter для создания оконных программ
import tkinter as tk

# Создаем главное окно
root = tk.Tk()
# Устанавливаем минимальный размер окна
root.minsize(1000, 600)

# Настраиваем сетку:
# Строка 0 растягивается
root.grid_rowconfigure(0, weight=1)
# Колонки 0 и 1 делят пространство поровну
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Создаём надпись (Label) с текстом "Hello, world"
label = tk.Label(root,
                 text="Hello, world",
                 bg="#2A2A2A",  # Темно-серый фон
                 fg="#FFF",  # Белый текст
                 font=("Montserrat Thin", 60))  # Шрифт и размер
# Размещаем надпись в левой части окна (колонка 0, строка 0)
label.grid(column=0, row=0, sticky="nsew")  # sticky="nsew" заставляет элемент растягиваться во все стороны

# Создаём кнопку (Button)
btn = tk.Button(root,
                text="Hello, world",
                bg="#30343F",  # Фиолетовый фон кнопки
                fg="#FFF",  # Белый текст
                font=("Montserrat Black", 40),
                activebackground="#10141F",  # Цвет при нажатии
                activeforeground="#FFF",  # Цвет текста при нажатии
                borderwidth=0)  # Без границы
# Размещаем кнопку в правой части окна (колонка 1, строка 0)
btn.grid(column=1, row=0, sticky="nsew")

# Запускаем окно
root.mainloop()
