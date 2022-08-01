#Sara Paguaga 20634

from library import Renderer, color, V2, V3
import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("Mandalorian.obj", 
                 translate= V3(width/2, height/4, 0), 
                 scale= V3(24, 24, 24))

rend.glFinish("Mandalorian.bmp")

