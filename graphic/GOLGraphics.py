from tkinter import *
from source.world import World
import random
from source.GoL import Alive

tk = Tk()
tk.title("GOL")
canvas = Canvas(width=1000, height=1000, bg="white")
canvas.pack()
def cell(x, y):
    size = 5
    x = x * (size*2)
    y = y * (size*2)
    cell = canvas.create_rectangle(x-size, y-size, x+size, y+size, fill="black", outline="white")

def kill_cell(x, y):
    size = 5
    x = x * (size*2)
    y = y * (size*2)
    cell = canvas.create_rectangle(x-size, y-size, x+size, y+size, fill="white", outline="white")



def randomCells(world):
    for x in range(1, 100):
        for y in range(1, 100):
            if random.randrange(0, 7) == 1:
                world.activate(x, y)
        
def updateGrapics(world):
    for x in range(1, 100):
        for y in range(1, 100):
            if world.get(x, y) == Alive:
                cell(x, y)
            else:
                kill_cell(x, y)

def start():
    world = World()
    randomCells(world)
    return world

def step(world):
    canvas.delete("all")
    updateGrapics(world)
    world.nextGeneration()
    canvas.pack()
    canvas.update()
    canvas.after(100, step(world))
