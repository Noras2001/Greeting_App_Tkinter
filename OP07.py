import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Приветствие")

# Функция для обработки нажатия кнопки
def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Привет, {name}!")

# Создаем виджеты
name_label = tk.Label(root, text="Введите ваше имя:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

greet_button = tk.Button(root, text="Поприветствовать", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

# Запускаем главный цикл программы
root.mainloop()
