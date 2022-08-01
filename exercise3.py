#Sara Paguaga 20634

from library import Renderer, color, V2, V3
import random

width = 540
height = 500

rend = Renderer(width, height)

rend.glLoadModel("Mandalorian.obj", 
                 translate= V3(width/2, height/3.5, 0), 
                 scale= V3(10, 10, 10))

rend.glFinish("Mandalorian.bmp")

