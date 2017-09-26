import sys
sys.path.append("D:\Python\Matrix")

from matutil import *
from mat import Mat

from vecutil import *
from vec import Vec

import itertools
from solver import solve

# 6.14.13
def rep2vec(u,veclist):
    # Return v that A*u = v
    # 0. veclist into matrix with coldict2mat
    # (veclist into matrix is called A)
    # 1. return v that A*u=v
    # using matrix * vector = vector

    # 0
    coldicts={idx:value for idx,value in enumerate(veclist)}
    A = coldict2mat(coldicts)

    # 1
    v = A*u

    return v

# 6.14.14
def vec2rep(veclist,v):
    # Return u that A*u=v
    # monte-carlo-search : find only meaningful section
    # if 'u' is not within range, it doesn't return any
    # Don't use this function if other option has solver.solve

    M=coldict2mat({idx:val for idx,val in enumerate(veclist)})

    return solve(M,v)

                                # index of range can be modified
    # for i in itertools.product(range(15,-15,-1),repeat=len(veclist)):
    #     result=sum(scalar*veclist[idx] for idx,scalar in enumerate(i))
    #     print(result)
    #     if result==v:
    #         return Vec(set(range(len(veclist))) ,{idx:scalar for idx,scalar in enumerate(i)})
    # return print('No root found')

# 6.14.15
def is_superfluous(L,i):
    # Return true or false
    # whether L[i] can be represented by other vectors, linear dependent

    '''
    >>> D={'a','b','c','d'}
    >>> a0=Vec(D,{'a':1})
    >>> a1=Vec(D,{'b':1})
    >>> a2=Vec(D,{'c':1})
    >>> a3=Vec(D,{'a':1,'c':3})
    >>> L=[a0,a1,a2,a3]

    >>> is_superfluous(L,3)
    True

    >>> is_superfluous(L,0)
    True

    >>> is_superfluous(L,1)
    False
    '''

    # A*u = b
    b=L[i]
    L.remove(L[i])
    A=coldict2mat({idx:value for idx,value in enumerate(L)})

    u=solve(A,b)

    residual = b - A*u

    # L is called by reference so we should roll-back L
    L.insert(i,b)

    if residual*residual <=1e-14:
        return True
    else:
        return False

# 6.14.16
def is_independent(L):
    # Return true if one of vector in L is superfluous-vector
    '''
    >>> D={'a','b','c','d'}
    >>> a0=Vec(D,{'a':1})
    >>> a1=Vec(D,{'b':1})
    >>> a2=Vec(D,{'c':1})
    >>> a3=Vec(D,{'a':1,'c':3})
    >>> L=[a0,a1,a2,a3]

    >>> is_independent([a0,a1,a2])
    True
    >>> is_independent([a0,a2,a3])
    False
    >>> is_independent([a0,a1,a3])
    True
    >>> is_independent(L)
    False
    '''

    for idx,vec in enumerate(L):
        if is_superfluous(L,idx) == True:
            return False
    return True

# 6.14.17
def subset_basis(T):
    # Return basis of Span T
    # Note that there are many roots for 'subset_basis'
    '''
    >>> D={'a','b','c','d'}
    >>> a0=Vec(D,{'a':1})
    >>> a1=Vec(D,{'b':1})
    >>> a2=Vec(D,{'c':1})
    >>> a3=Vec(D,{'a':1,'c':3})
    >>> L=[a0,a1,a2,a3]

    # >>> subset_basis([a0,a1,a2,a3])

    # >>> subset_basis([a0,a3,a1,a2])
    '''

    for idx,vec in enumerate(T):
        if is_superfluous(T,idx) == True:
            T.remove(T[idx])
    return T

# 6.14.18
def superset_basis(T,L):
    # T = list of linear-independent vectors
    # Return Basis S of Span L
    # That T is from Span L means (Span L == Span T union L)
    # But L or T union L are not basis so we can get it by doing below
    # S == subset_basis(T union L)

    '''
    >>> D={'a','b','c','d'}
    >>> a0=Vec(D,{'a':1})
    >>> a1=Vec(D,{'b':1})
    >>> a2=Vec(D,{'c':1})
    >>> a3=Vec(D,{'a':1,'c':3})
    >>> L=[a0,a1,a2,a3]

    # >>> superset_basis([a0,a3],[a0,a1,a2])
    '''
                        # the reason list(set()) is to remove duplicated elements
    return subset_basis(list(set(T+L)))

# 6.14.19
def exchange(S,A,z):
    # Return w of S - A
    # A = part

    '''
    >>> L=[[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]
    >>> S=[list2vec(v) for v in L]
    >>> A=[list2vec(v) for v in [[0,0,5,3],[2,0,1,3]] ]
    >>> z=list2vec([0,2,1,1])
    >>> #exchange(S,A,z)
    '''

    # set_of_w == S - A
    tmp=S.copy()
    for each in A:
        tmp.remove(each)
    set_of_w=tmp

    # S * u = z
    coldicts={idx:value for idx,value in enumerate(S)}
    M=coldict2mat(coldicts)
    u=solve(M,z)

    # list that every possible w
    result=[]

    for each in set_of_w:
        # 'rest' is S - w
        rest=S.copy()
        rest.remove(each)

        # 'coef_of_w' is coefficient of w
        coef_of_w=u[S.index(each)]

        # 'sum_of_rest' is sum of sigma:coef*(S-w)
        sum_of_rest=sum(u[S.index(val)]*val for val in rest)

        # Below equation is at 270 page, at proof
        w=(z - sum_of_rest)/coef_of_w

        result.append(w)

    return result