from vec import Vec
from mat import Mat
from matutil import coldict2mat
from math import *


def identity_pos(): return Mat(({'x','y','u'},{'x','y','u'}),{(d,d):1 for d in {'x','y','u'}})

def identity_col(): return Mat(({'r','g','b'},{'r','g','b'}),{(d,d):1 for d in {'r','g','b'}})

# 5.15.3
def translation(alpha,beta): return Mat(({'x','y','u'},{'x','y','u'}), ({('x','x'):1,('y','y'):1,('u','u'):1,('x','u'):alpha,('y','u'):beta}))

# 5.15.4
def scale(alpha,beta): return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):alpha, ('y','y'):beta, ('u','u'):1})

# 5.15.5
'''
reverse clock order
cos : -sin
sin : cos
'''
def rotation(theta): return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):cos(theta),('x','y'):-sin(theta),('y','x'):sin(theta),('y','y'):cos(theta),('u','u'):1 })
'''
clock order
cos  : sin
-sin : cos
'''
def rotation_(theta): return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):cos(theta),('x','y'):sin(theta),('y','x'):-sin(theta),('y','y'):cos(theta),('u','u'):1 })


# 5.15.6
def rotation_about(theta,x,y): return rotation(theta)*Mat(({'x','y','u'},set(range(1))),{('x',0):x,('y',0):y,('u',0):1})
def rotation_about_(theta,x,y): return rotation_(theta)*Mat(({'x','y','u'},set(range(1))),{('x',0):x,('y',0):y,('u',0):1})

# 5.15.7
def reflect_y(): return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):-1,('y','y'):1,('u','u'):1})

# 5.15.8
def reflect_x(): return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):1,('y','y'):-1,('u','u'):1})

# 5.15.9
def scale_color(r,g,b): return Mat(({'r','g','b'},{'r','g','b'}), {('r','r'):r,('g','g'):g,('b','b'):b})

# 5.15.10
def grayscale():
    D={'r','g','b'}
    r=Vec(D,{d:77/256 for d in D})
    g=Vec(D,{d:151/256 for d in D})
    b=Vec(D,{d:28/256 for d in D})

    dicts={'r':r, 'g':g, 'b':b}

    return coldict2mat(dicts)

# 5.15.11
def reflect_about(x1,y1,x2,y2):
    '''
    0. move the line passing (x1,y1) and (x2,y2) to core
    1. decline line to 0 degree
    2. x-axis reflection
    3. reversing step-1
    4. reversing step-0
    ==
    0. translation to core
    1. rotation to 0
    2. reflect_x
    3. rotation to origin
    4. translation to origin
    -------------------------
    return 4*3*2*1*0
    '''

    # y = a * x + b
    a=(y2-y1)/(x2-x1)
    b=(y1-x1*a)

    # coordinate that pass core and vertical to y
    alpha=-(a*b)/(a**2+1)
    beta=b/(a**2+1)

    # equation moved to core is below
    # y = a*x + b +a*alpha - beta

    M0=translation(-alpha,-beta)

    theta = atan(a)
    M1=rotation_(theta)

    M2=reflect_x()

    M3=rotation(theta)

    M4=translation(alpha,beta)

    return M4*M3*M2*M1*M0