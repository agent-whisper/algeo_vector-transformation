from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from numpy import *
from sys import *

print 'Lets start!\n\n'

def translate(segi,coords,dx,dy):
	for z in range(segi):
		coords[z].x += dx
		coords[z].y += dy
	return (coords)

def dilate(segi,coords,k):
	for z in range(segi):
		coords[z].x *= k
		coords[z].y *= k
	return (coords)

def reset(segi,coords,initcoords):
	for z in range(segi):
		coords[z].x = initcoords[z].x
		coords[z].y = initcoords[z].y
	return (coords)

#Class yang menyimpan pasangan koordinat(x,y), akan digunakan pada array of vertex
class Vertex:
	def __init__(self,x,y):
		self.x = x
		self.y = y

#Meminta masukan jumlah vertex (yang menentukan segi berapa)
segi = int(raw_input("Masukkan segi berapa yang ingin diolah: "))

#Inisialisasi array of vertex & meminta input koordinat bidang
coords = [None]*segi
for z in range(segi):
	x,y = map(int,raw_input("Masukkan koordinat ke "+ str(z) +": ").split(', '))
	coords[z] = Vertex(x,y)

initcoords = [None]*segi
for z in range(segi):
	initcoords[z] = Vertex(coords[z].x,coords[z].y)

#Menggambar pada OpenGL

window = 0                                             # glut window number
width, height = 500, 500                               # window size

def drawShape(segi, coords):
    glBegin(GL_LINE_LOOP)     	                             # start drawing a rectangle
    for z in range(segi):	
    	glVertex3f(coords[z].x, coords[z].y, 0)                                   # bottom left point
    glEnd() 

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
        
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    drawShape(segi,coords)	                           # rect at (10, 10) with width 200, height 100
    
    glutSwapBuffers()                                  # important for double buffering

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("AllGeo")              	   # create window with title
draw()
#glutDisplayFunc(draw)                                  # set draw function callback
#glutIdleFunc(draw)                                     # draw all the time
#glutMainLoop()                                         # start everything

#Melakukan operasi
loop = True

while(loop):
	opr = []
	operation = raw_input("Masukkan operasi yang ingin dilakukan: ")#.split()
	for field in operation.split():
		opr.append(field)


	if opr[0] == "translate":
		coords = translate(segi,coords,int(opr[1]),int(opr[2]))
	elif opr[0] == "dilate":
		coords = dilate(segi,coords,float(opr[1]))
	elif opr[0] == "rotate":
		coords = rotate(segi,coords,int(opr[1]),int(opr[2]),int(opr[3]))
	elif opr[0] == "reflect":
		coords = reflect(segi,coords,int(opr[1]),int(opr[2]))
	elif opr[0] == "shear":
		coords = shear(segi,coords,opr[1],int(opr[2]))
	elif opr[0] == "stretch":
		coords = stretch(segi,coords,opr[1],int(opr[2]))
	elif opr[0] == "custom":
		coords = custom(segi,coords,int(opr[1]),int(opr[2]),int(opr[3]),int(opr[4]))
	elif opr[0] == "multiple":
		coords = multiple(segi,coords,int(opr[1]))
	elif opr[0] == "reset":
		coords = reset(segi,coords,initcoords)
	elif opr[0] == "exit":
		sys.exit()
	else:
		print "Maaf, masukan operasi salah"

	draw()