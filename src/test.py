from math import cos as cosine
from math import sin as sinus
from matrix import *
from copy import *

def translate(segi, coords, dx, dy):
    for i in range(segi):
        for j in range(len(coords[i])):
            coords[i][j] += dx
            coords[i][j] += dy

    return (coords)

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

# def reflect(segi, coords, x, y):

n = 3
v = [[100, 100, 1],[150,300, 1],[200,100, 1]]


def translate(segi, coords, dx, dy):
    transformation = [[1, 0, 0], [0, 1, 0], [dx, dy, 1]]

    return (multiplyMatrix(transformation, coords))

print(rotate(n, v, 90, 0, 0))
# print(reflectY(n, v))
# print (translate(n, v, 100, 50))