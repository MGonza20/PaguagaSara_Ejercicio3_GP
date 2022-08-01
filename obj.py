# Sara Paguaga 20634

from sys import prefix

class Obj(object):
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()


        self.vertices = []
        self.textcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                # se separa el prefijo del resto del valor cuando lee el doc
                prefix, value = line.split(' ', 1)
            except:
                continue
            
            #trata de leer vertices
            if prefix == 'v':
                self.vertices.append(list(map(float, value.split(' '))))

            elif prefix == 'vt':
                self.textcoords.append(list(map(float, value.split(' '))))

            elif prefix == 'vn':
                self.normals.append(list(map(float, value.split(' '))))

            elif prefix == 'f':
                self.faces.append([  list(map(int, vert.split('/'))) for vert in value.split(' ')] )


