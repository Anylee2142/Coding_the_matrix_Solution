import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one

from math import *
from vecutil import *
from matutil import *
from orthogonalization import *
from echelon import *

A=listlist2mat([[1,2],[3,4]])
lambda1=(5+sqrt(33))/2

B=A-lambda1*identity({0,1},1)

print(B)

cols=mat2coldict(B)

input=[each for each in cols.values()]

v1=list2vec([-1,cols[0][0]/cols[1][0]])

print(v1)
print(B*v1)
print(A*v1)
print(lambda1*v1)

L=orthogonalize(input)
for each in L:
    print(each)