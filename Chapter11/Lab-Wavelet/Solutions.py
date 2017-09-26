import sys
sys.path.append("D:\Python\Matrix")

from math import *

from vecutil import *
from matutil import *

# 11.9.1
def forward_no_normalization(v):
    D={}

    while len(v) > 1:
        k=len(v)
        vnew=[ (v[2*i] + v[2*i+1])/2 for i in range(k//2)]
        w=[v[2*i] - v[2*i+1] for i in range(k//2)]

        for i in range(k//2):
            D[(k//2,i)]=w[i]

        v=vnew

    D[(0,0)]=v[0]

    return D

# 11.9.2
def normalize_coefficients(n,D):

    for k in D.keys():
        s=k[0]

        if s == 0:
            mul=sqrt(n)
        else:
            mul=sqrt(n/(4*s))

        D[k]=mul*D[k]

    return D

# 11.9.3
def forward(v): return normalize_coefficients(len(v),forward_no_normalization(v))

# 11.9.4
def suppress(D,threshold): return {k:0 if abs(D[k])<abs(threshold) else D[k] for k in D.keys()}

# 11.9.5
def sparsity(D): return sum(1 for v in D.values() if v != 0 )/len(D.keys())

# 11.9.6
def unnormalize_coefficients(n,D):

    for k in D.keys():
        s=k[0]

        if s == 0:
            div=sqrt(n)
        else:
            div=sqrt(n/(4*s))

        D[k]=D[k]/div

    return D

# 11.9.7
def backward_no_normalization(D):
    n=len(D)

    # v starts with w1
    # w1 = D[(0,0)]
    v=[D[(0,0)]]
    wstart=1

    while len(v) < n:
        w=[k for k in D.keys() if k[0]==wstart]
        vnew=[]

        for V,W in zip(v,w):
            vnew.append((2*V + D[W])/2)
            vnew.append((2*V - D[W])/2)

        v=vnew
        wstart+=1

    return v

# 11.9.8
def backward(D): return backward_no_normalization( unnormalize_coefficients(len(D.keys()) ,D) )



