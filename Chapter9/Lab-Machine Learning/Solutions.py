import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one
from vec import Vec
from mat import Mat
from echelon import *

from vecutil import *
from matutil import *
from cancer_data import *
from solver import solve
# from root import solve

# 9.4.1
A,b=read_training_data('train.data')

# 9.4.2
def signum(u): return Vec(u.D,{k:1 if u[k]>=0 else -1 for k in u.f.keys() })

# 9.4.3
def fraction_wrong(A,b,w):

    # rank A*w == rank b
    # type(signum(A*w)) == type(signum(b))
    sig_Aw=signum(A*w)
    sig_b=signum(b)

    different_count=sum(1 if sig_Aw[d] != sig_b[d] else 0 for d in sig_Aw.D)
    total=len(b.D)

    return different_count/total

# 9.4.4
def loss(A,b,w):

    errors = A*w - b

    L=sum(errors[k]**2 for k in errors.f.keys())

    return L

# 9.4.9
def find_grad(A,b,w):
    a=mat2rowdict(A)
    grad=sum([2*(a[key]*w - b[key])*a[key] for key in a.keys()])

    return grad

# 9.4.10
def gradient_descent_step(A,b,w,sigma): return w - sigma*find_grad(A,b,w)

# 9.4.11
def gradient_descent(A,b,w,sigma,T):
    next_w=w

    for each in range(T):
        next_w=gradient_descent_step(A,b,next_w,sigma)

        # if each%30==0:
            # print(loss(A,b,next_w))
            # print(fraction_wrong(A,b,next_w))
            # print(next_w)

    print('loss value of final w')
    print(loss(A,b,next_w))
    return next_w