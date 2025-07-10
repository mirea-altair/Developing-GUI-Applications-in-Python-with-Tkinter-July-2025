# Импортируем tkinter
import tkinter as tk

# Создаём окно
root = tk.Tk()

# Добавляем три надписи и одну кнопку.
# Они "прилипают" к разным сторонам окна:

# Метка справа
label1 = tk.Label(root,
                  text="Hello, world",
                  bg="#3A3A3A",
                  fg="#FFF",
                  font=("Montserrat Thin", 60))
label1.pack(side="right", fill="both", expand=True)

# Метка слева
label2 = tk.Label(root,
                  text="Hello, world",
                  bg="#4A4A4A",
                  fg="#FFF",
                  font=("Montserrat Thin", 60))
label2.pack(side="left", fill="both", expand=True)

# Метка сверху
label3 = tk.Label(root,
                  text="Hello, world",
                  bg="#2A2A2A",
                  fg="#FFF",
                  font=("Montserrat Thin", 60))
label3.pack(side="top", fill="both", expand=True)

# Кнопка снизу
btn = tk.Button(root,
                text="Hello, world",
                bg="#30343F",
                fg="#FFF",
                font=("Montserrat Black", 40),
                activebackground="#10141F",
                activeforeground="#FFF",
                borderwidth=0)
btn.pack(side="bottom", fill="both", expand=True)

# Запускаем окно
root.mainloop()
