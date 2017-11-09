from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from numpy import *
from sys import *
from math import cos as cosine
from math import sin as sinus
from matrix import *
from copy import *

print ('Lets start!\n\n')

def translate(dx,dy):
    global coords
    transformation = [[1, 0, 0],[0,1,0],[dx,dy,1]]
    coords = multiplyMatrix(transformation, coords)

def dilate(k):
    global coords
    transformation = [[k, 0, 0],[0,k,0],[0,0,1]]
    coords = multiplyMatrix(transformation,coords)

def rotate(deg,a,b):
    global coords

    baseTransformation = [[cosine(deg), sinus(deg), 0], [-sinus(deg), cosine(deg), 0], [0,0,1]]
    p1 = [[1,0,0],[0,1,0],[a + 249,b + 249,1]]
    p2 = [[1, 0, 0], [0, 1, 0], [-a -249, -b - 249, 1]]

    coords = multiplyMatrix(multiplyMatrix(multiplyMatrix(p1, baseTransformation), p2), coords)

def reflectX(x):
    t = x + 249
    if (t > 249):
        translate(0, -t)
    elif(t +0< 249):
        translate(0, t+0)
    else:
        return
    global coords
    transformation = [[1, 0, 0],[0, -1, 0],[0,0,1]]
    coords = multiplyMatrix(transformation, coords)

    if (t +0> 249):
        translate(0, t+0)
    elif (t +0< 249):
        translate(0, -t+0)

def reflectY(t):
    t = t + 249
    if (t + 0 > 249):
        translate(-t+0, 0)
    elif(t + 0< 249):
        translate(t-0, 0)
    else:
        return
    global coords
    transformation = [[-1, 0, 0],[0, 1, 0],[0,0,1]]
    coords = multiplyMatrix(transformation, coords)

    if (t +0 > 249):
        translate(t-0, 0)
    elif (t +0 < 249):
        translate(-t+0, 0)


def reflect(x, y):
    global coords

    if (x == 0 and y == 0):
        t = [[-1,0,0],[0,-1,0],[0,0,1]]
        coords = multiplyMatrix(t, coords)
        translate(2 * 249, 2 * 249)
        return
    reflectX(x)
    reflectY(y)


def shear(axis, m):
    global coords
    if (axis == "y" or axis == "Y"):
        transformation = [[1, m, 0], [0,1,0],[0,0,1]]
        coords = multiplyMatrix(transformation, coords)
    elif (axis == "x" or axis == "X"):
        transformation = [[1, 0, 0], [m, 1, 0], [0, 0, 1]]
        coords = multiplyMatrix(transformation, coords)
    else:
        print("Error: invalid axis")

def stretch(axis, k):
    global coords
    if (axis == "y" or axis == "Y"):
        transformation = [[1, 0, 0], [0, k, 0], [0, 0, 1]]
        coords = multiplyMatrix(transformation, coords)
    elif (axis == "x" or axis == "X"):
        transformation = [[k, 0, 0], [0, 1, 0], [0, 0, 1]]
        coords = multiplyMatrix(transformation, coords)
    else:
        print("Error: invalid axis")

def custom(a,b,c,d):
    global coords
    transformation = [[a,c,0],[b,d,0],[0,0,1]]
    coords = multiplyMatrix(transformation, coords)

def multiple():
    global segi
    global coords
    global initcoords

    n = int(input("Number of command > "))

    op = []
    for i in range(n):
        cmd = input("Command " + str(i) + " : ")
        if cmd == "multiple":
            print("Cannot do multiple command inside a multiple command")
        else:
            op += [cmd]

    for i in op:
        opr = []
        for field in i.split():
            opr.append(field)
        wrongCommand = False

        if opr[0] == "translate":
            if (len(opr) == 3):
                (translate(float(opr[1]), float(opr[2])))  # (dx, dy)
            else:
                wrongCommand = True
        elif opr[0] == "dilate":
            if (len(opr) == 2):
                dilate(float(opr[1]))
            else:
                wrongCommand = True
        elif opr[0] == "rotate":
            if len(opr) == 4:
                rotate(float(opr[1]), float(opr[2]), float(opr[3]))  # (deg, x, y)
            else:
                wrongCommand = True
        elif opr[0] == "reflect":
            if len(opr) == 3:
                reflect(float(opr[1]), float(opr[2]))  # (x, y)
            else:
                wrongCommand = True
        elif opr[0] == "shear":
            if len(opr) == 3:
                shear(opr[1], float(opr[2]))  # (axis, factor)
            else:
                wrongCommand = True
        elif opr[0] == "stretch":
            if len(opr) == 3:
                stretch(opr[1], float(opr[2]))  # (axis, factor)
            else:
                wrongCommand = True
        elif opr[0] == "custom":
            if len(opr) == 5:
                custom(int(opr[1]), int(opr[2]), int(opr[3]), int(opr[4]))
            else:
                wrongCommand = True

        elif opr[0] == "multiple":
            multiple()
        elif opr[0] == "reset":
            coords = reset(initcoords)
        elif opr[0] == "exit":
            sys.exit()
        else:
            print("Maaf, masukan operasi salah")

        if wrongCommand:
            print("Error: not enough arguments")

