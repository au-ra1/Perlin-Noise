#Pyglet window
import pyglet as gl
from NoiseGenerators import *


window = gl.window.Window(500, 500)
grid_size = 250

def draw_noise():

    for i in range(grid_size):
        for j in range(grid_size):
            a = perlin(i, j)
            if a <
       










@window.event
def on_draw():
    window.clear()
    draw_grid()

gl.app.run()