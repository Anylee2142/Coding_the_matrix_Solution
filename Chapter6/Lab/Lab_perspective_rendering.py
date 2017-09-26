import sys
sys.path.append("D:\Python\Matrix")

from matutil import *
from vecutil import *
from mat import Mat
from vec import Vec
import itertools
from solver import solve
from image_mat_util import *

C,R ={'x1','x2','x3'},{'y1','y2','y3'}

def move2board(y):
    return Vec(y.D,{key:(item/y['y3']) for (key,item) in y.f.items()})

def make_equations(x1,x2,w1,w2):
    u=Vec({d for d in itertools.product(R,C)}, {('y1','x1'):-x1,('y1','x2'):-x2,('y1','x3'):-1,('y3','x1'):w1*x1,('y3','x2'):w1*x2,('y3','x3'):w1})
    v=Vec({d for d in itertools.product(R,C)}, {('y2','x1'):-x1,('y2','x2'):-x2,('y2','x3'):-1,('y3','x1'):w2*x1,('y3','x2'):w2*x2,('y3','x3'):w2})
    return [u,v]

b = Vec( {d for d in itertools.product(R,C)} ,{('y3','x3'):1})

def make_L():
    dicts = dict()

    for i in set(range(4)):
        # print(2*i,2*i+1)
        result = make_equations(x1[i], x2[i], w1[i], w2[i])

        u = result[0]
        v = result[1]

        dicts[2 * i], dicts[2 * i + 1] = u , v

    dicts[8] = Vec( {d for d in itertools.product(R,C)} ,{('y1','x1'):1})

    return dicts

# D = itertools.product(R,C)

# Coordinates for whiteboard's 4 edges
# Refer to 277, 278 page
x1=[358,329,592,580]
x2=[36,597,157,483]
w1=[0,0,1,1]
w2=[0,1,0,1]

L=make_L()
L=rowdict2mat(L)

print(L)

# print(transpose(L))

# print(b)

# (y1,x1) entry should be 1 because of scale-equation noted in text-book
# and this is one of the root-set which (y1,x1) entry is 1
h=Vec( {d for d in itertools.product(R,C)} , {('y1','x1'):1,('y1','x2'):0.052,('y1','x3'):-360.044,
                                              ('y2','x1'):-0.381,('y2','x2'):0.737,('y2','x3'):109.843,
                                              ('y3','x1'):-0.720,('y3','x2'):-0.011,('y3','x3'):667.93})
print(h)

# if you want to check 'h' is right solution,
# do substitution with 'h' to 6.12 or 6.13

H = Mat((R,C),{k:v for k,v in h.f.items() })

print(H)

#----------------------------------------------------------------------
print('Image Extraction Started')
(X_pts, colors)= file2mat('board.png',('x1','x2','x3'))
print('Finished')

# for key,value in X_pts.f.items():
#     print(key,value)

# mat2display(X_pts,colors,('x1','x2','x3'))

print('Converting to White_board_basis representation')
Y_pts=H*X_pts
print('Finished')

def mat_move2board(Y): return coldict2mat( {key:value/value['y3'] for key,value in mat2coldict(Y).items()} )
    # dicts={key:value/value['y3'] for key,value in mat2coldict(Y).items()}
    # return coldict2mat(dicts)

print('Converting to the cooredinates on the white_board representation')
Y_board=mat_move2board(Y_pts)
print('Finished')

# # Perspective rectification Display
mat2display(Y_board,colors,('y1','y2','y3'),scale=100,xmin=None,ymin=None)
# mat2display(X_pts,colors,('x1','x2','x3'))