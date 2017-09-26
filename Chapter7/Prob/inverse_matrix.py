import sys
sys.path.append("D:\Python\Matrix")

from matutil import *
from mat import Mat

from vecutil import *
from vec import Vec

from GF2 import one
from triangular import *

from dimension_function import *

import itertools
from independence import *
from solver import solve


# 7.7.4
def morph(S,B):
    # Return tuple's list of z , w that exchange lemma
    # refer to iteration of Problem 7.1 at page 324

    '''
    >>> S=[list2vec(v) for v in [ [2,4,0], [1,0,3], [0,4,4], [1,1,1] ]]
    >>> B=[list2vec(v) for v in [ [1,0,0],[0,1,0],[0,0,1]]]
    >>> # morph(S,B)
    '''

    # 'result' contains tuple z,w
    result=[]

    # S morphing into T
    T=S.copy()

    for idx,val in enumerate(B):
        z=val
        w=T[idx]
        T.remove(w)
        T.insert(0,z)
        print('injecting',z)
        print('ejecting',w)

    return T

# 7.7.6
def my_is_independent(L):
    # Determine whether L is linear-independent or not
    # using 'rank' function from 'indepedence' module.
    # ( Returning length of list from subset_basis)

    '''
    >>> my_is_independent([list2vec(v) for v in [[2,4,0],[8,16,4],[0,0,7]]])
    False
    >>> my_is_independent([list2vec(v) for v in [[2,4,0],[8,16,4]]])
    True
    '''

    if rank(L) == len(L):
        return True
    return False

# 7.7.7
def my_rank(L):
    # Return degree of L's rank

    '''
    >>> my_rank([list2vec(v) for v in [ [1,2,3],[4,5,6],[1,1,1] ]])
    2
    '''

    return len(subset_basis(L))

# 7.7.11
def direct_sum_decompose(U_basis,V_basis,w):
    # Return representation u that (U+V) * u = w
    # 0. A= coldict2mat(U_basis + V_basis)
    # 1. rep = vec2rep(A,w)
    # 2. Derive u, v from rep
    # (Several different representation from different basis for one same vector)
    # (For this case, Basis can be U, V, U +V

    A=U_basis + V_basis

    rep=vec2rep(A,w)

    # Domain for each 'u' and 'd'
    u_D=set(range(len(U_basis)))
    v_D=set(range(len(V_basis)))

    # 'u','v' that U*u + V*v = w
    u=Vec(u_D, {d:rep[d] for d in u_D})
    v=Vec(v_D, {d:rep[len(U_basis) + d] for d in v_D })

    print(rep)

    return (u,v)

## Below is the test-case for # 7.7.11
# U_basis=[list2vec(v) for v in [[2,1,0,0,6,0],[11,5,0,0,1,0],[3,1.5,0,0,7.5,0]] ]
# V_basis=[list2vec(v) for v in [[0,0,7,0,0,1],[0,0,15,0,0,2]] ]
# w=[list2vec(v) for v in [[2,5,0,0,1,0],[0,0,3,0,0,-4],[1,2,0,0,2,1],[-6,2,4,0,4,5]] ]
#
# for each in w:
#     direct_sum_decompose(U_basis,V_basis,each)

# 7.7.12
def is_invertible(M):
    # Determine wheter M is invertible or not

    # If M is invertible,
    # 0. |R| == |C|
    # 1. Column space of M == linear-independent
    # ( Same as invertible linear function, because matrix can be represented as linear-function)

    # If 0 and 1 satisfied, Return True


    '''
    >>> M=listlist2mat([[1,0,0],[0,1,0],[0,0,1]])
    >>> A=listlist2mat([[1,1,1,1],[0,0,0,0]])

    >>> is_invertible(M)
    True
    >>> is_invertible(A)
    False
    '''

    # 0.
    R = len(M.D[0])
    C = len(M.D[1])

    if R != C:
        return False

    # 1.
    coldicts=mat2coldict(M)

    L = [each for each in coldicts.values()]

    if my_is_independent(L) is True:
        return True

# 7.7.13
def find_matrix_invertible(A):
    # Return inverse matrix of A

    # 0. find vector u that A*u = Identity-Vector
    # 1. make matrix with collection of u
    #   == Invertible matrix of A

    # This function can be modified for proper domain

    '''
    >>> A=listlist2mat([[1,1,0],[0,1,0],[0,0,1]])
    >>> B=listlist2mat([[1,1,1,1],[2,2,2,2]])
    >>> C=listlist2mat([[0,2,-2],[3,1,0],[1,0,1]])
    >>> #print(A*find_matrix_invertible(A))
    '''

    if is_invertible(A) is not True:
        return print('A is not invertible')

    # 0
    coldicts=mat2coldict(A)
    u=dict()

    for idx,val in enumerate(coldicts.values()):
        Identity_Vector = Vec(A.D[0], {idx:1})
        u[idx]=solve(A,Identity_Vector)

    # 1
    Inverse_A = coldict2mat(u)

    return Inverse_A

# 7.7.14
def find_tri_matrix_inverse(A):
    # Return Inverse matrix of upper-triangular-system
    # Same procedure as 7.13 but triangular_solve_n

    '''
    >>> A=listlist2mat([[1,1,1],[0,1,2],[0,0,1]])
    '''

    if is_invertible(A) is not True:
        return print('A is not invertible')

    # making argument 'b' for triangular_solve_n
    D=range(len(A.D[0]))
    b=[ [1 if each==i else 0 for each in D] for i in D]

    # 0.
    rowdicts=mat2rowdict(A)
    L=[val for val in rowdicts.values()]

    u=dict()

    for idx,val in enumerate(b):
        u[idx]=triangular_solve_n(L,val)

    # 1
    Inverse_A=coldict2mat(u)

    return Inverse_A

# A=listlist2mat([[1,1,1],[0,1,2],[0,0,1]])
# find_tri_matrix_inverse(A)