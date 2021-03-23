import imageio
from random import *
import random

img=imageio.imread("area_image.PNG")
count_tri=0
count_sqr=0
count=0
while(count<=10000):
    x=random.randint(0,754)
    y=random.randint(0,1358)
    z=0
    if (img[x][y][z]==0):
        count_sqr+=1
        count+=1
    else:
        if(img[x][y][z]==91):
            count_tri+=1
            count+=1

area_tri=(count_tri/count_sqr)*1
print(area_tri)
