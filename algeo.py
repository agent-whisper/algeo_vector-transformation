from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from numpy import *

print 'Lets start!\n\n'

class Vertex:
	def __init__(self,x,y):
		self.x = x
		self.y = y

segi = int(raw_input("Masukkan segi berapa yang ingin diolah: "))

coords = [None]*segi
for z in range(segi):
	x,y = map(int,raw_input("Masukkan koordinat ke "+ str(z) +": ").split(' '))
	coords[z] = Vertex(x,y)


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
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything