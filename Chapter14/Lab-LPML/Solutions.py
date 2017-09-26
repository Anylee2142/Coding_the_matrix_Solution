import sys
sys.path.append("D:\Python\Matrix")

from simplex import *
from matutil import *
from vecutil import *
from solver import *
from cancer_data import *

# 14.13.1
def main_constraint(i , a_i , d_i, D):

    result=Vec(D,{})

    # about a_i and gamma
    for idx,val in a_i.f.items():
        sign=1
        if d_i < 0:
            sign*=-1
        result[idx]=sign*val

    result['gamma']=-sign
    result[i]=1

    return result

# 14.13.4
def non_negative_constraint(i_set,i,D):
    return Vec(D,{each:1 for each in i_set if each==i})

# 14.13.5
def make_A(feature_vectors,diagnoses,features):
    rows={}

    i_set=set(feature_vectors.keys())
    D = features.union(i_set.union({'gamma'}))

    rows={i:main_constraint(i,a_i,diagnoses[i],D) for i,a_i in feature_vectors.items()}
    rows.update({-i:non_negative_constraint(i_set,i,D) for i in feature_vectors.keys()})

    return rowdict2mat(rows)

# 14.13.6
def make_b(A):
    return Vec(A.D[0],{each: 1 if each >0 else 0 for each in A.D[0]})

# 14.13.7
def make_c(A):
    return Vec(A.D[1],{each:1 for each in A.D[1] if isinstance(each,int)is True})

A, b = read_training_data('train.data', {'area(worst)', 'smoothness(worst)', 'texture(mean)'})

feature_vectors=mat2rowdict(A)
diagnoses=b
features=A.D[1]
pat_ID=A.D[0]

A=make_A(feature_vectors,diagnoses,features)
b=make_b(A)
c=make_c(A)
R_square={-each for each in pat_ID}
R_square.update({843786,864292,856106,862261})
#R_square represents start-vertex

find_vertex(A,b,R_square)
A_square = Mat((R_square, A.D[1]), {(r,c):A[r,c] for r,c in A.f if r in R_square})
b_square = Vec(R_square, {k:b[k] for k in R_square})
solution=solve(A_square,b_square)