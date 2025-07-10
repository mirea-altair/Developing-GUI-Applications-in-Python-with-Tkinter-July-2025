# Импортируем модуль ttk — он позволяет создавать красивые кнопки, чекбоксы и другие элементы
from tkinter import ttk

# Импортируем цвета из файла colors.py
# Эти переменные задают цвета для разных элементов интерфейса:
# - Кнопки, чекбоксы, метки и т.д.
from colors import (
    button_background,  # Цвет фона кнопки
    text_color,  # Цвет текста
    hover_effect_color,  # Цвет при наведении мыши
    label_background,  # Цвет фона меток
    entry_background  # Цвет поля ввода
)

# Импортируем шрифты из файла fonts.py
from fonts import (
    button_font,  # Шрифт для кнопок
    label_font  # Шрифт для надписей
)

# Создаем стиль для кнопок и называем его "Custom.TButton"
style = ttk.Style()

style.configure(
    "Custom.TButton",  # Название стиля
    background=button_background,  # Цвет фона кнопки
    foreground=text_color,  # Цвет текста
    font=button_font,  # Шрифт и размер текста
    padding=10  # Отступы внутри кнопки
)

# Делаем так, чтобы при наведении мыши на кнопку цвет фона менялся
style.map(
    "Custom.TButton",
    background=[("active", hover_effect_color)]  # При наведении мыши
)

# Создаем стиль для чекбоксов
style.configure(
    "Custom.TCheckbutton",  # Название стиля
    background=button_background,
    foreground=text_color,
    font=button_font,
    padding=10
)

# Меняем цвет при наведении мыши
style.map(
    "Custom.TCheckbutton",
    background=[("active", hover_effect_color)]
)

# Стиль для обычных надписей (например, заголовки)
style.configure(
    "Custom.TLabel",  # Название стиля
    background=label_background,  # Цвет фона
    foreground=text_color,  # Цвет текста
    font=label_font,  # Шрифт
    padding=10  # Отступы
)

# Стиль для радиокнопок
style.configure(
    "Custom.TRadiobutton",  # Название стиля
    background=button_background,
    foreground=text_color,
    font=button_font,
    padding=10
)

# Меняем цвет при наведении мыши
style.map(
    "Custom.TRadiobutton",
    background=[("active", hover_effect_color)]
)

# Стиль для поля ввода текста (например, для ввода никнейма)
entry_style = {
    "font": ("Montserrat Regular", 50),  # Шрифт и размер текста
    "fg": "#514B79",  # Цвет самого текста
    "bg": entry_background,  # Цвет фона поля
    "disabledbackground": "#EDE193",  # Цвет, когда поле неактивно
    "disabledforeground": "#716B99",  # Цвет текста, когда поле неактивно
    "borderwidth": 0  # Без рамки вокруг
}
