import sys
sys.path.append("D:\Python\Matrix")

from GF2 import one

from math import *
from vecutil import *
from matutil import *
from orthogonalization import *

def find_V(U,W):
    # Return V that U's orthogonal complement space to W
    # U = list that vectors
    # W = list that vectors

    W_basis=orthogonalize(W)
    U_basis=orthogonalize(U)

    L = U_basis + W_basis

    ortho_results=orthogonalize(L)

    # After orthogonalize(L), delete U's entries
    # Then V remains.
    for each in range(len(U_basis)):
        ortho_results.remove(ortho_results[0])

    remove_idx=[]
    for idx,val in enumerate(ortho_results):
        # If certain entry's square itself is less than e-20,
        # we assume that entry is 0-vector
        if val*val <= 1e-20:
            remove_idx.append(idx)

    remove_entry=[ortho_results[i] for i in remove_idx]
    for each in remove_entry:
        ortho_results.remove(each)

    return ortho_results

# 10.11.9
def orthonormalize(L):
    # Refer to the page 407
    result=orthogonalize(L)

    normalized=[result[idx]/sqrt(val*val) for idx,val in enumerate(result)]

    return normalized

# 10.11.10
def aug_orthonormalize(L):
    # Refer to the page 407
    Q, R = aug_orthogonalize(L)

    Qlist=orthonormalize(Q)

    # Multiplication R as much as Division Q
    # As much as sqrt(Q[i]*Q[i])), norm of each Q's col
    R=mat2rowdict(coldict2mat(R))
    Rlist=[sqrt(Q[i]*Q[i])*R[i] for i in range(len(R))]
    Rlist=mat2coldict(rowdict2mat(Rlist))

    return Qlist,Rlist

