#  Импорт библиотек
import tkinter as tk
from tkinter import ttk

# Создание главного холста
root = tk.Tk()
root.minsize(1000, 1000)
root.config(bg="#FFD9DA")

# Стили элоементов
button_style = {
    "bg": "#30343F",
    "fg": "#FFF",
    "font": ("Montserrat Black", 40),
    "activebackground": "#10141F",
    "activeforeground": "#FFF",
    "borderwidth": 0
}
label_style = {
    "bg": "#3A3A3A",
    "fg": "#FFF",
    "font": ("Montserrat Thin", 50)
}
radio_button_style = {
    "bg": "#80A1C1",
    "fg": "#FFF",
    "font": ("Montserrat Black", 40),
    "activebackground": "#30343F",
    "activeforeground": "#FFF",
    "selectcolor": "#000",
}
entry_style = {
    "font": ("Montserrat Regular", 50),
    "fg": "#514B79",
    "bg": "#776EB2",
    "disabledbackground": "#EDE193",
    "disabledforeground": "#716B99",
    "borderwidth": 0
}
check_button_style = {
    "font": ("Montserrat Regular", 50),
    "fg": "#514B79",
    "bg": "#776EB2",
    "borderwidth": 0,
    "activebackground": "#30343F",
    "activeforeground": "#FFF"
}


def save_user_data():
    new_list = []
    for hobby, var in selected_genres.items():
        if var.get() == 1:
            new_list.append(hobby)

    print(f"Анкета пользователя {input_nickname.get()}")
    print(f"Пол: {gender.get()}")
    print(f"Выбранные жанры: {', '.join(new_list)}")
    print(f"Ник: {input_nickname.get()}")


# Label для информации на какой странице находится пользователь
info_label = tk.Label(root, text="Создание профиля", **label_style)
info_label.pack(side="top", fill="both", expand=0)

# Frame для создания анкеты - в нём будет весь интерфейс
content_frame = tk.Frame(root, bg="#80A1C1")
content_frame.pack(side="top", fill="both", expand=1)

save_button = tk.Button(root, text="Сохранить", command=save_user_data, **button_style)
save_button.pack(side="bottom", fill="both", expand=0)

# Создание сетки для Основного Frame
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_columnconfigure(2, weight=1)

# Frame для выбора пола
gender_frame = tk.Frame(content_frame, bg="#80A1C1")
gender_frame.grid(column=0, row=0, sticky="nsew")

# Frame для выбора любимых жанров
genre_frame = tk.Frame(content_frame, bg="#80A1C1")
genre_frame.grid(column=1, row=0, sticky="nsew")

# Frame для ввода никнейма
nickname_frame = tk.Frame(content_frame, bg="#80A1C1")
nickname_frame.grid(column=2, row=0, sticky="nsew")


# Создание интерфейса для выбора пола
def save_gender():
    pass


gender = tk.StringVar()

info_gender_label = tk.Label(gender_frame, text="Выберете пол:", **label_style)
info_gender_label.pack(side="top", fill="both", expand=0)

tk.Radiobutton(gender_frame, text="Мужской", value="Мужской", variable=gender, command=save_gender,
               **radio_button_style).pack(side="top",
                                          fill="both",
                                          expand=0)
tk.Radiobutton(gender_frame, text="Женский", value="Женский", variable=gender, command=save_gender,
               **radio_button_style).pack(side="top",
                                          fill="both",
                                          expand=0)

# Создание интерфейса для любимых жанров
info_genre_label = tk.Label(genre_frame, text="Выберете любимые жанры:", **label_style)
info_genre_label.pack(side="top", fill="both", expand=0)

genres = ["Боевик", "Фентези", "Документальный", "Фантастика", "Комедия", "Путешествия"]
selected_genres = {}

for genre in genres:
    var = tk.IntVar()
    selected_genres[genre] = var
    tk.Checkbutton(genre_frame, text=genre, variable=var, **check_button_style).pack(side="top", fill="both", expand=0, anchor="w")

# Создание интерфейса для никнейма
info_nickname_label = tk.Label(nickname_frame, text="Введите никнейм:", **label_style)
info_nickname_label.pack(side="top", fill="both", expand=0)

input_nickname = tk.Entry(nickname_frame, **entry_style)
input_nickname.pack(side="top", fill="both", expand=0)

root.mainloop()
