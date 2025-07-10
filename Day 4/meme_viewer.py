# Импортируем библиотеку tkinter для создания оконной программы
import tkinter as tk

# Импортируем PIL — чтобы работать с картинками (например, открывать и показывать изображения)
from PIL import Image, ImageTk

# Папка, где хранятся наши мемы
MEMES_DIR = "memes/"

# Список названий файлов с мемами
MEMES_LIST = [
    "6fb726d46f5894ed0c67399b8b42f4c0.jpg",
    "6g-fo54hrcctez4vg4-avzkijc0.jpeg",
    "meme1.jfif",
    "photo_2025-07-03_10-19-25.jpg"
]

# Начальный индекс — какой мем будет показан первым (счёт начинается с 0)
actual_index = 0

# Эта переменная будет хранить ссылку на картинку, чтобы она не исчезла с экрана
image_reference = None

# Создаем главное окно
root = tk.Tk()

# Настраиваем сетку:
# Окно разбито на 3 колонки: слева кнопка ←, по центру мем, справа кнопка →
root.grid_rowconfigure(0, weight=1)  # Строка растягивается по высоте
root.grid_columnconfigure(0, weight=0)  # Левая колонка (кнопка ←) — фиксированная ширина
root.grid_columnconfigure(1, weight=1)  # Центральная колонка (мем) — занимает больше всего места
root.grid_columnconfigure(2, weight=0)  # Правая колонка (кнопка →) — тоже фиксированная


# Эта функция загружает мем по его номеру (index)
def load_meme(index):
    global actual_index, image_reference  # Мы будем изменять эти переменные внутри функции

    filename = MEMES_LIST[index]  # Получаем имя файла
    path = f"{MEMES_DIR}{filename}"  # Полный путь к картинке

    img = Image.open(path)  # Открываем картинку
    image_reference = ImageTk.PhotoImage(img)  # Преобразуем её для tkinter

    # Создаём надпись (Label), в которую поместим картинку
    meme_label = tk.Label(root,
                          image=image_reference,  # Картинка
                          width=img.width,  # Ширина картинки
                          height=img.height  # Высота картинки
                          )
    # Размещаем картинку в центральной части окна
    meme_label.grid(column=1, row=0, sticky="nsew")  # "nsew" — растягивается во все стороны

    actual_index = index  # Запоминаем, какой мем сейчас отображается


def prev_index():
    # Вычисляем индекс предыдущего мема
    # Если это первый мем, то покажем последний — так создаётся круговой переход
    prev_index_meme = (actual_index - 1) % len(MEMES_LIST)

    # Загружаем этот мем
    load_meme(prev_index_meme)


def next_index():
    # Вычисляем индекс следующего мема
    # Если это последний мем, то снова покажем первый — круговой переход
    prev_index_meme = (actual_index + 1) % len(MEMES_LIST)

    # Загружаем этот мем
    load_meme(prev_index_meme)


# Кнопка со стрелкой влево "<-"
prev_meme_btn = tk.Button(root, text="<-", command=prev_index)
# Размещаем её слева от картинки
prev_meme_btn.grid(column=0, row=0, sticky="e")

# Кнопка со стрелкой вправо "->"
next_meme_btn = tk.Button(root, text="->", command=next_index)
# Размещаем её справа от картинки
next_meme_btn.grid(column=2, row=0, sticky="w")

# Загружаем самый первый мем (индекс 0)
load_meme(actual_index)

# Запускаем главный цикл программы — окно будет работать, пока его не закроют
root.mainloop()