def reset(initcoords):
    global coords
    coords = deepcopy(initcoords)

def operate(segi,coords, initcoords):
    opr = []
    operation = input("Masukkan operasi yang ingin dilakukan: ")#.split()
    for field in operation.split():
        opr.append(field)
    wrongCommand = False

    if opr[0] == "translate":
        if (len(opr) == 3):
            (translate(float(opr[1]), float(opr[2]))) #(dx, dy)
        else:
            wrongCommand = True
    elif opr[0] == "dilate":
        if (len(opr) == 2):
            dilate(float(opr[1]))
        else:
            wrongCommand = True
    elif opr[0] == "rotate":
        if len(opr) == 4:
            rotate(float(opr[1]), float(opr[2]), float(opr[3])) #(deg, x, y)
        else:
            wrongCommand = True
    elif opr[0] == "reflect":
        if len(opr) == 3:
            reflect(float(opr[1]), float(opr[2])) #(x, y)
        else:
            wrongCommand = True
    elif opr[0] == "shear":
        if len(opr) == 3:
            shear(opr[1], float(opr[2])) #(axis, factor)
        else:
            wrongCommand = True
    elif opr[0] == "stretch":
        if len(opr) == 3:
            stretch(opr[1],float(opr[2])) #(axis, factor)
        else:
            wrongCommand = True
    elif opr[0] == "custom":
        if len(opr) == 5:
            custom(int(opr[1]),int(opr[2]),int(opr[3]),int(opr[4]))
        else:
            wrongCommand = True
    elif opr[0] == "multiple":
        multiple()
    elif opr[0] == "reset":
        reset(initcoords)
    elif opr[0] == "exit":
        sys.exit()
    else:
        print ("Maaf, masukan operasi salah")

    if wrongCommand:
        print("Error: not enough arguments")

#Class yang menyimpan pasangan koordinat(x,y), akan digunakan pada array of vertex
# class Vertex:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

def drawShape(segi, coords):
    glBegin(GL_LINE_LOOP)  # start drawing a rectangle
    for z in range(segi):
        glVertex3f(coords[z][0], coords[z][1], 0)  # bottom left point
    glEnd()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    glColor3f(0.0, 0.0, 1.0)  # set color to blue
    drawShape(segi, coords)  # rect at (10, 10) with width 200, height 100

    glColor3f(1.0, 0.0, 0.0)  # set color to blue
    drawShape(2, [[0,250,1],[499,250,1]])
    drawShape(2, [[250, 0, 1], [250, 499, 1]])
    # glBegin(GL_POLYGON)
    glutSwapBuffers()  # important for double buffering

#==================================================================================================
#==================================================================================================
#==================================================================================================



#Meminta masukan jumlah vertex (yang menentukan segi berapa)
segi = int(input("Masukkan segi berapa yang ingin diolah: "))

#Inisialisasi array of vertex & meminta input koordinat bidang
coords = [None]*segi
for z in range(segi):
    x = int(input("Masukkan koordinat x untuk simpul "+ str(z) +": "))
    y = int(input("Masukkan koordinat y untuk simpul "+ str(z) +": "))
    coords[z] = [x + 249, y + 249, 1]

# print(coords)
for v in coords:
    print(" [" + str(v[0]-249) + "," + str(v[1]-249) + "] "),
# initcoords = [None]*segi
# for z in range(segi):
# 	initcoords[z] = Vertex(coords[z].x,coords[z].y)
initcoords = deepcopy(coords)
#Menggambar pada OpenGL

window = 0                                             # glut window number
width, height = 500, 500                               # window size

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"AllGeo")              	   # create window with title
draw()

#Melakukan operasi
loop = True

while(loop):
    operate(segi,coords, initcoords)
    for v in coords:
        print(" [" + str(v[0] - 249) + "," + str(v[1] - 249) + "] "),
    draw()


# def convertVertexToList(segi, v):
#     aColum ={None]}
#     for z in range(segi):


# def translate(segi,coords,dx,dy):
# 	for z in range(segi):
# 		coords[z].x += dx
# 		coords[z].y += dy
# 	return (coords)
#
# def dilate(segi,coords,k):
#     for z in range(segi):
#         coords[z].x *= k
#         coords[z].y *= k
#     return (coords)

# def translate(segi,coords,dx,dy):
#     for i in range(segi):
#         for j in range(len(coords[i])):
#             coords[i][j] += dx
#             coords[i][j] += dy
#
#     return (coords)

# def dilate(segi,coords,k):
#     for i in range(segi):
#         for j in range(len(coords[i])):
#             coords[i][j] *= k
#             coords[i][j] *= k
#
#     return (coords)

# def reset(segi,coords,initcoords):
#     for z in range(segi):
#         coords[z].x = initcoords[z].x
#         coords[z].y = initcoords[z].y
#     return (coords)

# def reset(segi,coords,initcoords):
#     for i in range(segi):
#         for j in range(len(coords[i])):
#             coords[i][j] = initcoords[i][j]
#             coords[i][j] = initcoords[i][j]
#
#     return(initcoords[:])