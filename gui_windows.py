import tkinter
from tkinter.ttk import Frame, Button, Entry, Label, Style
from tkinter import Tk


def openNewWindow():
    newWindow = tkinter.Toplevel(root)
    newWindow.geometry('200x280')
    newWindow.title('Nueva ventana')


# Ventana principal
root = Tk()
root.geometry('800x600')
root.title('Agenda personal')


Button(root, text='Abrir nueva ventana...', command=openNewWindow).pack()

root.mainloop()
