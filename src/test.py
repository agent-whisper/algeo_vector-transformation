from math import cos as cosine
from math import sin as sinus
from matrix import *
from copy import *

def reflectX(segi, coords):
    transformation = [[1,0],[0,-1]]
    return(multiplyMatrix(transformation, coords))

def reflectY(segi, coords):
    transformation = [[-1, 0], [0, 1]]
    return (multiplyMatrix(transformation, coords))


def rotate(segi, coords, deg, a, b):
    baseTransformation = [[cosine(deg), sinus(deg), 0], [-sinus(deg), cosine(deg), 0], [0, 0, 1]]
    p1 = [[1, 0, 0], [0, 1, 0], [a, b, 1]]
    p2 = [[1, 0, 0], [0, 1, 0], [-a, -b, 1]]

    result = multiplyMatrix(multiplyMatrix(multiplyMatrix(p1, baseTransformation), p2), coords)
    return (result)


def reflectX(x):
    global coords
    if (x > 0):
        translate(0, -x)
    elif (x < 0):
        translate(0, x)

    transformation = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
    coords = multiplyMatrix(transformation, coords)

    if (x > 0):
        translate(0, x)
    elif (x < 0):
        translate(0, -x)

# def reflect(segi, coords, x, y):

def translate(dx,dy):
    global coords
    transformation = [[1, 0, 0],[0,1,0],[dx,dy,1]]
    coords = multiplyMatrix(transformation, coords)

def reflectY(x):
    if (x > 0):
        translate(-x, 0)
    elif(x < 0):
        translate(x, 0)
    global coords
    transformation = [[-1, 0, 0],[0, 1, 0],[0,0,1]]
    coords = multiplyMatrix(transformation, coords)

    if (x > 0):
        translate(x, 0)
    elif (x < 0):
        translate(-x, 0)

def stretch(axis, m):
    global coords
    if (axis == "x" or axis == "X"):
        transformation = [[1, m, 0], [0,1,0],[0,0,1]]
        coords = multiplyMatrix(transformation, coords)
    elif (axis == "y" or axis == "Y"):
        transformation = [[1, 0, 0], [m, 1, 0], [0, 0, 1]]
        coords = multiplyMatrix(transformation, coords)
    else:
        print("Error: invalid axis")

n = 3
v = [[100, 100, 1],[150,300, 1],[200,100, 1]]
coords = deepcopy(v)

# print(rotate(n, v, 90, 0, 0))
# print(reflectY(n, v))
# print (translate(n, v, 100, 50))
# reflectX(50)
# reflectY(0)
# print(coords)

stretch('x', 1)
print (coords)