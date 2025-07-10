# Импортируем tkinter
import tkinter as tk

# Создаём окно
root = tk.Tk()
# Устанавливаем минимальный размер
root.minsize(600, 600)
# Цвет фона всего окна
root.config(bg="#1A1A1A")

# Надпись с текстом
label = tk.Label(root,
                 text="Hello, world",
                 bg="#3A3A3A",
                 fg="#FFF",
                 font=("Montserrat Thin", 60))
# Размещаем её чуть ниже и левее от начала окна
label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

# Кнопка
btn = tk.Button(root,
                text="Hello, world",
                bg="#30343F",
                fg="#FFF",
                font=("Montserrat Black", 40),
                activebackground="#10141F",
                activeforeground="#FFF",
                borderwidth=0)
# Размещаем её чуть ниже середины окна
btn.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.2)

# Запускаем окно
root.mainloop()
