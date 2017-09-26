import sys
sys.path.append("D:\Python\Matrix")

from simplex import *
from matutil import *
from vecutil import *
from solver import *

# 14.16.2
def find_move_helper(A,r):
    D=A.D[0]

    b=Vec(D,{r:1})

    w=solve(A,b)

    # return solve(A,Vec(A.D[1],{r:1}))
    return w

# 14.16.3
def find_move_direction(A,x,r):
    w=find_move_helper(A,r)

    print(w)
    print(A*x)
    print(A*(x+w))

    # return find_move_helper(A,r)
    return w

# 14.16.4
def find_move(A,x,r):
    w=find_move_direction(A,x,r)

    if min(w.f.values()) >= 0:
        return w,'any sigma'

    former_sigma=0

    for iter in range(10):
        sigma=iter + 1
        print(sigma)
        print(x+ sigma*w)
        # pick biggest sigma that allows non-negative-entries for (x + sigma*w)
        if min((x + sigma*w).f.values()) <= 0:
            if former_sigma == 0:
                return w,'no proper sigma'
            return w,former_sigma
        former_sigma=sigma


    return w,'no proper sigma'

A=listlist2mat([[50,0],[100,150],[0,50],[50,30],[1,0],[0,1]])
x=list2vec([1,1])
b=list2vec([200,1000,300,300,0,0])
# w,sigma=find_move(A,x,1)
#
# print(w)
# print(sigma)

c=list2vec([1,1.6])
