# Импорт библиотек
import tkinter as tk  # Библиотека для создания графического интерфейса
from tkinter import ttk  # Современные виджеты с улучшенным дизайном

# Создание главного окна приложения
root = tk.Tk()
root.minsize(1000, 1000)  # Минимальный размер окна — 1000x1000 пикселей
root.config(bg="#FFD9DA")  # Цвет фона — нежно-розовый

# Подключаем стили из файла styles.py
from styles import style, entry_style


# Функция, которая выполняется при нажатии на кнопку "Сохранить"
def save_user_data():
    # Собираем выбранные жанры
    new_list = []
    for hobby, var in selected_genres.items():
        if var.get() == 1:  # Если чекбокс отмечен
            new_list.append(hobby)

    # Выводим данные в консоль
    print(f"Анкета пользователя {input_nickname.get()}")
    print(f"Пол: {gender.get()}")
    print(f"Выбранные жанры: {', '.join(new_list)}")
    print(f"Ник: {input_nickname.get()}")


# Метка "Создание профиля" — заголовок программы
info_label = ttk.Label(root, text="Создание профиля", style="Custom.TLabel")
info_label.pack(side="top", fill="both", expand=0)  # Размещаем вверху

# Рамка для всей анкеты — внутри неё будут разные разделы
content_frame = tk.Frame(root, bg="#80A1C1")  # Серо-голубой фон
content_frame.pack(side="top", fill="both", expand=1)  # Занимает большую часть окна

# Кнопка "Сохранить"
save_button = ttk.Button(root, text="Сохранить", style="Custom.TButton", command=save_user_data)
save_button.pack(side="bottom", fill="both", expand=0)  # Внизу экрана

# Настраиваем сетку внутри content_frame: 1 строка, 3 колонки
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_columnconfigure(2, weight=1)

# Рамка для выбора пола
gender_frame = tk.Frame(content_frame, bg="#80A1C1")
gender_frame.grid(column=0, row=0, sticky="nsew")  # Левая часть окна

# Рамка для выбора жанров
genre_frame = tk.Frame(content_frame, bg="#80A1C1")
genre_frame.grid(column=1, row=0, sticky="nsew")  # Центральная часть окна

# Рамка для ввода никнейма
nickname_frame = tk.Frame(content_frame, bg="#80A1C1")
nickname_frame.grid(column=2, row=0, sticky="nsew")  # Правая часть окна


# --- Интерфейс для выбора пола ---
def save_gender():
    pass  # Эта функция пока ничего не делает


# Переменная для хранения выбранного пола
gender = tk.StringVar()

# Надпись "Выберете пол"
info_gender_label = ttk.Label(gender_frame, text="Выберете пол:", style="Custom.TLabel")
info_gender_label.pack(side="top", fill="both", expand=0)

# Радиокнопка "Мужской"
ttk.Radiobutton(gender_frame,
                text="Мужской",
                value="Мужской",
                variable=gender,
                command=save_gender,
                style="Custom.TRadiobutton").pack(side="top", fill="both", expand=0)

# Радиокнопка "Женский"
ttk.Radiobutton(gender_frame,
                text="Женский",
                value="Женский",
                variable=gender,
                command=save_gender,
                style="Custom.TRadiobutton").pack(side="top", fill="both", expand=0)

# --- Интерфейс для выбора любимых жанров ---
# Надпись "Выберете любимые жанры"
info_genre_label = ttk.Label(genre_frame, text="Выберете любимые жанры:", style="Custom.TLabel")
info_genre_label.pack(side="top", fill="both", expand=0)

# Список доступных жанров
genres = ["Боевик", "Фентези", "Документальный", "Фантастика", "Комедия", "Путешествия"]

# Словарь для хранения состояния каждого чекбокса
selected_genres = {}

# Создаем чекбоксы для каждого жанра
for genre in genres:
    var = tk.IntVar()  # Переменная, которая хранит 0 или 1 (выбрано или нет)
    selected_genres[genre] = var  # Сохраняем её в словаре
    # Создаем чекбокс и добавляем его на форму
    ttk.Checkbutton(genre_frame,
                    text=genre,
                    variable=var,
                    style="Custom.TCheckbutton").pack(side="top", fill="both", expand=0, anchor="w")

# --- Интерфейс для ввода никнейма ---
# Надпись "Введите никнейм"
info_nickname_label = ttk.Label(nickname_frame, text="Введите никнейм:", style="Custom.TLabel")
info_nickname_label.pack(side="top", fill="both", expand=0)

# Поле для ввода текста
input_nickname = tk.Entry(nickname_frame, **entry_style)
input_nickname.pack(side="top", fill="both", expand=0)

# Запускаем главный цикл приложения — окно будет работать, пока его не закроют
root.mainloop()
