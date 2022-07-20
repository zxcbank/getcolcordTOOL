import numpy as np
import cv2

img1 = cv2.imread('MAP.png')
(WIDTH, HEIGHT) = img1.shape[:2]

Scor = []
Bcor = []
Tcor = []

TER_DB = open("TER_DB.txt", 'w')
SEA_DB = open("SEA_DB.txt", 'w')
BEACH_DB = open("BEACH_DB.txt", 'w')


for i in range(0, WIDTH):
    for j in range(0, HEIGHT):
        if img1[i, j][0] == 238:
            Scor.append([i, j])
        if img1[i, j][0] == 0:
            Bcor.append([i, j])
        if img1[i, j][0] == 255:
            Tcor.append([i, j])
TER_DB.write(str(Tcor))
BEACH_DB.write(str(Bcor))
SEA_DB.write(str(Scor))


