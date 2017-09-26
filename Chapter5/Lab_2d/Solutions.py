import sys
sys.path.append("D:\Python\Matrix")
from vec import Vec
from mat import Mat
from math import *
from image_mat_util import *
from transform import *


# 5.15.1
# image_mat[0] = position, image_mat[1]= color
image_mat=file2mat("img01.png")

# mat2display(image_mat[0],image_mat[1])

# e_pos=identity_pos()
# e_col=identity_col()

tmp=Mat(({'x','y','u'},{0}),{('x',0):0,('y',0):0,('u',0):1})

# mat2display(e_pos*image_mat[0],e_col*image_mat[1])

trans=translation(100,100)

# mat2display(trans*image_mat[0],image_mat[1])

# scal=scale(3,3)

# mat2display(scal*image_mat[0],image_mat[1])

# rot=rotation(pi/6)

# mat2display(trans*(rot*image_mat[0]),image_mat[1])

# print(rotation_about(pi/6,0,1))

# rfl_y=reflect_y()

# mat2display(trans*(rfl_y*image_mat[0]),image_mat[1])

# rfl_x=reflect_x()

# mat2display(trans*(rfl_x*image_mat[0]),image_mat[1])

# scal_col=scale_color(10,10,2)

# mat2display(image_mat[0],scal_col*image_mat[1])

# gray_col=grayscale()

# mat2display(image_mat[0],gray_col*image_mat[1])

# mat2display(reflect_about(0,-1,1,1)*image_mat[0],image_mat[1])

x1,y1,x2,y2=0,1,-4,0
mat2display(trans*(reflect_about(0,0,1,1)*image_mat[0]),image_mat[1])
