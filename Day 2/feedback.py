# Импортируем библиотеку tkinter для создания оконной программы
import tkinter as tk

# Глобальные переменные (мы будем их использовать в разных функциях)
film_for_feedback = ""  # Название фильма
input_feedback = None  # Поле для отзыва
film_word_label = None  # Надпись "Фильм:"
film_title_label = None  # Надпись с названием фильма
feedback_word_label = None  # Надпись "Отзыв:"
send_feedback_button = None  # Кнопка "Отправить"

# Создаем главное окно
root = tk.Tk()
root.title("Отзовик")  # Заголовок окна
root.minsize(1100, 1000)  # Минимальный размер окна
root.config(bg="#514B79")  # Цвет фона окна


# Функция, которая запускается при нажатии кнопки "Далее"
def continue_func():
    # Объявляем глобальные переменные, чтобы мы могли их изменять
    global film_for_feedback, input_feedback, film_word_label, film_title_label, feedback_word_label, send_feedback_button

    # Получаем текст из поля ввода фильма
    film_for_feedback = input_film.get()

    # Если пользователь что-то ввёл — продолжаем
    if film_for_feedback:
        # Убираем старые элементы интерфейса
        label_film_info.destroy()
        input_film.destroy()
        continue_btn.destroy()

        # Добавляем новые элементы:

        # Надпись "Фильм:"
        film_word_label = tk.Label(root,
                                   text="Фильм:",
                                   bg="#9F93ED",  # Цвет фона
                                   fg="#EDE193",  # Цвет текста
                                   font=("Montserrat Regular", 50),  # Шрифт и размер
                                   )
        film_word_label.grid(column=0, row=0, sticky="nsew")  # Размещаем в сетке

        # Название фильма, которое ввёл пользователь
        film_title_label = tk.Label(root,
                                    text=f"{film_for_feedback}",
                                    bg="#9F93ED",
                                    fg="#EDE193",
                                    font=("Montserrat Regular", 50),
                                    )
        film_title_label.grid(column=1, row=0, sticky="nsew")

        # Надпись "Отзыв:"
        feedback_word_label = tk.Label(root,
                                       text="Отзыв:",
                                       bg="#9F93ED",
                                       fg="#EDE193",
                                       font=("Montserrat Regular", 50),
                                       )
        feedback_word_label.grid(column=0, row=1, sticky="nsew")

        # Поле для ввода отзыва (можно писать много строк)
        input_feedback = tk.Text(root, wrap="word",
                                 font=("Montserrat Thin", 30),
                                 fg="#514B79",
                                 bg="#776EB2",
                                 borderwidth=0,
                                 width=30, height=10
                                 )
        input_feedback.grid(column=1, row=1, sticky="nsew")

        # Кнопка "Отправить"
        send_feedback_button = tk.Button(root,
                                         text="Отправить",
                                         command=send_feedback,  # Что делать при нажатии
                                         bg="#9F93ED",
                                         fg="#EDE193",
                                         font=("Montserrat Black", 40),
                                         activebackground="#514B79",
                                         activeforeground="#EDE193",
                                         borderwidth=0,
                                         )
        send_feedback_button.grid(column=1, row=2, sticky="nsew")


# Функция отправки отзыва
def send_feedback():
    global input_feedback

    # Проверяем, что пользователь написал отзыв
    if input_feedback.get("1.0", tk.END).strip():  # .strip() удаляет пробелы в начале и конце
        # Убираем все элементы
        film_word_label.destroy()
        film_title_label.destroy()
        feedback_word_label.destroy()
        send_feedback_button.destroy()

        # Меняем размер окна
        root.geometry("2000x1000")

        # Выводим сообщение об успешной отправке
        info_label = tk.Label(root,
                              text="Ваш отзыв отправлен. Можете закрыть приложение",
                              bg="#9F93ED",
                              fg="#EDE193",
                              font=("Montserrat Regular", 50),
                              )
        info_label.grid(column=1, row=1, sticky="nsew")


# Настройка сетки окна — как таблица
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)

# Надпись "Фильм:"
label_film_info = tk.Label(root,
                           text="Фильм:",
                           bg="#9F93ED",
                           fg="#EDE193",
                           font=("Montserrat Regular", 50),
                           )
label_film_info.grid(column=1, row=0, sticky="nsew")

# Поле ввода названия фильма
input_film = tk.Entry(root,
                      font=("Montserrat Regular", 50),
                      fg="#514B79",
                      bg="#776EB2",
                      disabledbackground="#EDE193",
                      disabledforeground="#716B99",
                      borderwidth=0
                      )
input_film.grid(column=1, row=1, sticky="nsew")

# Кнопка "Далее"
continue_btn = tk.Button(root,
                         text="Далее",
                         command=continue_func,  # Вызывает функцию continue_func
                         bg="#9F93ED",
                         fg="#EDE193",
                         font=("Montserrat Black", 40),
                         activebackground="#514B79",
                         activeforeground="#EDE193",
                         borderwidth=0,
                         )
continue_btn.grid(column=1, row=2, sticky="nsew")

# Запускаем главный цикл программы — окно будет работать, пока его не закроют
root.mainloop()
