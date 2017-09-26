import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one
from vec import Vec
from mat import Mat
from echelon import *

from vecutil import *
from matutil import *

# 9.3.12
def project_along(b,v):
    # Return projection of b along v
    # projection of b along v = b || v = coef * v

    coef = (b*v)/(v*v) if v*v>1e-20 else 0

    return coef*v

# 9.3.13
def project_orthogonal_1(b,v): return b - project_along(b,v)

# 9.3.15
def projection_matrix(v):
    # Refer to the page 385
    coldicts={0:v}
    v_m=coldict2mat(coldicts)
    v_m_t=transpose(v_m)

    return v_m*v_m_t

# test-case for 9.3.15
v=list2vec([6,2])
M=projection_matrix(v)
print(M)
b=list2vec([2,4])

print(M*b)