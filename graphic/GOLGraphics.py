from tkinter import *

tk = Tk()
tk.title("GOL")
canvas = Canvas(width=500, height=500, bg="white")
canvas.pack()
def cell(x, y):
    size = 10
    x = x * (size*2)
    y = y * (size*2)
    cell = canvas.create_rectangle(x-size, y-size, x+size, y+size, fill="black", outline="white")

def kill_cell(x, y):
    size = 10
    x = x * (size*2)
    y = y * (size*2)
    cell = canvas.create_rectangle(x-size, y-size, x+size, y+size, fill="white", outline="white")
