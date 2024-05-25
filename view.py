import tkinter as tki
from tkinter import ttk

# Использование виджета Menu
# Пишем обработчики событий для пунктов меню
f1 = lambda: lbl.config(text = "Hello")
f2 = lambda: lbl.config(text = "Hello Petya")
def f3():
    """HelloFunc"""
    lbl.config(text = "Hello Masha Ivanova")
def f4():
    """HelloFunc"""
    lbl.config(text = "Hello Masha Petrova")

# Формируем окно с меню
root = tki.Tk()
root.geometry('600x250+100+80')
root.title("My application")
mainmenu = tki.Menu(root, tearoff=0) # Создаем объект класса Menu
# Выпадающее меню. Нельзя открепить (tearoff=0)
# Формированеи структуры меню
# Формирование выпадающего подменю
printmenu2 = tki.Menu(mainmenu, tearoff=0) # Создаем объект класса Menu
printmenu2.add_command(label="Ivanova", command = f3)
printmenu2.add_command(label="Petrova", command = f4)
# Формирование основного выпадающего меню
# В него вставлено подменю
printmenu1 = tki.Menu(mainmenu, tearoff=0)
printmenu1.add_command(label="Petya", command = f2)
printmenu1.add_cascade(label="Masha", menu = printmenu2)
# Размещение пунктов в меню
mainmenu.add_cascade(label="Печать", menu=printmenu1)
mainmenu.add_command(label="Hello", command = f1)
mainmenu.add_command(label="Exit", command = root.destroy)
root.config(menu=mainmenu)
# Поле с приветствием
lbl = tki.Label(root, text="Приветствие")
# Относительные координаты - относительно левого верхнего угла
# (1,1) - правый нижний угол
lbl.place(relx=0.25, rely=0.25)
# lbl.grid(column=0, row=0)
root.mainloop()
